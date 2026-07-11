from ai.ai_pipeline import process_query

question = "My tomato leaves are turning yellow."

result = process_query(question)

print("Language :", result["language"])
print("Intent   :", result["intent"])
print("Keywords :", result["keywords"])

print("\nResponse:")
print(result["response"])