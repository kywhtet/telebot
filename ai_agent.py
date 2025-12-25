import requests
from dotenv import load_dotenv
import os

load_dotenv()


OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

class AIAgent:
    #@staticmethod
    def ai_chat(self, user_text):
        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        }

      
   

        payload = {
            "model": "gpt-4o-mini",  # you can use any model from OpenRouter
            "messages": [
                {
                "role": "system",
                    "content": (
                        "You are a helpful AI network infrastructure engineer. "
                        "Provide clear, concise, and short answers.")
                },
                {"role": "user", "content": user_text}
            ],
            "temperature": 0.2
        }

        response = requests.post(OPENROUTER_URL, headers=headers, json=payload)

        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            print("Error:", response.status_code, response.text)
            return None