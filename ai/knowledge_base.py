import json
import os


# Get project main folder path
BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)


# Database file location
KNOWLEDGE_FILE = os.path.join(
    BASE_DIR,
    "database",
    "agri_knowledge.json"
)

# Load agriculture knowledge data
def load_knowledge():

    try:

        with open(KNOWLEDGE_FILE, "r", encoding="utf-8") as file:

            return json.load(file)


    except FileNotFoundError:

        print("Knowledge base file not found")

        return []


    except Exception as e:

        print("Error loading knowledge base:", e)

        return []



# Load data
knowledge_data = load_knowledge()



def search_knowledge_base(question, intent, entities):

    """
    Search agriculture knowledge base.

    Parameters:
        question : farmer question
        intent   : classified intent
        entities : crop, disease, fertilizer details

    Returns:
        Answer if found otherwise None
    """

    question = question.lower()


    crop = entities.get("crop")
    disease = entities.get("disease")
    fertilizer = entities.get("fertilizer")



    for item in knowledge_data:


        item_crop = item.get("crop", "").lower()

        item_disease = item.get("disease", "").lower()

        item_fertilizer = item.get("fertilizer", "").lower()



        # Crop + Disease matching
        if crop and disease:

            if (
                crop.lower() == item_crop
                and disease.lower() == item_disease
            ):

                return item.get("solution")



        # Crop + Fertilizer matching
        if crop and fertilizer:

            if (
                crop.lower() == item_crop
                and fertilizer.lower() == item_fertilizer
            ):

                return item.get("solution")



        # Only Crop matching
        if crop:

            if crop.lower() == item_crop:

                return item.get("solution")



        # Keyword search fallback
        keywords = item.get("keywords", [])

        for keyword in keywords:

            if keyword.lower() in question:

                return item.get("solution")



    # No answer found
    return None