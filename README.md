# 🤖 Bot Factory - AI-Powered Bot Generator

An intelligent Telegram bot that generates custom bots on demand using Claude AI. Simply tell it what kind of bot you want, and it creates a fully functional, production-ready bot for you.

## ✨ Features

- **AI-Powered Generation**: Uses Claude 3.5 Sonnet to generate custom bot code
- **Multiple Bot Types**:
  - 🎮 Gaming Bots (Trivia, Word Games, etc.)
  - 📚 Educational Bots (Learning tools, Quizzes)
  - 💼 Business Bots (CRM, Scheduling, Analytics)
  - 🎨 Creative Bots (Image generation, Design tools)
  - 🤖 AI Assistants (Chat, Translation, Summarization)
  - 🎵 Music Bots (Playlist management, Recommendations)
  - 📊 Data Bots (Analytics, Reporting, Dashboards)
  - ✏️ Custom Bots (Anything you can imagine!)

- **Complete Bot Generation**:
  - Fully functional Python code
  - Requirements.txt with all dependencies
  - Setup instructions
  - Command documentation
  - Production-ready and well-documented

- **Interactive UI**: Easy-to-use inline buttons and prompts

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Telegram Bot Token (from [@BotFather](https://t.me/botfather))
- Anthropic API Key (from [Anthropic Console](https://console.anthropic.com))

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/a89785285-dev/telegram-bot-.git
   cd telegram-bot-
   git checkout bot-factory
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Setup environment variables**
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` and add:
   - Your Telegram Bot Token
   - Your Anthropic API Key

5. **Run the bot**
   ```bash
   python bot_factory.py
   ```

## 🎮 Usage

1. **Start the bot**: `/start`
2. **Select bot type** from the inline menu
3. **Describe features** you want (e.g., "chat, image processing, user profiles")
4. **Add customizations** (e.g., "multilingual, fast response, database integration")
5. **AI generates your bot** with:
   - Complete source code
   - Setup instructions
   - List of features
   - Required dependencies
6. **Use your generated bot** by following the setup instructions

## 📋 Available Commands

- `/start` - Begin creating a bot
- `/help` - Show help information
- `/examples` - See example bots

## 🎯 Example Bot Ideas

### Gaming
- Wordle game bot
- 20 questions game
- Chess multiplayer bot
- Riddle daily challenge

### AI & Assistance
- ChatGPT-like assistant
- Code review bot
- Translation bot
- Summarization bot

### Business
- Task management bot
- Invoice generator
- Appointment scheduler
- Expense tracker

### Educational
- Language learning bot
- Daily quote bot
- Quiz master bot
- Math tutor bot

## 🔧 Generated Bot Structure

Each generated bot includes:

```
generated_bots/
├── [user_id]/
│   └── [bot_name]/
│       ├── bot.py              # Main bot code
│       ├── requirements.txt     # Dependencies
│       ├── config.json          # Bot configuration
│       └── SETUP.md             # Setup instructions
```

## 🛠️ Technical Details

- **Framework**: python-telegram-bot
- **AI Model**: Claude 3.5 Sonnet
- **Architecture**: Conversation Handler for state management
- **Code Generation**: Dynamic prompt engineering

## 📝 How It Works

1. User describes desired bot type and features
2. Bot Factory creates a detailed prompt for Claude AI
3. Claude generates:
   - Complete, production-ready Python code
   - List of required packages
   - Setup instructions
   - Feature documentation
4. Bot Factory saves everything to organized directories
5. User can copy the generated code and run immediately

## ⚙️ API Keys

### Telegram Bot Token
1. Open Telegram and search for `@BotFather`
2. Send `/start`
3. Send `/newbot`
4. Follow the prompts
5. Copy your token

### Anthropic API Key
1. Go to [console.anthropic.com](https://console.anthropic.com)
2. Sign up or login
3. Generate an API key
4. Copy it to your `.env` file

## 🚨 Error Handling

The bot includes comprehensive error handling:
- Invalid responses from AI
- Network failures
- File system errors
- User input validation

## 🔐 Security

- API keys stored in `.env` (not committed)
- User data isolated in separate directories
- No storage of sensitive information
- `.gitignore` protects generated files

## 🎓 Learning Resources

- [python-telegram-bot Documentation](https://python-telegram-bot.readthedocs.io/)
- [Anthropic API Documentation](https://docs.anthropic.com/)
- [Telegram Bot API](https://core.telegram.org/bots/api)

## 🤝 Contributing

Feel free to fork, modify, and improve!

## 📄 License

GPL-3.0 License

## 🌟 Features Roadmap

- [ ] Web interface for bot generation
- [ ] Bot deployment to cloud (Heroku, Railway, etc.)
- [ ] Bot marketplace/sharing system
- [ ] Advanced customization templates
- [ ] Multi-language support
- [ ] Database integration templates
- [ ] API integration helpers
- [ ] Testing framework generation

## 🆘 Troubleshooting

### Bot doesn't start
- Check TELEGRAM_BOT_TOKEN in .env
- Verify internet connection
- Check Python version (3.8+)

### API errors
- Verify ANTHROPIC_API_KEY is correct
- Check API account has credits
- Review rate limits

### Generated code issues
- Check all requirements are installed
- Verify Python 3.8+ compatibility
- Check generated code for syntax

## 📞 Support

For issues, questions, or suggestions, please create an issue on GitHub.

---

**Made with ❤️ using Claude AI**
