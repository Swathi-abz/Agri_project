
from langdetect import detect


def detect_language(text):

    lang = detect(text)

    mapping = {
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

    return mapping.get(lang, "en-IN")