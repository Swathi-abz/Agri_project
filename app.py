from dotenv import load_dotenv
import os

from flask import Flask, render_template, request, jsonify

from ai.ai_pipeline import process_query
from speech.speech_to_text import sarvam_stt
from speech.text_to_speech import text_to_speech

load_dotenv()

app = Flask(__name__)


# ==========================
# Check API Keys
# ==========================

if os.getenv("OPENAI_API_KEY"):
    print("✓ OpenAI API loaded")
else:
    print("✗ OpenAI API not found")


if os.getenv("SARVAM_API_KEY"):
    print("✓ Sarvam API loaded")
else:
    print("✗ Sarvam API not found")



# ==========================
# Home Page
# ==========================

@app.route("/")
def home():

    print("🌐 Home page opened")

    return render_template("index.html")



# ==========================
# Text Query
# ==========================

@app.route("/ask", methods=["POST"])
def ask():

    try:

        print("\n" + "=" * 60)
        print("🌾 NEW TEXT QUERY")
        print("=" * 60)


        data = request.get_json()

        print("Received Data:")
        print(data)


        question = data.get("question", "").strip()


        print("\nUser Question:")
        print(question)



        if question == "":

            print("❌ Empty question")

            return jsonify({
                "error": "Please enter a question."
            })



        print("\n🤖 Processing with AI Pipeline...")


        result = process_query(question)



        print("\n✅ AI Response Generated")


        print("\nLanguage:")
        print(result.get("language"))


        print("\nIntent:")
        print(result.get("intent"))


        print("\nEntities:")
        print(result.get("entities"))


        print("\nResponse:")
        print(result.get("response"))



        print("\n🔊 Generating Audio...")


        audio_path = text_to_speech(
            result["response"],
            result["language"]
        )


        print("Audio File:")
        print(audio_path)



        result["audio"] = audio_path



        print("\n✅ TEXT REQUEST COMPLETED")

        print("=" * 60)


        return jsonify(result)



    except Exception as e:


        print("\n❌ ASK ERROR:")
        print(e)


        return jsonify({
            "error": str(e)
        }), 500





# ==========================
# Voice Query
# ==========================

@app.route("/voice", methods=["POST"])
def voice():

    try:


        print("\n" + "=" * 60)
        print("🎤 NEW VOICE QUERY")
        print("=" * 60)



        if "audio" not in request.files:


            return jsonify({
                "error": "No audio uploaded."
            })



        audio = request.files["audio"]


        path = "static/input.webm"


        audio.save(path)



        print("✅ Audio saved:")
        print(path)



        print("\n📝 Speech To Text Processing...")


        text = sarvam_stt(path)



        print("\nRecognized Text:")
        print(text)



        if text is None or text.strip() == "":


            return jsonify({
                "error": "Speech not recognized."
            })



        print("\n🤖 Sending Voice Text to AI...")


        result = process_query(text)



        print("\nAI Response:")
        print(result.get("response"))




        print("\n🔊 Generating Speech...")


        audio_path = text_to_speech(
            result["response"],
            result["language"]
        )



        print("Audio File:")
        print(audio_path)



        result["audio"] = audio_path

        result["text"] = text



        print("\n✅ VOICE REQUEST COMPLETED")

        print("=" * 60)



        return jsonify(result)



    except Exception as e:


        print("\n❌ VOICE ERROR:")
        print(e)



        return jsonify({
            "error": str(e)
        }), 500





# ==========================
# Run Application
# ==========================

if __name__ == "__main__":


    print("\n🚀 Starting AgriAI Server...")


    app.run(
        debug=True
    )