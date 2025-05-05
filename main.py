from wake_word import detect_wake_word
from recognizer import recognize_speech
from responder import speak_text
from commands import get_time, handle_command
from cohere_chat import ask_cohere
from gui_app import SammyGUI


if __name__ == "__main__":
    mode = input("Type 'gui' to start with GUI or press Enter for voice mode: ")

    if mode == "gui":
        SammyGUI()
    
    else:
        detect_wake_word()
        speak_text("Yes, how can I help you?")
        user_command = recognize_speech()

        if not user_command:
            speak_text("Sorry, I didn't catch that. You can type your command instead.")
            user_command = input("Type your command: ").lower()

        if user_command:

            response = handle_command(user_command)


            if response:
                speak_text(response)

            else:
                ai_response = ask_cohere(user_command)
                speak_text(ai_response)

        
    


    

        # if "time" in user_command:
        #     current_time = get_time()
        #     speak_text(current_time)

    # elif "joke" in user_command:
    #     joke = tell_joke()
    #     speak_text(joke)

        # elif "open" in user_command:
        #     words = user_command.split()
        # # Try to extract the word after 'open'
        #     try:
        #         site_index = words.index("open") + 1
        #         site = words[site_index]

        #         if "." not in site:
        #             site += ".com"

        # # Add www. if it's a common domain
        #     if not site.startswith("www."):
        #         site = "www." + site

        # # Prepend https:// if missing
        #     if not site.startswith("http"):
        #         site = "https://" + site

        #     speak_text(f"Opening {site}")
        #     open_website(site)

        # except (IndexError, ValueError):
        #     speak_text("I couldn't figure out which website to open.")

    # elif "hello" in user_command:
    #     speak_text("Hello! How can I assist you today?")
        
    
        
        

