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

    payload = {
        "inputs": [text],
        "target_language_code": language,
        "speaker": "anushka",
        "model": "bulbul:v2"
    }

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

        output_file = "static/output.wav"

        with open(output_file, "wb") as f:
            f.write(audio_bytes)

        print("Audio saved:", output_file)

        return output_file

    except Exception as e:

        print("TTS Exception:", e)

        return None