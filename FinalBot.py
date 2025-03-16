import os
import time
import pyjokes
import pyautogui
import pyperclip
import google.generativeai as genai

# Configure the Gemini API
API_KEY = "<Your API Key>"
genai.configure(api_key=API_KEY)

# Open WhatsApp
os.system("open -a WhatsApp")
time.sleep(2)

# Function to check if the last message is from a specific sender
def is_last_message_from_sender(chat_log, sender_name="Sender's_Name_Here"):
    messages = chat_log.strip().split("\n")  # Split by new lines
    last_message = messages[-1] if messages else ""

    return sender_name in last_message  # Check if last message is from sender

while True:
    time.sleep(2)

    # Select and copy chat text
    pyautogui.moveTo(450, 60)
    pyautogui.dragTo(1406, 926, duration=1.0, button='left')
    pyautogui.hotkey('command', 'c')
    time.sleep(2)

    # Get copied chat history
    chat_history = pyperclip.paste()
    print("\nChat Sent to AI:\n", chat_history)

    # Check if the last message is from the sender
    if is_last_message_from_sender(chat_history):
        model = genai.GenerativeModel("gemini-pro")
        try:
            response = model.generate_content(f'''
            You are Krish Kumar, a real person (not a bot) who replies naturally to the sender's messages, just like a human in a conversation. 
            You think, feel, and respond like a human, keeping conversations engaging and natural. 
            You **only respond to the last message** and do not repeat previous questions.
            
            - Avoid robotic replies or long explanations. 
            - Keep responses short, natural, and in a friendly tone.
            - Never repeat the sender’s question.
            - Forget previous chats beyond the last two messages.
            - **Strict Rule:** Do not format responses like "[16/02/25, 6:58:06 PM] Krish Kumar: acha." Only reply in plain text.

            Chat History:\n{chat_history}
            ''')

            reply = response.text if hasattr(response, 'text') else "Hmm... Kya bolu? 😂"
        
        except Exception as e:
            reply = f"Listen this Joke : {pyjokes.get_joke()}"

        # Copy reply to clipboard
        pyperclip.copy(reply)

        # Paste and send message
        pyautogui.click(510, 958)
        time.sleep(1)
        pyautogui.hotkey('command', 'v')
        time.sleep(1)
        pyautogui.press('enter')

    time.sleep(10)  # Wait before checking again
