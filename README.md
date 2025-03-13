# Whatsapp AI Reply Bot
This program automates a chat response system for WhatsApp using a combination of Python libraries and the Gemini API by Google.

Purpose:
The program's primary function is to monitor WhatsApp messages from a specific sender and generate an automated, human-like reply in real-time, mimicking Krish Kumar’s responses. The program reads the latest chat history, checks if the last message is from the specified sender, and then uses the Gemini AI model to generate a response based on the conversation.

How it works:

Launches WhatsApp: The program opens the WhatsApp application on the system.
Chat Monitoring: It continuously checks the last received message in a specific chat window.
Message Detection: If the last message is from the sender, the program grabs the chat history.
AI Response Generation: It sends the chat history to the Gemini AI model, requesting a conversational response, with specific guidelines to keep the replies short, friendly, and human-like.
Reply Automation: The generated reply is copied, and the program pastes it back into WhatsApp, sending the message.
Repetition: This cycle repeats every 20 seconds to keep monitoring and responding to new messages.
Key Features:

Automated, context-aware replies.
Integration with Google’s Gemini AI for generating natural-sounding responses.
Smooth integration with WhatsApp using pyautogui for controlling the interface.
In short, the program mimics a conversation with Krish Kumar while automating the reply generation for messages from a specific person
