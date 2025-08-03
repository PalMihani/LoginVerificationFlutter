from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import os, requests, json

# === Message Central API Settings ===
# IMPORTANT: Replace these with your actual Message Central credentials
MESSAGE_CENTRAL_AUTH_TOKEN = "YOUR_MESSAGE_CENTRAL_AUTH_TOKEN_HERE"
MESSAGE_CENTRAL_CUSTOMER_ID = "YOUR_CUSTOMER_ID_HERE"
MESSAGE_CENTRAL_SEND_URL = "https://cpaas.messagecentral.com/verification/v3/send"
MESSAGE_CENTRAL_VERIFY_URL = "https://cpaas.messagecentral.com/verification/v3/validateOtp"

USERS_FILE = "Users.json"

app = FastAPI()

# === Enable CORS for React frontend ===
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# === Store verification request IDs ===
verification_requests = {}

# === Load/Save Users JSON ===
def load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}

def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=4)

user_store = load_users()

# === Pydantic models ===
class PhoneNumber(BaseModel):
    phone: str

class OtpInput(BaseModel):
    phone: str
    otp: str

class SignupInput(BaseModel):
    phone: str
    name: str
    email: str

# === Send OTP via Message Central ===
@app.post("/api/send_otp")
def send_otp(data: PhoneNumber):
    # Extract mobile number (remove + and country code for the API)
    phone = data.phone.replace("+", "")
    
    # Remove country code (91) if present for mobile number parameter
    mobile_number = phone
    if phone.startswith("91") and len(phone) > 10:
        mobile_number = phone[2:]  # Remove the "91" prefix
    
    # Build the URL with query parameters
    url = f"{MESSAGE_CENTRAL_SEND_URL}?countryCode=91&customerId={MESSAGE_CENTRAL_CUSTOMER_ID}&flowType=WHATSAPP&mobileNumber={mobile_number}"
    
    headers = {
        'authToken': MESSAGE_CENTRAL_AUTH_TOKEN
    }
    
    response = requests.post(url, headers=headers, data={})
    
    print("=== Message Central SEND DEBUG ===")
    print("URL:", url)
    print("Status Code:", response.status_code)
    print("Response:", response.text)
    print("===================================")
    
    if response.status_code == 200:
        try:
            response_data = response.json()
            # Store the verification request ID for later verification
            if 'data' in response_data and 'verificationId' in response_data['data']:
                verification_id = response_data['data']['verificationId']
                verification_requests[data.phone] = verification_id
                return {"message": "OTP sent via Message Central WhatsApp", "success": True}
            else:
                return {"message": "OTP sent but no verification ID received", "response": response_data}
        except json.JSONDecodeError:
            return {"message": "OTP sent via Message Central", "response": response.text}
    else:
        raise HTTPException(status_code=500, detail=f"Failed to send OTP: {response.text}")

# === Verify OTP via Message Central ===
@app.post("/api/verify_otp")
def verify_otp(data: OtpInput):
    # Get the verification ID for this phone number
    verification_id = verification_requests.get(data.phone)
    if not verification_id:
        raise HTTPException(status_code=400, detail="No OTP request found for this number")
    
    # Extract mobile number for verification
    phone = data.phone.replace("+", "")
    mobile_number = phone
    if phone.startswith("91") and len(phone) > 10:
        mobile_number = phone[2:]
    
    # Build verification URL
    verify_url = f"{MESSAGE_CENTRAL_VERIFY_URL}?countryCode=91&mobileNumber={mobile_number}&verificationId={verification_id}&code={data.otp}"
    
    headers = {
        'authToken': MESSAGE_CENTRAL_AUTH_TOKEN
    }
    
    response = requests.get(verify_url, headers=headers)
    
    print("=== Message Central VERIFY DEBUG ===")
    print("Verify URL:", verify_url)
    print("Status Code:", response.status_code)
    print("Response:", response.text)
    print("=====================================")
    
    if response.status_code == 200:
        try:
            response_data = response.json()
            # Check if verification was successful
            if response_data.get('responseCode') == 200:
                # Clean up the verification request
                del verification_requests[data.phone]
                exists = data.phone in user_store
                
                # **FIXED: Return user data if exists**
                if exists:
                    user_data = user_store[data.phone]
                    return {
                        "message": "OTP verified successfully", 
                        "exists": True,
                        "user": {
                            "name": user_data.get("name"),
                            "email": user_data.get("email")
                        }
                    }
                else:
                    return {"message": "OTP verified successfully", "exists": False}
            else:
                raise HTTPException(status_code=400, detail="Invalid OTP")
        except json.JSONDecodeError:
            # Fallback for non-JSON response
            if "success" in response.text.lower():
                exists = data.phone in user_store
                if exists:
                    user_data = user_store[data.phone]
                    return {
                        "message": "OTP verified successfully", 
                        "exists": True,
                        "user": {
                            "name": user_data.get("name"),
                            "email": user_data.get("email")
                        }
                    }
                else:
                    return {"message": "OTP verified successfully", "exists": False}
            else:
                raise HTTPException(status_code=400, detail="Invalid OTP")
    else:
        raise HTTPException(status_code=400, detail="OTP verification failed")

# === Signup ===
@app.post("/api/signup")
def signup(data: SignupInput):
    if data.phone in user_store:
        raise HTTPException(status_code=400, detail="User already exists")
    user_store[data.phone] = {
        "name": data.name,
        "email": data.email
    }
    save_users(user_store)
    return {"message": "Signup successful"}

# === Serve React frontend ===
STATIC_DIR = "frontend-src/build/static"

if os.path.isdir(STATIC_DIR):
    app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

@app.get("/{full_path:path}")
def serve_react(full_path: str):
    index_path = os.path.join("frontend-src", "build", "index.html")
    if os.path.exists(index_path):
        return FileResponse(index_path)
    return {"message": "React frontend not built yet"}
