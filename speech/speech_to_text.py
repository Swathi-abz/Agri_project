import os
import requests
from dotenv import load_dotenv

from speech.whisper_fallback import whisper_transcribe

load_dotenv()

SARVAM_API_KEY = os.getenv("SARVAM_API_KEY")


def sarvam_stt(audio_file):

    try:

        print("Trying Sarvam Speech-to-Text...")

        url = "https://api.sarvam.ai/speech-to-text"

        headers = {
            "api-subscription-key": SARVAM_API_KEY
        }

        # Detect file type automatically
        extension = os.path.splitext(audio_file)[1].lower()

        if extension == ".webm":
            mime = "audio/webm"
            filename = "audio.webm"

        elif extension == ".wav":
            mime = "audio/wav"
            filename = "audio.wav"

        elif extension == ".mp3":
            mime = "audio/mpeg"
            filename = "audio.mp3"

        else:
            mime = "application/octet-stream"
            filename = "audio"

        with open(audio_file, "rb") as audio:

            files = {
                "file": (
                    filename,
                    audio,
                    mime
                )
            }

            response = requests.post(
                url,
                headers=headers,
                files=files,
                timeout=30
            )

        print("Sarvam Status:", response.status_code)

        data = response.json()

        print("Sarvam Response:", data)

        if response.status_code == 200 and "transcript" in data:

            text = data["transcript"]

            print("Sarvam Success")

            print("Recognized Text:", text)

            return text

        print("Sarvam Failed")

        print("Using Whisper Fallback")

        return whisper_transcribe(audio_file)

    except Exception as e:

        print("Sarvam Exception:", e)

        print("Using Whisper Fallback")

        return whisper_transcribe(audio_file)