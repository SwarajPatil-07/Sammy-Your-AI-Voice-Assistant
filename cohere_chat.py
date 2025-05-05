import cohere
import os
from dotenv import load_dotenv

load_dotenv()
co = cohere.Client(os.getenv("COHERE_API_KEY"))

chat_history = []

def ask_cohere(prompt):
    global chat_history

    try:
        formatted_history = [
            {"role": "USER", "message": msg["message"]} if msg["role"] == "user"
            else {"role": "CHATBOT", "message": msg["message"]}
            for msg in chat_history
        ]

   
        response = co.chat(
            model="command-r",
            message=prompt,
            chat_history=formatted_history,
            
            temperature=0.7,
        )

 
        reply = response.text.strip()

     
        chat_history.append({"role": "user", "message": prompt})
        chat_history.append({"role": "chatbot", "message": reply})

        return reply

    except Exception as e:
        return f"❌ Cohere API Error: {str(e)}"
