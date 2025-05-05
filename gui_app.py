import tkinter as tk
from tkinter import scrolledtext
from responder import speak_text
from recognizer import recognize_speech
from commands import handle_command
from cohere_chat import ask_cohere
import threading

class SammyGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Sammy - Your AI Assistant")
        self.window.geometry("500x600")
        self.window.configure(bg="#1e1e2f")

        self.chat_log = scrolledtext.ScrolledText(self.window, wrap=tk.WORD, bg="#282c34", fg="#f8f8f2",
                                                  font=("Consolas", 12), state='disabled')
        self.chat_log.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.input_frame = tk.Frame(self.window, bg="#1e1e2f")
        self.input_frame.pack(fill=tk.X, padx=10, pady=(0, 10))

        self.user_input = tk.Entry(self.input_frame, font=("Consolas", 12), bg="#3c3f4a", fg="white")
        self.user_input.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        self.user_input.bind("<Return>", self.handle_typed_command)

        self.send_button = tk.Button(self.input_frame, text="Send", font=("Consolas", 12), bg="#61afef", fg="white",
                                     command=self.handle_typed_command)
        self.send_button.pack(side=tk.RIGHT)

        self.mic_button = tk.Button(self.window, text="🎙️ Speak", font=("Consolas", 12), bg="#98c379", fg="black",
                                    command=self.handle_voice_command)
        self.mic_button.pack(pady=(0, 10))

        self.start_listening_thread()
        self.window.mainloop()

    def start_listening_thread(self):
        threading.Thread(target=self.listen_for_commands, daemon=True).start()

    def listen_for_commands(self):
        while True:
            from wake_word import detect_wake_word
            detect_wake_word()
           
            self.append_message("🟢 Sammy", "Yes, how can I help you?")
            speak_text("Yes, how can I help you?")

            command = recognize_speech()
            self.process_command(command)

    def handle_voice_command(self):
        command = recognize_speech()
        self.process_command(command)

    def handle_typed_command(self, event=None):
        command = self.user_input.get()
        self.user_input.delete(0, tk.END)
        self.process_command(command)

    def append_message(self, sender, message):
        self.chat_log.configure(state='normal')
        self.chat_log.insert(tk.END, f"{sender}: {message}\n")
        self.chat_log.configure(state='disabled')
        self.chat_log.yview(tk.END)

    def process_command(self, command):
        if not command:
            
            self.append_message("Sammy", "Sorry, I didn’t catch that.")
            speak_text("Sorry, I didn’t catch that.")
            return

        self.append_message("🧑 You", command)
        response = handle_command(command)

        if response:
            self.append_message("🟢 Sammy", response)
            speak_text(response)
        else:
            ai_response = ask_cohere(command)
            self.append_message("🟢 Sammy", ai_response)
            speak_text(ai_response)

if __name__ == "__main__":
    SammyGUI()
