import os
import requests
from dotenv import load_dotenv

load_dotenv()

SARVAM_API_KEY = os.getenv("SARVAM_API_KEY")


def translate_text(text, source_lang, target_lang):

    url = "https://api.sarvam.ai/translate"

    headers = {
        "api-subscription-key": SARVAM_API_KEY,
        "Content-Type": "application/json"
    }

    payload = {
        "input": text,
        "source_language_code": source_lang,
        "target_language_code": target_lang
    }

    response = requests.post(
        url,
        headers=headers,
        json=payload
    )

    if response.status_code == 200:
        return response.json()["translated_text"]

    print(response.text)
    return text