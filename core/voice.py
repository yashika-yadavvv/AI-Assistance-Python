# ============================================
# JARVIS — VOICE (Listen + Speak)
# ============================================

import pyttsx3
import speech_recognition as sr
from config import VOICE_RATE, VOICE_VOLUME, ASSISTANT_NAME, USER_NAME

# ---- SPEAK ----
engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', VOICE_RATE)
engine.setProperty('volume', VOICE_VOLUME)

def Speak(text):
    if len(str(text)) == 0:
        return
    print(f"\n🤖 {ASSISTANT_NAME} : {text}\n")
    engine.say(text)
    engine.runAndWait()

# ---- LISTEN ----
def Listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(f"\n🎤 Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 6)
    try:
        print("⏳ Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"\n👤 {USER_NAME} : {query}\n")
        return query.lower()
    except:
        return ""