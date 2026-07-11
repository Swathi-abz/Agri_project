from ai.language_detector import detect_language

english = "My tomato plant leaves are turning yellow."
kannada = "ನನ್ನ ಟೊಮೇಟೊ ಗಿಡದ ಎಲೆಗಳು ಹಳದಿಯಾಗುತ್ತಿವೆ."
telugu = "నా టమాటా మొక్క ఆకులు పసుపుగా మారుతున్నాయి."
hindi = "मेरे टमाटर के पौधे की पत्तियां पीली हो रही हैं।"

print("English :", detect_language(english))
print("Kannada :", detect_language(kannada))
print("Telugu  :", detect_language(telugu))
print("Hindi   :", detect_language(hindi))