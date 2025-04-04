# AI Chatbot with Web Interface

A modern chatbot application built using Google's Gemini AI model with a clean web interface.

## Features

- Real-time chat interface
- Powered by Google's Gemini Pro 1.5 AI model
- Modern and responsive web design
- Message history tracking
- Easy-to-use interface

## Prerequisites

- Python 3.x
- Google Gemini API key

## Required Python Packages

```
flask
flask-cors
python-dotenv
google-generativeai
```

## Setup

1. Clone this repository or download the files
2. Create a `.env` file in the project root directory
3. Add your Gemini API key to the `.env` file:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

## Installation

1. Create a virtual environment:
   ```
   python -m venv venv
   ```

2. Activate the virtual environment:
   - Windows:
     ```
     .\venv\Scripts\activate
     ```
   - Linux/Mac:
     ```
     source venv/bin/activate
     ```

3. Install required packages:
   ```
   pip install flask flask-cors python-dotenv google-generativeai
   ```

## Running the Application

1. Make sure your virtual environment is activated
2. Run the Flask server:
   ```
   python chat.py
   ```
3. Open your web browser and navigate to:
   ```
   http://localhost:5000
   ```

## Project Structure

- `chat.py` - Main Python server file with Gemini AI integration
- `index.html` - Web interface
- `.env` - Environment variables (API key)
- `README.md` - Project documentation

## Usage

1. Start the server using the instructions above
2. Type your message in the input field
3. Press Enter or click the Send button to send your message
4. The AI will respond in real-time

## Security Notes

- Keep your API key secure and never commit it to version control
- This is a development server and should not be used in production
- For production deployment, use a proper WSGI server

## Development

The project uses:
- Flask for the backend server
- Google's Generative AI for chat responses
- Modern HTML/CSS for the interface
- JavaScript for real-time interactions

## License

This project is open source and available under the MIT License.
