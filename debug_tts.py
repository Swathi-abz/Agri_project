from ai.sarvam_api import client

print("Creating request...")

response = client.text_to_speech.convert(
    text="Hello",
    target_language_code="en-IN",
    speaker="anushka",
    model="bulbul:v2"
)

print("Type:", type(response))
print("Dir:", dir(response))
print("Response:", response)