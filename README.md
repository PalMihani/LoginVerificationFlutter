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
6. Both computer and mobile device on same WiFi network

## Installation Guide

### Backend Setup

1. Clone this repository
git clone https://github.com/yourusername/flutter-whatsapp-otp-auth.git
cd flutter-whatsapp-otp-auth

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

3. Configure API connection
Find your computer IP address:
- Windows: Run `ipconfig` in Command Prompt
- Mac/Linux: Run `ifconfig` in Terminal

Edit `lib/config.dart` and replace:
static const String baseUrl = "http://YOUR_COMPUTER_IP:8000";

text

4. Connect your Android device or start emulator

5. Run the app
flutter run

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
└── README.md

text

## Usage Flow

1. User opens the app and sees login screen
2. User enters phone number with country code
3. App sends request to backend
4. Backend calls Message Central API
5. User receives WhatsApp message with 4-digit OTP
6. User enters OTP in app
7. Backend verifies OTP with Message Central
8. If user exists: Show welcome back message
9. If new user: Show registration form, then welcome message

## API Endpoints

- `POST /api/send_otp` - Send OTP to phone number
- `POST /api/verify_otp` - Verify OTP and check user existence
- `POST /api/signup` - Register new user
- `GET /docs` - API documentation (Swagger UI)

## Configuration Options

### Development Configuration
Use your computer's local IP address for testing on physical device.

### Production Configuration
Deploy backend to cloud service like Railway, Heroku, or DigitalOcean.

### Message Central Setup
1. Sign up at Message Central website
2. Create WhatsApp Business API account
3. Get Auth Token and Customer ID from dashboard
4. Update credentials in main.py

## Building for Production

### Create Release APK
flutter build apk --release

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
- Verify backend runs at: http://YOUR_IP:8000/docs
- Check both devices on same WiFi
- Ensure backend started with --host 0.0.0.0

### Device Connection Issues
- Enable Developer Options on Android
- Enable USB Debugging
- Accept authorization dialog on phone
- Try different USB cable

### OTP Delivery Issues
- Verify Message Central credentials
- Check phone number format
- Ensure account has sufficient credits
- Test with different phone numbers

## Development Tips

### Adding Debug Logs
print("Making API call to: ${AppConfig.baseUrl}");
print("Response: ${response.body}");

text

### Testing Backend Directly
Visit http://YOUR_IP:8000/docs to test API endpoints manually.

### Hot Reload
After changing IP configuration, restart Flutter completely:
Stop with Ctrl+C, then:
flutter run

text

## Security Considerations

- Never commit API keys to version control
- Use environment variables in production
- Implement rate limiting for OTP requests
- Add request validation and sanitization
- Use HTTPS in production

## Future Enhancements

- Add biometric authentication
- Implement user profile management
- Add push notifications
- Integrate with database (PostgreSQL/MongoDB)
- Add user activity logging
- Implement forgot password functionality

## Contributing

1. Fork the repository
2. Create feature branch
3. Make changes with proper testing
4. Update documentation if needed
5. Submit pull request with description

## License

MIT License - feel free to use this project for learning or commercial purposes.

## Support

For issues or questions:
- Check troubleshooting section first
- Create GitHub issue with error details
- Include device info and error logs
- Provide steps to reproduce problem

## Acknowledgments

- Message Central for WhatsApp API integration
- Flutter team for excellent mobile framework
- FastAPI for powerful Python web framework
- Community contributors and testers

---

Built with ❤️ using Flutter and Python
