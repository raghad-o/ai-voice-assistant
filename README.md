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

## Project Structure
