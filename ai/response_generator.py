from ai.knowledge_base import search_crop, search_disease


def generate_response(crop, intent, english_text):

    if intent == "crop_advisory":

        crop_data = search_crop(crop)

        if crop_data:
            return f"""
🌱 Crop: {crop_data['crop'].title()}

📅 Season: {crop_data['season']}

🌍 Soil: {crop_data['soil']}

🌿 Fertilizer: {crop_data['fertilizer']}

💧 Water Requirement: {crop_data['water']}
"""
        else:
            return "Sorry, crop information not found."

    elif intent == "crop_disease":

        disease = search_disease(crop, english_text)

        if disease:
            return f"""
🌱 Crop: {disease['crop'].title()}

🦠 Disease: {disease['disease']}

⚠ Symptoms:
{disease['symptoms']}

✅ Solution:
{disease['solution']}
"""
        else:
            return "Sorry, disease information not found."

    return "Sorry, I couldn't understand your request."