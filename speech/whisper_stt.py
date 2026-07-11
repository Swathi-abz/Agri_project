import whisper

model = whisper.load_model("base")


def whisper_speech_to_text(audio_path):

    print("Whisper processing...")

    result = model.transcribe(audio_path)

    print("Whisper Success")

    return result["text"]