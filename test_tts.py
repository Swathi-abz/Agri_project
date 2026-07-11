from ai.tts import text_to_speech

print("Starting TTS test...")

path = text_to_speech(
    "ನಿಮ್ಮ ಭತ್ತದ ಬೆಳೆಗೆ ಯೂರಿಯಾ ಗೊಬ್ಬರವನ್ನು ಬಳಸಬಹುದು."
)

print("Returned:", path)
print("Finished.")