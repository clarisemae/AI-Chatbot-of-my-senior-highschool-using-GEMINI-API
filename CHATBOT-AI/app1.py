from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import json
import os
import re

app = Flask(__name__)

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

# Format message for HTML (browser)
def format_message(text):
    text = text.replace("\n", "<br>")  # Line breaks for browser
    text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)  # Bold
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2" target="_blank">\1</a>', text)  # Links
    return text

# Generate response using Gemini
def generate_response(user_input, history):
    # Prepare the history in Gemini format
    contents = []
    for entry in history:
        contents.append({"role": entry["role"], "parts": [entry["text"]]})

    # Add current user input
    contents.append({"role": "user", "parts": [user_input]})

    # Generate response
    response = model.generate_content(contents)
    return response.text

@app.route('/')
def index():
    return render_template('chatbot.html')  # Your chatbot.html page

@app.route('/send_message', methods=['POST'])
def send_message():
    user_input = request.json['user_input']
    
    # Load conversation history from JSON file
    history = load_history()

    # If 'bye', clear history
    if user_input.lower() == "bye":
        history = []
        save_history(history)
        return jsonify({'response': "Chat ended. See you next time!"})

    # Generate model response
    model_response = generate_response(user_input, history)

    # Format response for browser (HTML)
    formatted_response = format_message(model_response)

    return jsonify({'response': formatted_response})


if __name__ == "__main__":
    app.run(debug=True)
