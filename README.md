# Flutter WhatsApp OTP Authentication

A modern mobile authentication system built with Flutter and Python that uses WhatsApp for OTP delivery. Users can login with their phone number and receive verification codes directly through WhatsApp messages.

## Project Description

This project demonstrates a complete mobile authentication flow using modern technologies. The system consists of a Flutter mobile app that communicates with a Python FastAPI backend. When users want to login, they enter their phone number, receive a 4-digit OTP via WhatsApp, verify the code, and either login (if existing user) or complete registration (if new user).

The backend integrates with Message Central API to send WhatsApp messages, stores user data in JSON format, and provides REST API endpoints for the mobile app. The Flutter frontend features smooth animations, real-time validation, and a clean user interface.

This architecture is perfect for businesses wanting to implement phone-based authentication without the complexity of SMS costs, as WhatsApp messages are typically free for users.

## Features

- Phone number authentication with country code selection
- WhatsApp OTP delivery via Message Central API
- 4-digit OTP verification with auto-advance
- User registration with name and email
- Returning user detection and personalized welcome
- Clean, animated Flutter UI with haptic feedback
- FastAPI backend with automatic API documentation
- JSON-based user storage (easily upgradeable to database)
- Real-time form validation and error handling
- Cross-platform support (Android, iOS, Web)

## Technology Stack

**Mobile App:**
- Flutter 3.32.8
- Dart programming language
- HTTP package for API communication
- Material Design components

**Backend Server:**
- Python 3.8+
- FastAPI web framework
- Message Central WhatsApp API
- JSON file storage
- Uvicorn ASGI server

**External Services:**
- Message Central for WhatsApp OTP delivery

## Prerequisites

Before you begin, ensure you have:

1. Flutter SDK 3.0 or higher installed
2. Android Studio or VS Code with Flutter extensions
3. Python 3.8 or higher
4. Android device with USB debugging enabled OR Android emulator
5. Message Central account with API credentials
6. For phone testing: Both computer and mobile device on same WiFi network
7. For web testing: Chrome browser installed

## Installation Guide

### Backend Setup

1. Clone this repository
git clone https://github.com/PalMihani/LoginVerificationFlutter.git
cd LoginVerificationFlutter

text

2. Install Python dependencies
pip install fastapi uvicorn requests

text

3. Configure Message Central credentials
Open `main.py` and replace:
MESSAGE_CENTRAL_AUTH_TOKEN = "your_actual_auth_token_here"
MESSAGE_CENTRAL_CUSTOMER_ID = "your_actual_customer_id_here"

text

4. Start the backend server
uvicorn main:app --reload --host 0.0.0.0

text

### Mobile App Setup

1. Navigate to Flutter directory
cd flutter_app

text

2. Install dependencies
flutter pub get

text

3. Configure API connection (see platform-specific instructions below)

## Platform-Specific Launch Instructions

### Running on Chrome (Web Browser)

**Configuration:**
1. Edit `lib/config.dart` and set:
static const String baseUrl = "http://localhost:8000";

text

**Launch Steps:**
1. Make sure your backend is running:
uvicorn main:app --reload --host 0.0.0.0

text

2. Enable web support (if not already enabled):
flutter config --enable-web

text

3. Run on Chrome:
flutter run -d chrome

text

**Alternative Chrome Launch:**
flutter run -d web-server --web-port 3000

text
Then open `http://localhost:3000` in Chrome manually.

**Chrome-Specific Notes:**
- OTP will be received on your phone via WhatsApp
- Copy the OTP from your phone and enter it in the Chrome browser
- All animations and UI features work in Chrome
- Use Chrome DevTools for debugging (F12)

### Running on Android Phone

**Prerequisites:**
1. Enable Developer Options on your Android phone:
   - Go to Settings > About Phone
   - Tap "Build Number" 7 times rapidly
   - Go back to Settings > Developer Options
   - Enable "USB Debugging"

**Configuration:**
1. Find your computer's IP address:
   - **Windows:** Run `ipconfig` in Command Prompt (look for IPv4 Address)
   - **Mac/Linux:** Run `ifconfig` in Terminal (look for inet address)
   - Example: 192.168.1.100

2. Edit `lib/config.dart` and replace:
static const String baseUrl = "http://YOUR_COMPUTER_IP:8000";

text
Example:
static const String baseUrl = "http://192.168.1.100:8000";

text

**Launch Steps:**
1. Connect phone to computer via USB cable

2. Check device authorization:
   - Look for authorization dialog on your phone
   - Tap "Allow" or "OK"
   - Check "Always allow from this computer" (optional)

3. Verify device connection:
flutter devices

text
You should see your phone listed (e.g., "A142P (mobile)")

4. Start backend with external access:
uvicorn main:app --reload --host 0.0.0.0

text

5. Launch app on phone:
flutter run -d YOUR_DEVICE_ID

text
Or simply:
flutter run

text
Then select your phone from the device list.

**Phone-Specific Notes:**
- Both computer and phone must be on same WiFi network
- OTP will be received directly on the same phone running the app
- Hot reload works for instant code changes
- Use `flutter logs` to see debug output

### Running on Android Emulator

**Setup Emulator:**
1. Open Android Studio
2. Go to Tools > Device Manager
3. Create a new virtual device or start existing one

**Configuration:**
1. Edit `lib/config.dart`:
static const String baseUrl = "http://10.0.2.2:8000";

text
Note: `10.0.2.2` is the special IP for localhost from Android emulator

**Launch Steps:**
1. Start Android emulator from Android Studio

2. Verify emulator is running:
flutter devices

text

3. Start backend:
uvicorn main:app --reload

text

4. Launch app:
flutter run -d emulator-XXXX

text

