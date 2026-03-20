# ============================================
# JARVIS — FILE SKILLS
# ============================================

import os

def list_files(path="."):
    files = os.listdir(path)
    return f"Files: {', '.join(files)}"

def create_note(filename, content):
    with open(f"{filename}.txt", "w") as f:
        f.write(content)
    return f"Note saved as {filename}.txt"

def read_note(filename):
    try:
        with open(f"{filename}.txt", "r") as f:
            return f.read()
    except:
        return "File not found"