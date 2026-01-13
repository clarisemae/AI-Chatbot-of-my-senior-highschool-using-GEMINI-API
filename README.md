# JPI Muzon AI Assistant

This repository contains a context-aware AI chatbot developed for **Japan-Philippines Institute of Technology (JPI) – Muzon Campus**. The application utilizes the **Google Gemini 2.0 Flash model** to provide real-time, accurate responses regarding school enrollment, academic strands, and general inquiries.

![Application Screenshot](image.png)

## Overview

The goal of this project is to create a lightweight conversational agent capable of maintaining context over multiple turns. It references a specialized dataset (via prompt history) to ensure answers are specific to JPI Muzon's policies and location.

The project includes both a web-based interface (Flask) and a command-line interface (CLI) for testing.

## Tech Stack

* **Backend:** Python 3, Flask
* **AI/LLM:** Google Generative AI (`gemini-2.0-flash`)
* **Data Persistence:** Local JSON file storage (`history.json`)
* **Frontend:** HTML/CSS (Jinja2 templates)

## 📂 Project Structure

```text
├── app.py             # Main Flask application with input validation
├── chatbot.py         # CLI version for terminal testing
├── history.json       # Stores conversation context logs
├── static/            # CSS and static assets
│   ├── images/
│   └── styles.css
├── templates/
│   └── chatbot.html   # Frontend interface
├── .env               # Environment variables (API Key)
└── README.md

```

## ⚙️ Setup and Installation

Follow these steps to get the project running locally.

### 1. Clone the repository

```bash
git clone [https://github.com/yourusername/jpi-muzon-chatbot.git](https://github.com/yourusername/jpi-muzon-chatbot.git)
cd jpi-muzon-chatbot

```

### 2. Set up a Virtual Environment

It is recommended to use a virtual environment to manage dependencies.

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate

```

### 3. Install Dependencies

```bash
pip install flask google-generativeai python-dotenv

```

### 4. Configure Environment Variables

Create a `.env` file in the root directory and add your Gemini API key:

```env
GEMINI_API_KEY=your_api_key_here

```

*> **Note:** The `.env` file is excluded from version control for security.*

## Usage

### Web Interface

To run the full web application:

```bash
python app.py

```

Access the interface at `http://127.0.0.1:5000/`. The web app includes HTML formatting for links and bold text.

### CLI Version

To run the terminal-based version for quick logic testing:

```bash
python chatbot.py

```

Type `bye` to terminate the session.

## Implementation Details

* **Context Management:** The application loads and saves conversation history to `history.json` on every turn. This allows the model to "remember" previous interactions (e.g., if a user asks "Where is it located?" after discussing the school name).
* **Input Validation:** The web application (`app.py`) includes a validation layer (`validate_user_input`) to intercept specific queries and cross-reference them with chat history before querying the LLM.
* **Formatting:** Responses are processed to convert Markdown (bolding, links) into HTML tags for the frontend and clean text for the CLI.

## Future Improvements

* Migrate data persistence from `history.json` to a lightweight database (SQLite).
* Implement RAG (Retrieval-Augmented Generation) to query the student handbook dynamically.
* Improve frontend UI with Bootstrap or Tailwind CSS.

```