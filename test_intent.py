from ai.intent_classifier import classify_intent

text = "Which fertilizer is best for tomato?"

intent = classify_intent(text)

print(intent)