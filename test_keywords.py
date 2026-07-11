from ai.keyword_extractor import extract_keywords

question = "My tomato plant leaves are turning yellow due to fungus."

keywords = extract_keywords(question)

print("Question:")
print(question)

print("\nKeywords:")
print(keywords)