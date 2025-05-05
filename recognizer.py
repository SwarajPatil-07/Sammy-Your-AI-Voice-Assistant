import speech_recognition as sr 

def recognize_speech():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        print("Listening for your command...")
        recognizer.adjust_for_ambient_noise(source)
        try:

            audio = recognizer.listen(source, timeout=5)
        except sr.WaitTimeoutError:
            print("⏱️ Listening timed out while waiting for phrase to start.")
            return None
    

    try:
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
        return None


    except sr.RequestError:
        print("⚠️ Could not request results from Google Speech Recognition.")
        return None

