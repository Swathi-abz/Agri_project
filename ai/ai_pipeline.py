# ai/ai_pipeline.py

import os
from dotenv import load_dotenv
from openai import OpenAI

from language.detect_language import detect_language
from language.translate import translate_text

from ai.intent_classifier import classify_intent
from ai.named_entity import extract_agri_entities
from ai.knowledge_base import search_knowledge_base
from ai.session_manager import get_session, update_session

# ---------------------------------
# Load Environment Variables
# ---------------------------------

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

if os.getenv("OPENAI_API_KEY"):
    print("✓ OpenAI API loaded")
else:
    print("✗ OpenAI API not found")


# ---------------------------------
# AI Query Processing
# ---------------------------------

def process_query(question):

    original_question = question

    # ---------------------------------
    # Detect Language
    # ---------------------------------

    language = detect_language(question)

    print("Detected Language:", language)

    # ---------------------------------
    # Translate to English
    # ---------------------------------

    if language != "en":

        question = translate_text(
            question,
            language,
            "en"
        )

        print("Translated Question:", question)

    # ---------------------------------
    # Intent Classification
    # ---------------------------------

    intent = classify_intent(question)

    print("Intent:", intent)

    # ---------------------------------
    # Named Entity Recognition
    # ---------------------------------

    entities = extract_agri_entities(question)

    print("Entities:", entities)

    # ---------------------------------
    # Session Memory
    # ---------------------------------

    session = get_session()

    print("Previous Session:", session)

    if entities["crop"] is None:

        previous_crop = session.get("crop")

        if previous_crop:

            entities["crop"] = previous_crop

            print("Using Previous Crop:", previous_crop)

    # ---------------------------------
    # Knowledge Base
    # ---------------------------------

    answer = search_knowledge_base(
        question,
        intent,
        entities
    )

    if answer:

        print("Answer From Knowledge Base")

    # ---------------------------------
    # OpenAI Fallback
    # ---------------------------------

    if answer is None:

        print("Using OpenAI")

        prompt = f"""
You are an AI Agricultural Assistant.

Farmer Question:
{question}

Intent:
{intent}

Agricultural Entities:
{entities}

Give practical agricultural advice.
Use simple language.
"""

        response = client.chat.completions.create(

            model="gpt-4.1-mini",

            messages=[
                {
                    "role": "system",
                    "content": "You are an AI Agricultural Assistant."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]

        )

        answer = response.choices[0].message.content

    # ---------------------------------
    # Translate Back
    # ---------------------------------

    if language != "en":

        answer = translate_text(
            answer,
            "en",
            language
        )

    # ---------------------------------
    # Update Session
    # ---------------------------------

    update_session(

        language=language,

        crop=entities.get("crop"),

        intent=intent,

        user=original_question,

        bot=answer

    )

    print("Session Updated Successfully")

    return {
    "language": language,
    "translated_question": question,
    "intent": intent,
    "entities": entities,
    "response": answer
}