# ============================================
# JARVIS — MAIN FILE
# ============================================

import sys
import threading
from PyQt5.QtWidgets import QApplication
from ui.floating import FloatingUI
from core.voice import Speak, Listen
from core.executor import execute
from core.memory import init_db
from config import WAKE_WORD, ASSISTANT_NAME

init_db()

def jarvis_loop(ui):
    Speak(f"Hello Yashika! Say {WAKE_WORD} to wake me up!")
    ui.signals.update_status.emit("🤖 Say 'Jarvis'...")
    ui.signals.update_color.emit("#22c55e")
    ui.signals.update_subtitle.emit("")

    while True:
        query = Listen()

        if WAKE_WORD in query:
            Speak("Yes Yashika, I am listening!")
            ui.signals.update_status.emit("🎤 Listening...")
            ui.signals.update_color.emit("#3b82f6")
            ui.signals.update_subtitle.emit("Jarvis is listening...")

            command = Listen()

            if command:
                ui.signals.update_status.emit(f"⚡ Processing...")
                ui.signals.update_color.emit("#f59e0b")
                ui.signals.update_subtitle.emit(f"You: {command}")

                result = execute(command)

                if not result:
                    ui.signals.update_status.emit("👋 Goodbye!")
                    ui.signals.update_subtitle.emit("See you soon Yashika!")
                    break

                ui.signals.update_status.emit("🤖 Say 'Jarvis'...")
                ui.signals.update_color.emit("#22c55e")
                ui.signals.update_subtitle.emit(f"You: {command}")

app = QApplication(sys.argv)
ui = FloatingUI()
ui.show()

thread = threading.Thread(target=jarvis_loop, args=(ui,), daemon=True)
thread.start()

sys.exit(app.exec_())