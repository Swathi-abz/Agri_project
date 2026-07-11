import os
import requests
from dotenv import load_dotenv

load_dotenv()

SARVAM_API_KEY = os.getenv("SARVAM_API_KEY")


def translate_text(text, source_lang, target_lang):

    # Convert language codes to Sarvam-supported format
    lang_map = {
        "en": "en-IN",
        "hi": "hi-IN",
        "kn": "kn-IN",
        "ta": "ta-IN",
        "te": "te-IN",
        "ml": "ml-IN",
        "mr": "mr-IN",
        "gu": "gu-IN",
        "bn": "bn-IN",
        "pa": "pa-IN",
        "or": "od-IN",
        "ur": "ur-IN"
    }

    source_lang = lang_map.get(source_lang, source_lang)
    target_lang = lang_map.get(target_lang, target_lang)

    # No translation needed
    if source_lang == target_lang:
        return text

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

    try:

        response = requests.post(
            url,
            headers=headers,
            json=payload,
            timeout=30
        )

        if response.status_code == 200:

            result = response.json()

            # Different API versions may return different keys
            if "translated_text" in result:
                return result["translated_text"]

            if "translation" in result:
                return result["translation"]

            if "translations" in result:
                return result["translations"][0]

            return text

        else:

            print("Translation Failed:", response.json())

            return text

    except Exception as e:

        print("Translation Exception:", e)

        return text