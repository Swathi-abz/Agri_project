# ai/intent_classifier.py


# ----------------------------
# Intent Keywords
# ----------------------------

intent_patterns = {


    "disease_detection": [

        "disease",
        "spots",
        "brown spots",
        "black spots",
        "yellow leaves",
        "leaf",
        "infection",
        "pest",
        "fungus",
        "fungal"

    ],



    "fertilizer_recommendation": [

        "fertilizer",
        "urea",
        "npk",
        "dap",
        "potash",
        "nutrient",
        "manure"

    ],



    "irrigation_advice": [

        "water",
        "watering",
        "irrigation",
        "moisture"

    ],



    "weather_query": [

        "weather",
        "rain",
        "temperature",
        "climate",
        "forecast"

    ],



    "market_price": [

        "price",
        "market",
        "sell",
        "rate",
        "cost"

    ],



    "government_scheme": [

        "scheme",
        "subsidy",
        "government",
        "loan",
        "benefit"

    ],



    "crop_advice": [

        "crop",
        "grow",
        "cultivation",
        "planting",
        "farming"

    ]

}





# ----------------------------
# Intent Classification Function
# ----------------------------

def classify_intent(question):


    question = question.lower()



    scores = {}



    for intent, keywords in intent_patterns.items():

        score = 0


        for keyword in keywords:

            if keyword in question:

                score += 1



        scores[intent] = score



    # Find best matching intent

    best_intent = max(
        scores,
        key=scores.get
    )



    # If no keyword matched

    if scores[best_intent] == 0:

        return "general_agriculture"



    return best_intent