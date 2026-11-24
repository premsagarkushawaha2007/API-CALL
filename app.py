import requests
import os
from dotenv import load_dotenv

# Load API Token
load_dotenv()

API_URL = "https://router.huggingface.co/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {os.getenv('HF_TOKEN')}",
    "Content-Type": "application/json"
}

# User se topic lena
topic = input("Enter your topic: ")

# AI ko instruction bhejna
payload = {
    "model": "meta-llama/Llama3.1-8B-Instruct",
    "messages": [
        {
            "role": "user",
            "content": f"""
            Generate 5 flashcards about {topic}.
            Each flashcard should contain:
            Question:
            Answer:
            Keep answers short and easy.
            """
        }
    ],
    "max_tokens": 700
}

# API Call
print("\nGenerating Flashcards...")

response = requests.post(
    API_URL,
    headers=headers,
    json=payload,
    timeout=60
)

# Result
if response.status_code == 200:

    result = response.json()

    answer = result["choices"][0]["message"]["content"]

    print("\n===== YOUR AI FLASHCARDS =====\n")
    print(answer)

else:
    print("API Error:", response.status_code)
    print(response.text)