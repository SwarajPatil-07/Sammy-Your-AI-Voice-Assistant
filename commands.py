import time
import webbrowser
# import random
import os

from weather import get_weather

def get_time():
    current_time = time.strftime("%I:%M %p")
    return f"The Current time is {current_time}"

def handle_command(command):
    command = command.lower()

    if "open" in command and "website" in command:
        speak_text = "Which website would you like to open?"
        return speak_text
    
    elif "open" in command:
        words = command.split()
        for i, word in enumerate(words):
            if word == "open" and i+1 < len(words):
                website = words[i+1]
                url = f"https://{website}.com"
                webbrowser.open(url)
                return f"Opening {website}."

    elif "play music" in command:
        music_dir = "sammy_assistant\music"
        songs = os.listdir(music_dir)
        os.startfile(os.path.join(music_dir, songs[0]))
        return "Playing music."
        
    elif "time" in command:
        current_time = get_time()
        return(current_time)
    
    elif "weather" in command:
        city = command.split("weather in")[-1].strip()
        return get_weather(city)


    return None      


