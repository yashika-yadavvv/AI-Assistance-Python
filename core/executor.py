# ============================================
# JARVIS — EXECUTOR (Commands)
# ============================================

import os
import subprocess
import webbrowser
import datetime
from core.voice import Speak
from core.brain import ask_jarvis

def execute(query):

    # ---- TIME ----
    if "time" in query:
        time = datetime.datetime.now().strftime("%I:%M %p")
        Speak(f"Current time is {time}")

    # ---- DATE ----
    elif "date" in query:
        date = datetime.datetime.now().strftime("%B %d, %Y")
        Speak(f"Today is {date}")

    # ---- OPEN APPS ----
    elif "open chrome" in query:
        Speak("Opening Chrome")
        os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

    elif "open vs code" in query:
        Speak("Opening VS Code")
        os.startfile("C:\\Users\\Hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")

    elif "open notepad" in query:
        Speak("Opening Notepad")
        os.startfile("notepad.exe")

    elif "open calculator" in query:
        Speak("Opening Calculator")
        os.startfile("calc.exe")

    # ---- GOOGLE SEARCH ----
    elif "search" in query:
        query = query.replace("search", "").strip()
        Speak(f"Searching for {query}")
        webbrowser.open(f"https://www.google.com/search?q={query}")

    # ---- YOUTUBE ----
    elif "youtube" in query:
        query = query.replace("youtube", "").replace("play", "").strip()
        Speak(f"Playing {query} on YouTube")
        webbrowser.open(f"https://www.youtube.com/results?search_query={query}")

    # ---- SHUTDOWN ----
    elif "shutdown" in query:
        Speak("Shutting down the system")
        os.system("shutdown /s /t 5")

    # ---- RESTART ----
    elif "restart" in query:
        Speak("Restarting the system")
        os.system("shutdown /r /t 5")

    # ---- BYE ----
    elif "bye" in query or "exit" in query or "quit" in query:
        Speak("Goodbye Yashika! Have a great day!")
        return False

    # ---- AI BRAIN (default) ----
    else:
        response = ask_jarvis(query)
        Speak(response)

    return True