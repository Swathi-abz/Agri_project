import whisper


# Load Whisper model
model = whisper.load_model("base")



def whisper_transcribe(audio_file):

    try:

        print("Using Whisper fallback...")


        result = model.transcribe(
            audio_file
        )


        text = result["text"]


        print(
            "Whisper Text:",
            text
        )


        return text



    except Exception as e:

        print(
            "Whisper Error:",
            e
        )

        return None