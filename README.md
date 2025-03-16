# WhatsApp Auto Reply Bot using Gemini AI

## Overview
This Python script automates replies on WhatsApp using Google's Gemini AI. It reads incoming messages, checks if the last message is from a specific sender, generates a human-like response, and sends the reply automatically.

## Features
- Uses Google Gemini AI for generating natural replies.
- Reads the last received message to ensure context-aware responses.
- Prevents robotic or repetitive responses.
- Includes a fallback to send jokes if an error occurs.
- Works on macOS (since it uses `os.system("open -a WhatsApp")`).

## Requirements
- Python 3.x
- Install dependencies:
  ```sh
  pip install pyautogui pyperclip pyjokes google-generativeai
  ```
- Google Gemini API key (Replace `<Your API Key>` in the script)

## Setup & Usage
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo
   ```
2. Add your Gemini API key inside the script:
   ```python
   API_KEY = "your_google_gemini_api_key"
   ```
3. Run the script:
   ```sh
   python whatsapp_auto_reply.py
   ```
4. Make sure WhatsApp is open and visible on the screen.

## How It Works
- The script opens WhatsApp and copies chat history.
- It checks if the last message is from a specific sender.
- If yes, it generates a response using the Gemini AI API.
- The response is copied, pasted into the chat, and sent automatically.
- If an error occurs, it sends a joke instead.

## Notes
- Ensure that WhatsApp is positioned correctly on your screen for the automation to work.
- The script is designed for macOS; for Windows, replace `os.system("open -a WhatsApp")` with an appropriate command.
- Modify cursor coordinates if needed based on your screen resolution.

## Disclaimer
This script is for educational purposes only. Use responsibly and ensure compliance with WhatsApp's terms of service.

## License
[MIT License](LICENSE)

