import subprocess
import sys
import os
import sounddevice as sd
import soundfile as sf
import numpy as np


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

AR_MODEL = os.path.join(BASE_DIR, "models", "ar_JO-kareem-medium.onnx")
EN_MODEL = os.path.join(BASE_DIR, "models", "en_US-ryan-medium.onnx")


def speak(text):

    if any("\u0600" <= char <= "\u06FF" for char in text):
        model = AR_MODEL
    else:
        model = EN_MODEL

    output = os.path.join(BASE_DIR, "outputs", "response.wav")
    os.makedirs("outputs", exist_ok=True)

    subprocess.run(
        [
            sys.executable,
            "-m",
            "piper",
            "--model",
            model,
            "--output_file",
            output
        ],
        input=text,
        text=True
    )

    data, samplerate = sf.read(output)

    #silence to prevent audio cutoff
    silence = np.zeros(int(samplerate * 0.3))
    data = np.concatenate([data, silence])

    sd.play(data, samplerate)
    sd.wait() 


if __name__ == "__main__":

    speak("السلام عليكم، أنا مساعدك .")
    speak("Hello, I am your AI assistant.")