# ============================================
# JARVIS — BRAIN (Groq LLM)
# ============================================

from groq import Groq
from config import OPENAI_API_KEY, ASSISTANT_NAME, USER_NAME
from core.memory import get_recent_conversations, save_conversation

client = Groq(api_key=OPENAI_API_KEY)

def ask_jarvis(user_input):
    history = get_recent_conversations(5)
    messages = [
        {
            "role": "system",
            "content": f"You are {ASSISTANT_NAME}, a smart AI desktop assistant. "
                      f"You are talking to {USER_NAME}. "
                      f"Keep responses short, helpful and friendly."
        }
    ]
    for past_input, past_response in reversed(history):
        messages.append({"role": "user", "content": past_input})
        messages.append({"role": "assistant", "content": past_response})

    messages.append({"role": "user", "content": user_input})

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            max_tokens=150
        )
        reply = response.choices[0].message.content.strip()
        save_conversation(user_input, reply)
        return reply
    except Exception as e:
        return f"Sorry, I couldn't process that. Error: {str(e)}"