**Emulator-Specific Notes:**
- OTP will be received on your physical phone
- Copy OTP from physical phone to emulator
- Emulator uses special localhost IP (10.0.2.2)
- Good for UI testing without device setup

## Quick Launch Commands

**For Chrome (Web):**
Terminal 1 - Start backend
uvicorn main:app --reload --host 0.0.0.0

Terminal 2 - Run Flutter web
flutter run -d chrome

text

**For Android Phone:**
Terminal 1 - Start backend
uvicorn main:app --reload --host 0.0.0.0

Terminal 2 - Connect phone and run
flutter devices
flutter run

text

**For Android Emulator:**
Terminal 1 - Start backend
uvicorn main:app --reload

Terminal 2 - Run on emulator
flutter run -d emulator-5554

text

## Project Structure

project-root/
├── main.py # FastAPI backend server
├── Users.json # User data storage
├── lib/
│ ├── main.dart # App entry point
│ ├── config.dart # API configuration
│ ├── login_screen.dart # Phone input screen
│ ├── otp_screen.dart # OTP verification screen
│ ├── signup_screen.dart # User registration screen
│ └── welcome_screen.dart # Success/welcome screen
├── android/ # Android-specific files
├── ios/ # iOS-specific files
├── web/ # Web-specific files
└── README.md

text

## Usage Flow

1. User opens the app (on phone/Chrome/emulator)
2. User enters phone number with country code
3. App sends request to backend
4. Backend calls Message Central API
5. User receives WhatsApp message with 4-digit OTP on their phone
6. User enters OTP in the app
7. Backend verifies OTP with Message Central
8. If user exists: Show welcome back message
9. If new user: Show registration form, then welcome message

## API Endpoints

- `POST /api/send_otp` - Send OTP to phone number
- `POST /api/verify_otp` - Verify OTP and check user existence
- `POST /api/signup` - Register new user
- `GET /docs` - API documentation (Swagger UI)

## Configuration Summary

| Platform | Backend Start Command | Config baseUrl | Flutter Run Command |
|----------|----------------------|----------------|---------------------|
| Chrome | `uvicorn main:app --reload --host 0.0.0.0` | `http://localhost:8000` | `flutter run -d chrome` |
| Android Phone | `uvicorn main:app --reload --host 0.0.0.0` | `http://YOUR_IP:8000` | `flutter run` |
| Android Emulator | `uvicorn main:app --reload` | `http://10.0.2.2:8000` | `flutter run -d emulator-XXXX` |

## Building for Production

### Create Release APK
flutter build apk --release

text

### Create Web Build
flutter build web

text

### Deploy Backend
Create `requirements.txt`:
fastapi
uvicorn[standard]
requests

text

Deploy to Railway, Heroku, or similar service.

## Troubleshooting

### Network Connection Issues
- **Chrome:** Verify backend at `http://localhost:8000/docs`
- **Phone:** Verify backend at `http://YOUR_IP:8000/docs` from phone browser
- **Emulator:** Verify backend at `http://10.0.2.2:8000/docs` from emulator browser
- Check both devices on same WiFi (for phone testing)
- Ensure backend started with `--host 0.0.0.0` (for phone testing)

### Device Connection Issues
- Enable Developer Options on Android
- Enable USB Debugging
- Accept authorization dialog on phone
- Try different USB cable
- Check `flutter doctor` for issues

### Platform-Specific Issues

**Chrome:**
- Enable web support: `flutter config --enable-web`
- Clear browser cache if issues persist
- Check browser console (F12) for errors

**Android Phone:**
- Device must be authorized for USB debugging
- Both devices must be on same WiFi network
- Try `flutter clean` then `flutter pub get`

**Android Emulator:**
- Use `10.0.2.2` instead of `localhost` or computer IP
- Ensure emulator has internet access
- Try cold boot if emulator acts strangely

### OTP Delivery Issues
- Verify Message Central credentials
- Check phone number format (+91XXXXXXXXXX)
- Ensure account has sufficient credits
- Test with different phone numbers

## Development Tips

### Adding Debug Logs
print("Making API call to: ${AppConfig.baseUrl}");
print("Response: ${response.body}");

text

### Testing Backend Directly
- **Chrome/Phone:** Visit `http://YOUR_IP:8000/docs`
- **Emulator:** Visit `http://10.0.2.2:8000/docs`

### Hot Reload
After changing IP configuration, restart Flutter completely:
Stop with Ctrl+C, then:
flutter run

text

### Multi-Platform Testing
Test your changes across platforms:
Test on Chrome
flutter run -d chrome

Test on phone
flutter run -d YOUR_DEVICE_ID

Test on emulator
flutter run -d emulator-XXXX

text

## Security Considerations

- Never commit API keys to version control
- Use environment variables in production
- Implement rate limiting for OTP requests
- Add request validation and sanitization
- Use HTTPS in production
- For web deployment, ensure CORS is properly configured

## Future Enhancements

- Add biometric authentication
- Implement user profile management
- Add push notifications
- Integrate with database (PostgreSQL/MongoDB)
- Add user activity logging
- Implement forgot password functionality
- Add iOS support

## Contributing

1. Fork the repository
2. Create feature branch
3. Test on multiple platforms (Chrome, Android)
4. Update documentation if needed
5. Submit pull request with description

## License

MIT License - feel free to use this project for learning or commercial purposes.

## Support

For issues or questions:
- Check troubleshooting section first
- Create GitHub issue with error details
- Include platform info (Chrome/Android/Emulator)
- Include device info and error logs
- Provide steps to reproduce problem

## Acknowledgments

- Message Central for WhatsApp API integration
- Flutter team for excellent cross-platform framework
- FastAPI for powerful Python web framework
- Community contributors and testers

---

Built with ❤️ using Flutter and Python
