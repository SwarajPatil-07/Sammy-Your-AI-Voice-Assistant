import cohere
import os
from dotenv import load_dotenv

load_dotenv()
co = cohere.Client(os.getenv("COHERE_API_KEY"))

chat_history = []

def ask_cohere(prompt):
    global chat_history

    try:
        # Format chat history for Cohere
        formatted_history = [
            {"role": "USER", "message": msg["message"]} if msg["role"] == "user"
            else {"role": "CHATBOT", "message": msg["message"]}
            for msg in chat_history
        ]

        # Call Cohere Chat endpoint
        response = co.chat(
            model="command-r",
            message=prompt,
            chat_history=formatted_history,
            # or "command-r-plus" if allowed
            temperature=0.7,
        )

        # Extract reply
        reply = response.text.strip()

        # Add both user and assistant message to history
        chat_history.append({"role": "user", "message": prompt})
        chat_history.append({"role": "chatbot", "message": reply})

        return reply

    except Exception as e:
        return f"❌ Cohere API Error: {str(e)}"