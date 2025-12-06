# AI-Chatbot-of-my-senior-highschool-using-GEMINI-API

Just a quick project to test out Gemini API for Chatbot

## JPI Muzon AI Assistant
This repository contains a context-aware AI chatbot developed for Japan-Philippines Institute of Technology (JPI) – Muzon Campus. The application utilizes the Google Gemini 2.0 Flash model to provide real-time, accurate responses regarding school enrollment, academic strands, and general inquiries.

The project includes both a web-based interface (Flask) and a command-line interface (CLI) for testing.

## Overview
The goal of this project was to create a lightweight conversational agent capable of maintaining context over multiple turns. It references a specialized dataset (via prompt history) to ensure answers are specific to JPI Muzon's policies and location.

## Tech Stack
Backend: Python 3, Flask
AI/LLM: Google Generative AI (gemini-2.0-flash)
Data Persistence: Local JSON file storage (history.json)
Frontend: HTML/CSS (Jinja2 templates)

If you want to test this code make sure to have Python installed and these dependencies:
---> pip install flask google-generativeai

then change the .env file in the root directory and add your Gemini API key

python app.py --> to run the web app
python chatbot.py --> to run in terminal


Here is a cleaner, "formal casual" version. It cuts the fluff and focuses on the technical implementation, which is how most CS students write READMEs for portfolios or assignments.

JPI Muzon AI Assistant
This repository contains a context-aware AI chatbot developed for Japan-Philippines Institute of Technology (JPI) – Muzon Campus. The application utilizes the Google Gemini 2.0 Flash model to provide real-time, accurate responses regarding school enrollment, academic strands, and general inquiries.

The project includes both a web-based interface (Flask) and a command-line interface (CLI) for testing.

Overview
The goal of this project was to create a lightweight conversational agent capable of maintaining context over multiple turns. It references a specialized dataset (via prompt history) to ensure answers are specific to JPI Muzon's policies and location.

Tech Stack
Backend: Python 3, Flask

AI/LLM: Google Generative AI (gemini-2.0-flash)

Data Persistence: Local JSON file storage (history.json)

Frontend: HTML/CSS (Jinja2 templates)

Project Structure
Bash

├── app.py             # Main Flask application with input validation
├── chatbot.py         # CLI version for terminal testing
├── history.json       # Stores conversation context logs
├── templates/
│   └── chatbot.html   # Frontend interface
├── .env               # Environment variables (API Key)
└── README.md
Setup and Installation
Clone the repository

Bash

git clone https://github.com/yourusername/jpi-muzon-chatbot.git
cd jpi-muzon-chatbot
Install dependencies Ensure you have Python installed, then run:

Bash

pip install flask google-generativeai
Environment Configuration Create a .env file in the root directory and add your Gemini API key:

Bash

GEMINI_API_KEY=your_api_key_here
Note: The .env file is excluded from version control for security.

Usage
Web Interface
To run the web application:

Bash

python app.py
Access the interface at http://127.0.0.1:5000/. The web app includes HTML formatting for links and bold text.

CLI Version
To run the terminal-based version for quick logic testing:

Bash

python chatbot.py
Type bye to terminate the session.

## Implementation Details
Context Management: The application loads and saves conversation history to history.json on every turn. This allows the model to "remember" previous interactions (e.g., if a user asks "Where is it located?" after discussing the school name).

Input Validation: The web application (app.py) includes a validation layer (validate_user_input) to intercept specific queries and cross-reference them with chat history before querying the LLM.

Formatting: Responses are processed to convert Markdown (bolding, links) into HTML tags for the frontend and clean text for the CLI.

## Future Improvements
Migrate data persistence from history.json to a lightweight database (SQLite).

Implement RAG (Retrieval-Augmented Generation) to query the student handbook dynamically.

Improve frontend UI with Bootstrap or Tailwind CSS.