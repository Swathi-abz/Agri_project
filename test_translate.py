from ai.translator import translate_text

result = translate_text(
    "ನನ್ನ ಟೊಮೇಟೊ ಬೆಳೆಗೆ ಯಾವ ಗೊಬ್ಬರ ಹಾಕಬೇಕು?",
    "kn-IN",
    "en-IN"
)

print(result)