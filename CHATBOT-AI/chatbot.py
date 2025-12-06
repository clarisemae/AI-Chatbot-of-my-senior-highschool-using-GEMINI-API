import os
import json
import google.generativeai as genai
import re

# Configure Gemini API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize the model
model = genai.GenerativeModel('gemini-2.0-flash')

# Load conversation history
def load_history():
    if os.path.exists("history.json"):
        with open("history.json", "r") as f:
            return json.load(f)
    return []

# Save conversation history
def save_history(history):
    with open("history.json", "w") as f:
        json.dump(history, f, indent=4)

# Format message for CLI
def format_message(text):
    text = text.replace("**", "")  # Remove bold
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'\1', text)  # Remove links
    return text

# Generate response using Gemini
def generate_response(user_input, history):
    # Prepare the history for Gemini (structured roles)
    contents = []
    for entry in history:
        role = entry["role"]
        text = entry["text"]
        contents.append({"role": role, "parts": [text]})
    
    # Add current user input
    contents.append({"role": "user", "parts": [user_input]})

    # Generate response
    response = model.generate_content(contents)
    return response.text

# Main CLI chatbot loop
if __name__ == "__main__":
    history = load_history()
    print("Chatbot (type 'bye' to exit)\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Chat ended.")
            break

        # Generate response
        model_response = generate_response(user_input, history)
        clean_response = format_message(model_response)
        print(f"Bot: {clean_response}\n")

        # Save history
        history.append({"role": "user", "text": user_input})
        history.append({"role": "model", "text": model_response})
        save_history(history)