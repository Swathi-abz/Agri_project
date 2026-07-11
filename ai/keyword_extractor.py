import spacy

# Load English NLP model
nlp = spacy.load("en_core_web_sm")

def extract_keywords(text):
    """
    Extract important agricultural keywords.
    """

    doc = nlp(text)

    keywords = []

    for token in doc:
        # Ignore stop words and punctuation
        if token.is_stop or token.is_punct:
            continue

        # Keep useful words
        if token.pos_ in ["NOUN", "PROPN", "ADJ"]:
            keywords.append(token.text.lower())

    return keywords