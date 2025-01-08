from flask import Flask, render_template, request, jsonify, Response
from flask_cors import CORS
from openai import OpenAI
import os
from dotenv import load_dotenv
import json
import sys

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# Initialize OpenAI client with DeepSeek configuration
api_key = os.getenv("DEEPSEEK_API_KEY", "sk-501d1a0492274a6c9c745d8810967289")
print(f"Using API key (last 4): ...{api_key[-4:]}", file=sys.stderr)

client = OpenAI(
    api_key=api_key,
    base_url="https://api.deepseek.com"
)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        print("Received chat request", file=sys.stderr)
        data = request.json
        messages = data.get('messages', [])
        print(f"Messages: {json.dumps(messages, indent=2)}", file=sys.stderr)
        
        def generate():
            try:
                print("Making API request...", file=sys.stderr)
                response = client.chat.completions.create(
                    model="deepseek-chat",
                    messages=messages,
                    stream=True
                )
                print("Got API response", file=sys.stderr)
                
                for chunk in response:
                    print(f"Got chunk: {chunk}", file=sys.stderr)
                    if hasattr(chunk.choices[0].delta, 'content') and chunk.choices[0].delta.content is not None:
                        content = chunk.choices[0].delta.content
                        print(f"Sending content: {content}", file=sys.stderr)
                        yield f"data: {json.dumps({'content': content})}\n\n"
                
                print("Stream finished", file=sys.stderr)
                yield "data: [DONE]\n\n"
                
            except Exception as e:
                print(f"Error in generate: {str(e)}", file=sys.stderr)
                yield f"data: {json.dumps({'error': str(e)})}\n\n"
        
        return Response(generate(), mimetype='text/event-stream')

    except Exception as e:
        print(f"Error in chat: {str(e)}", file=sys.stderr)
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Test API connection
    try:
        print("Testing API connection...", file=sys.stderr)
        test_response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[{"role": "user", "content": "test"}],
            max_tokens=5,
            stream=False
        )
        print("API test successful!", file=sys.stderr)
    except Exception as e:
        print(f"API test failed: {str(e)}", file=sys.stderr)
    
    app.run(debug=True, host='0.0.0.0', port=3000) 