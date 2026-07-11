# speech/text_to_speech.py

import os
import base64
import requests
from dotenv import load_dotenv

load_dotenv()

SARVAM_API_KEY = os.getenv("SARVAM_API_KEY")


def text_to_speech(text, language="en-IN"):

    print("Generating speech...")

    url = "https://api.sarvam.ai/text-to-speech"

    headers = {
        "api-subscription-key": SARVAM_API_KEY,
        "Content-Type": "application/json"
    }

    # Supported Sarvam language codes
    supported_languages = [
        "en-IN",
        "hi-IN",
        "kn-IN",
        "ta-IN",
        "te-IN",
        "ml-IN",
        "mr-IN",
        "gu-IN"
    ]

    if language not in supported_languages:
        language = "en-IN"

    payload = {
        "inputs": [text],
        "target_language_code": language,
        "speaker": "anushka",
        "model": "bulbul:v2"
    }

    print("TTS LANGUAGE :", language)
    print("TTS MODEL    :", payload["model"])
    print("TTS SPEAKER  :", payload["speaker"])

    try:

        response = requests.post(
            url,
            headers=headers,
            json=payload,
            timeout=30
        )

        data = response.json()

        if response.status_code != 200:
            print("TTS Error:", data)
            return None

        audio_base64 = data["audios"][0]

        audio_bytes = base64.b64decode(audio_base64)

        output_path = "static/output.wav"

        with open(output_path, "wb") as f:
            f.write(audio_bytes)

        print("Audio saved:", output_path)

        return output_path

    except Exception as e:

        print("TTS Exception:", e)

        return None