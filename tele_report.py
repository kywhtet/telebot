import requests
from dotenv import load_dotenv
import os

load_dotenv()

# Replace with your bot's token


# Replace with your chat ID (this is my group ID name is my automation team)

BOT_TOKEN = os.getenv("BOT_TOKEN2")
CHAT_ID  = os.getenv("CHAT_ID")


class TeleService:
    def __init__(self):
        self.bot_token = BOT_TOKEN
        self.chat_id = CHAT_ID
# Send the message
    def send_telegram_message(self, message):
        url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"
        payload = {"chat_id": self.chat_id, "text": message, "parse_mode": "markdown"}
        print(message)
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print("Message sent successfully!")
        else:
            print(f"Failed to send message: {response.status_code}, {response.text}")
                

    




