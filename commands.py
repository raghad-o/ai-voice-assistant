EXIT_COMMANDS = [
    "bye",
    "goodbye",
    "see you",
    "see you later",
    "exit",
    "quit",
    "وداعا",
    "وداعًا",
    "مع السلامة",
    "الى اللقاء",
    "إلى اللقاء",
]

def is_exit_command(text):

    text = text.lower().strip()

    return any(command in text for command in EXIT_COMMANDS)