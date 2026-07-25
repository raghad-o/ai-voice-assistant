import os
from dotenv import load_dotenv
import cohere

load_dotenv()

api_key = os.getenv("COHERE_API_KEY")

co = cohere.Client(api_key)

def ask_llm(conversation):

    chat_history = []

    for message in conversation[:-1]:
        chat_history.append({
            "role": "USER" if message["role"] == "user" else "CHATBOT",
            "message": message["content"]
        })

    response = co.chat(
        model="command-r7b-arabic-02-2025",
        chat_history=chat_history,
        message=conversation[-1]["content"]
    )

    return response.text


if __name__ == "__main__":

    conversation = []

    while True:

        user_input = input("\nYou: ")

        conversation.append({
            "role": "user",
            "content": user_input
        })

        answer = ask_llm(conversation)

        print("\nAssistant:", answer)


        conversation.append({
            "role": "assistant",
            "content": answer
        })
