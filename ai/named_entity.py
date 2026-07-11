import json
import os


# ----------------------------
# Load Agriculture Entities
# ----------------------------

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)


ENTITY_FILE = os.path.join(
    BASE_DIR,
    "database",
    "agri_entities.json"
)



def load_entities():

    try:

        with open(
            ENTITY_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)


    except Exception as e:

        print(
            "Entity file loading error:",
            e
        )

        return {}



agri_entities = load_entities()



# ----------------------------
# Symptom Based Disease Mapping
# ----------------------------

disease_patterns = {


    "early blight": [

        "brown spots",
        "dark spots",
        "leaf spots",
        "brown patches",
        "yellow leaves",
        "leaves turning yellow"

    ],


    "late blight": [

        "black spots",
        "water soaked spots",
        "dark lesions",
        "rotting leaves"

    ],


    "powdery mildew": [

        "white powder",
        "white patches",
        "powder on leaves"

    ],


    "leaf curl virus": [

        "leaf curling",
        "curled leaves",
        "leaves curling",
        "twisted leaves"

    ],


    "bacterial wilt": [

        "plant wilting",
        "sudden drying",
        "drooping leaves"

    ]

}



# ----------------------------
# Extract Agricultural Entities
# ----------------------------

def extract_agri_entities(text):


    text = text.lower()



    entities = {

        "crop": None,

        "disease": None,

        "fertilizer": None

    }



    # ----------------------------
    # Crop Detection
    # ----------------------------

    crops = agri_entities.get(
        "crops",
        []
    )


    for crop in crops:

        if crop.lower() in text:

            entities["crop"] = crop

            break



    # ----------------------------
    # Disease Name Detection
    # ----------------------------

    diseases = agri_entities.get(
        "diseases",
        []
    )


    for disease in diseases:

        if disease.lower() in text:

            entities["disease"] = disease

            break



    # ----------------------------
    # Symptom Based Disease Detection
    # ----------------------------

    if entities["disease"] is None:


        for disease, symptoms in disease_patterns.items():


            for symptom in symptoms:


                if symptom in text:

                    entities["disease"] = disease

                    break


            if entities["disease"]:

                break



    # ----------------------------
    # Fertilizer Detection
    # ----------------------------

    fertilizers = agri_entities.get(
        "fertilizers",
        []
    )


    for fertilizer in fertilizers:


        if fertilizer.lower() in text:

            entities["fertilizer"] = fertilizer

            break



    return entities