from RealtimeSTT import AudioToTextRecorder

recorder = None


def initialize_recorder():
    global recorder

    print("Preparing assistant...")

    recorder = AudioToTextRecorder(
        model="base", 
        compute_type="float32", 
        initial_prompt="Arabic and English speech."
    )

    print("Assistant is ready!")

def listen():
    print("\nListening...")
    text = recorder.text()

    return text

def shutdown_recorder():
    global recorder

    if recorder:
        recorder.shutdown()
        recorder = None

if __name__ == "__main__":
    initialize_recorder()

    while True:
        result = listen()

        print("You said:")
        print(repr(result))