# DeepSeek Chat Interface

A modern web interface for the DeepSeek AI chat API, built with Flask and featuring real-time streaming responses, code syntax highlighting, and Markdown support.

## Features

- 🚀 Real-time streaming responses
- 💻 Code syntax highlighting with Prism.js
- ✨ Markdown rendering with marked.js
- 📋 One-click code copying
- 🎨 Dark theme with JetBrains Mono font
- 🌐 Network-accessible interface
- 🔄 Auto-startup capability (macOS)

## Prerequisites

- Python 3.x
- pip
- DeepSeek API key ([Get one here](https://platform.deepseek.com))

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/shayonpal/DeepSeek-AI.git
   cd DeepSeek-AI
   ```

2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root:
   ```bash
   echo "DEEPSEEK_API_KEY=your_api_key_here" > .env
   ```

## Usage

### Running Manually

1. Start the application:
   ```bash
   cd app
   ./start.sh
   ```

2. Access the chat interface at:
   - Local: `http://127.0.0.1:3000`
   - Network: `http://<your-ip>:3000`

3. To stop the application:
   ```bash
   ./stop.sh
   ```

### Auto-startup (macOS)

To configure the application to start automatically on login:

1. Copy the Launch Agent:
   ```bash
   cp app/com.deepseek.chat.plist ~/Library/LaunchAgents/
   ```

2. Load the Launch Agent:
   ```bash
   launchctl load ~/Library/LaunchAgents/com.deepseek.chat.plist
   ```

To disable auto-startup:
```bash
launchctl unload ~/Library/LaunchAgents/com.deepseek.chat.plist
```

## Development

The project structure is organized as follows:

```
DeepSeek-AI/
├── app/
│   ├── app.py              # Flask application
│   ├── templates/          # HTML templates
│   │   └── index.html     # Main chat interface
│   ├── start.sh           # Start script
│   ├── stop.sh            # Stop script
│   └── logs/              # Application logs
├── venv/                  # Virtual environment
├── .env                   # Environment variables
└── requirements.txt       # Python dependencies
```

## Logs

Application logs are stored in:
- `app/logs/app.log` - Main application log
- `app/logs/launchd.out.log` - Launch Agent stdout
- `app/logs/launchd.err.log` - Launch Agent stderr

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [DeepSeek AI](https://platform.deepseek.com) for their powerful chat API
- [Flask](https://flask.palletsprojects.com/) for the web framework
- [Prism.js](https://prismjs.com/) for code syntax highlighting
- [marked.js](https://marked.js.org/) for Markdown rendering 