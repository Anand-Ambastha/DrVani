
# 🩺 Dr. Vani – Your AI-Powered Virtual Doctor

**Dr. Vani** is a voice-enabled, AI-powered virtual doctor that listens to your symptoms, analyzes medical images (like skin conditions), and replies with lifelike voice feedback. It uses **GROQ APIs** for transcription and image understanding, and **ElevenLabs** for realistic speech synthesis. Built with a Gradio interface, Dr. Vani offers a seamless and interactive health query simulation experience.

---

## 🔧 Features

- 🎙️ **Voice Input**: Speak naturally through your mic.
- 🧠 **Speech-to-Text**: Transcribes your speech using GROQ Whisper (`whisper-large-v3`).
- 🖼️ **Image Diagnosis**: Analyzes uploaded medical images via GROQ's Vision LLaMA model.
- 🗣️ **Voice Output**: Responds in lifelike speech using ElevenLabs (voice: Aria).
- 🌐 **Web UI**: Powered by Gradio for intuitive interaction.
- 👨‍⚕️ **Doctor-Style Prompting**: Mimics real doctors—no AI lingo, just human responses.

---

## 🧠 Tech Stack

| Component     | Tool / API                  |
|---------------|-----------------------------|
| UI            | Gradio                      |
| STT           | GROQ Whisper (whisper-large-v3) |
| Vision LLM    | GROQ LLaMA-4 / LLaMA-3 Vision |
| TTS           | ElevenLabs (eleven_turbo_v2) |
| Voice Input   | PyAudio, SpeechRecognition  |
| Audio Tools   | ffmpeg, portaudio           |
| Alt. TTS      | gTTS (fallback only)        |
| Language      | Python 3.9+                 |

---

## 📁 Folder Structure

.
├── gradio_app.py # Main Gradio interface logic
├── drbrain.py # Handles image + text inference using GROQ
├── doctorvoice.py # TTS response using ElevenLabs or gTTS
├── patientvoice.py # Audio recording and speech transcription
├── .env # Stores API keys securely



## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/drvani.git
cd drvani
2. Install Python Dependencies
bash
pip install -r requirements.txt
⚠️ You must have both ffmpeg and portaudio installed on your system.

Install ffmpeg
Windows: Download here and add to PATH

Mac: brew install ffmpeg

Linux: sudo apt install ffmpeg

Install portaudio
Windows: Usually installed with pyaudio wheel

Mac: brew install portaudio

Linux: sudo apt install portaudio19-dev

🗝️ Environment Setup
Create a .env file in the root directory:

GROQ_API_KEY=your_groq_api_key_here
ELEVENLABS_API_KEY=your_elevenlabs_api_key_here
🚀 Running the App
bash

python gradio_app.py
Open your browser and go to: http://127.0.0.1:7860

📷 Workflow
🎤 Speak your health-related question

🖼️ Upload an image (e.g., rash, acne, etc.)

🧠 AI analyzes your input

🩺 Doctor Vani replies with voice + text

🧪 Customization Ideas
🔄 Replace ElevenLabs with offline TTS

🌍 Add multilingual support

💾 Store conversation logs

📱 Convert to mobile/web app for telemedicine

📜 Disclaimer
For educational use only. This project does not provide actual medical advice. Always consult a licensed medical professional for real-world health concerns.

🙌 Acknowledgements
GROQ – Fast LLM and Vision model serving

ElevenLabs – Human-like voice generation

Gradio – Easy UI for ML apps

Google TTS – Fallback voice support
