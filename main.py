from core.ai_engine import AIEngine

ai = AIEngine()

while True:
    question = input("You: ")

    if question.lower() == "exit":
        break

    answer = ai.ask(question)

    print("\nBrother:", answer)