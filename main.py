import re
from speech_to_text import listen, initialize_recorder, shutdown_recorder
from llm import ask_llm
from text_to_speech import speak
from commands import is_exit_command

EXIT_ON_FAREWELL = True

def clean_text(text):
    text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)
    text = text.replace("*", "")
    return text

def main():

    initialize_recorder()

    conversation = []

    while True:

        user_text = listen()

        if not user_text:
            continue

        print("You:", user_text)


        conversation.append({
            "role": "user",
            "content": user_text
        })

        response = ask_llm(conversation)
        response = clean_text(response)

        conversation.append({
            "role": "assistant",
            "content": response
        })

        print("\nAssistant:", response)


        speak(response)

        if is_exit_command(user_text):

            if EXIT_ON_FAREWELL:
                shutdown_recorder()
                return

            else:
                continue

if __name__ == "__main__":
    main()