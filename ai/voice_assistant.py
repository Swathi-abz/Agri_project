from ai.sarvam_api import client

def speech_to_text(audio_path):
    with open(audio_path, "rb") as audio_file:
        response = client.speech_to_text.transcribe(
            file=audio_file,
            model="saaras:v3",
            mode="transcribe"
        )

    print(response)
    return response.transcript