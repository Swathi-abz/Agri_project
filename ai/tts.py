from ai.sarvam_api import client
import base64
import os

def text_to_speech(text):
    response = client.text_to_speech.convert(
        text=text,
        target_language_code="kn-IN",
        speaker="anushka",
        model="bulbul:v2"
    )

    audio_data = base64.b64decode(response.audios[0])

    os.makedirs("static", exist_ok=True)

    output_file = "static/output.wav"

    with open(output_file, "wb") as f:
        f.write(audio_data)

    print("Audio saved to:", output_file)

    return output_file