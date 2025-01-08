from flask import Flask, render_template, request, jsonify, Response
from flask_cors import CORS
from openai import OpenAI
import os
from dotenv import load_dotenv
import json

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# Initialize OpenAI client with DeepSeek configuration
client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        messages = data.get('messages', [])
        
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=messages,
            stream=True
        )
        
        def generate():
            for chunk in response:
                if hasattr(chunk.choices[0].delta, 'content') and chunk.choices[0].delta.content is not None:
                    yield f"data: {json.dumps({'content': chunk.choices[0].delta.content})}\n\n"
            yield "data: [DONE]\n\n"
        
        return Response(generate(), mimetype='text/event-stream')

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=3000) 