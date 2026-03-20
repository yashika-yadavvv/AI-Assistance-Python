🤖 AI Jarvis Assistant
A voice-controlled AI desktop assistant built with Python — originally developed as my Diploma final year project (2022-23), now updated with modern AI integration.
📌 About
This was my Diploma Final Year Project — my first real attempt at building something intelligent. At the time, I had just started learning Python and wanted to build something that felt like actual AI.
Two years later, I've revisited and upgraded it with:
🧠 LLM Integration (Groq API — Llama 3)
🪟 Floating UI built with PyQt5
💾 Memory System using SQLite
⚡ Faster voice using pyttsx3
✨ Features
Feature
Description
🎤 Wake Word
Say "Jarvis" to activate
🗣️ Voice Commands
Natural language input
🤖 AI Brain
Powered by Groq LLM
💾 Memory
Remembers past conversations
🪟 Floating UI
Always-on-top animated card
⚙️ System Control
Open apps, search, YouTube
📸 Screenshot
Voice triggered
🛠️ Tech Stack
Python 3.11
PyQt5 — Floating UI
SpeechRecognition — Voice input
pyttsx3 — Text to speech
Groq API — LLM (Llama 3)
SQLite — Memory storage
📁 Project Structure
AI-Assistance-Python/
├── core/
│   ├── brain.py       # LLM logic
│   ├── voice.py       # Listen + Speak
│   ├── memory.py      # SQLite memory
│   └── executor.py    # Command handler
├── ui/
│   └── floating.py    # PyQt5 UI
├── skills/
│   ├── system.py      # System commands
│   ├── web.py         # Web search
│   └── files.py       # File handling
├── data/
│   └── memory.db      # Conversation history
├── config.py
└── main.py
🚀 How to Run
# Install dependencies
pip install pyqt5 speechrecognition pyttsx3 groq pyaudio psutil

# Add your Groq API key in config.py
OPENAI_API_KEY = "your-groq-api-key"

# Run
python main.py
🎯 Voice Commands
"Jarvis" → Wake up
"What time is it?" → Current time
"Open Chrome" → Opens Chrome
"Search machine learning" → Google search
"YouTube lofi music" → YouTube search
"Take a screenshot" → Screenshots
"Bye" → Exit
👩‍💻 About This Project
This project holds a special place — it was built during my Diploma in Computer Science as a final year project. Back then, voice assistants felt like magic to me.
Now as a CSE student diving deeper into AI, I rebuilt it from scratch with proper architecture, LLM integration, and a floating UI.
Still growing. Still learning. 🚀
Made with ❤️ by Yashika Yadav
