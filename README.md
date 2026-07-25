# Voice AI Assistant

A Voice-to-Voice AI Assistant that enables natural spoken interaction with AI, supporting both Arabic and English languages. The project combines Speech-to-Text (STT), Large Language Models (LLM), and Text-to-Speech technologies to create an interactive assistant suitable for applications such as smart assistants, accessibility tools, customer support systems, educational platforms, and hands-free AI interactions.

## Project Overview

This project implements a complete voice-based AI pipeline:

1. **Speech-to-Text (STT):** Converts the user's voice input into text using RealtimeSTT with the Faster-Whisper model.
2. **AI Processing:** Sends the recognized text to Cohere LLM to generate an intelligent response.
3. **Text-to-Speech (TTS):** Converts the AI response back into speech using Piper TTS.

The assistant supports Arabic and English conversations and provides a flexible structure that can be customized depending on the intended use case.

## Features

- Voice interaction with an AI assistant.
- Arabic and English language support.
- Speech recognition using Faster-Whisper.
- AI response generation using Cohere LLM.
- Natural voice output using Piper TTS.
- Optional exit command: the assistant can stop when a specific farewell phrase is detected.
- The assistant can also be modified to run continuously depending on the required application.

## Demonstration

The following videos demonstrate the assistant working in both supported languages:

- English Voice Assistant Simulation

- Arabic Voice Assistant Simulation

## Technologies Used

- Python
- RealtimeSTT
- Faster-Whisper
- Cohere LLM
- Piper TTS
- PyAudio
- SoundDevice
- Python-dotenv

## Installation and Setup

1. Clone the repository:

```bash
git clone https://github.com/raghad-o/ai-voice-assistant.git
cd ai-voice-assistant
```

2. Create and activate the virtual environment:

```bash
python -m venv venv
venv\Scripts\activate
```

3. Install the required libraries:

```bash
pip install -r requirements.txt
```

4. Create a `models` folder in the project directory, then download the required voice models:

```bash
python -m piper.download_voices ar_JO-kareem-medium --data-dir models
python -m piper.download_voices en_US-ryan-medium --data-dir models
```

5. Create a `.env` file and add your Cohere API key using the `COHERE_API_KEY` environment variable.

6. Run the assistant:

```bash
python main.py
```
## Project Structure

- `main.py`: The main entry point that runs the voice assistant.

- `speech_to_text.py`: Handles voice input and converts speech into text.

- `llm.py`: Manages communication with Cohere LLM to generate AI responses.

- `text_to_speech.py`: Converts generated responses into spoken audio using Piper TTS.

- `models/`: Stores the downloaded Piper voice models.

- `.env`: Stores required environment variables such as the Cohere API key.

- `requirements.txt`: Contains the project dependencies.

- `README_Videos/`: Contains Arabic and English demonstration videos.
