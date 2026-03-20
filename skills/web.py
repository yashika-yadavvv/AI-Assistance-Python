# ============================================
# JARVIS — WEB SKILLS
# ============================================

import webbrowser
import requests

def get_weather(city="Delhi"):
    api_key = "your-weather-api-key"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        data = requests.get(url).json()
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        return f"Weather in {city} is {desc} with temperature {temp} degrees celsius"
    except:
        return "Sorry, couldn't fetch weather"

def google_search(query):
    webbrowser.open(f"https://www.google.com/search?q={query}")
    return f"Searching for {query}"

def open_youtube(query):
    webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
    return f"Playing {query} on YouTube"