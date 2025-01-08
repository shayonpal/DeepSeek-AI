#!/bin/bash

# Activate virtual environment
source ../venv/bin/activate

# Export environment variables
export DEEPSEEK_API_KEY="sk-501d1a0492274a6c9c745d8810967289"
export PORT=3000

# Start the Flask app in the background
nohup python app.py > logs/app.log 2>&1 &

# Save the process ID
echo $! > logs/app.pid

echo "DeepSeek Chat is running on http://127.0.0.1:3000 and http://10.0.0.140:3000" 