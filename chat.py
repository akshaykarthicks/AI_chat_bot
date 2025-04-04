import os
from dotenv import load_dotenv
import google.generativeai as genai
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

load_dotenv()  # Load environment variables from .env file

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create the model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config,
)

history = []
chat_session = model.start_chat(history=history)

@app.route('/')
def home():
    return send_file('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    try:
        data = request.json
        user_message = data.get('message', '')
        
        if not user_message:
            return jsonify({'error': 'No message provided'}), 400

        response = chat_session.send_message(user_message)
        
        # Update history
        history.append({
            "role": "user",
            "parts": [user_message],
        })
        history.append({
            "role": "bot",
            "parts": [response.text],
        })
        
        return jsonify({'response': response.text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)