// lib/config.dart
class AppConfig {
  // For development, change this to your computer's IP address
  // For production, use your deployed backend URL
  static const String baseUrl = "http://YOUR_COMPUTER_IP:8000";
  
  // API endpoints
  static const String sendOtpEndpoint = "$baseUrl/api/send_otp";
  static const String verifyOtpEndpoint = "$baseUrl/api/verify_otp";
  static const String signupEndpoint = "$baseUrl/api/signup";
  
  // Instructions for setup:
  // 1. Find your computer's IP address:
  //    - Windows: Run 'ipconfig' in command prompt
  //    - Mac/Linux: Run 'ifconfig' in terminal
  // 2. Replace YOUR_COMPUTER_IP with your actual IP (e.g., 192.168.1.0)
  // 3. Make sure your backend runs with: uvicorn main:app --reload --host 0.0.0.0
}
