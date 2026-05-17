# Bot Factory - User Guide

## Table of Contents
1. [Getting Started](#getting-started)
2. [Creating Your First Bot](#creating-your-first-bot)
3. [Bot Types Explained](#bot-types-explained)
4. [Features & Customization](#features--customization)
5. [Running Generated Bots](#running-generated-bots)
6. [Tips & Tricks](#tips--tricks)
7. [Troubleshooting](#troubleshooting)

## Getting Started

### Prerequisites
- Telegram account
- Telegram bot token (from @BotFather)
- Anthropic API key
- Python 3.8 or higher
- Basic command line knowledge

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/a89785285-dev/telegram-bot-.git
   cd telegram-bot-
   git checkout bot-factory
   ```

2. **Set up Python environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment**
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` and add your tokens:
   ```
   TELEGRAM_BOT_TOKEN=YOUR_TOKEN_HERE
   ANTHROPIC_API_KEY=YOUR_KEY_HERE
   ```

5. **Start the Bot Factory**
   ```bash
   python bot_factory.py
   ```

## Creating Your First Bot

### Step-by-Step Process

#### Step 1: Start the Conversation
- Open Telegram and find your Bot Factory bot
- Send `/start`
- You'll see 8 bot type options

#### Step 2: Select Bot Type
Choose from:
- 🎮 Gaming Bot
- 📚 Educational Bot
- 💼 Business Bot
- 🎨 Creative Bot
- 🤖 AI Assistant
- 🎵 Music Bot
- 📊 Data Bot
- ✏️ Custom Bot

#### Step 3: Describe Features
Be specific about what you want:

**Good examples:**
- "multiplayer chess with ranking system"
- "vocabulary learning with spaced repetition"
- "task management with recurring tasks and reminders"
- "image generation with style selection"

**Vague examples (less optimal):**
- "game"
- "useful bot"
- "something cool"

#### Step 4: Add Customizations (Optional)
Specify any special requirements:
- "multilingual support (English, French, Arabic)"
- "database integration with PostgreSQL"
- "fast response time"
- "offline functionality"
- "webhook support"

Or simply type "none" if you're happy with defaults.

#### Step 5: Let AI Generate
Wait for Claude AI to generate your bot (usually 30-60 seconds)

#### Step 6: Receive Your Bot
You'll get:
- Bot name and description
- Features list
- Setup instructions
- File location

## Bot Types Explained

### 🎮 Gaming Bot
**What it creates:** Entertaining interactive games

**Example ideas:**
- Trivia quiz with categories
- Wordle/hangman game
- 20 questions game
- Math challenge game
- Word association game

**Typical features:**
- Score tracking
- Difficulty levels
- Leaderboards
- Multiplayer support

### 📚 Educational Bot
**What it creates:** Learning and teaching tools

**Example ideas:**
- Language learning assistant
- Quiz generator
- Flashcard bot
- History facts bot
- Science tutorial bot

**Typical features:**
- Progressive lessons
- Quiz functionality
- Progress tracking
- Spaced repetition

### 💼 Business Bot
**What it creates:** Productivity and business tools

**Example ideas:**
- Task management
- Invoice generator
- Appointment scheduler
- Expense tracker
- Customer CRM

**Typical features:**
- Database storage
- Reminders
- Reporting
- User authentication

### 🎨 Creative Bot
**What it creates:** Creative and generative tools

**Example ideas:**
- AI image generator
- Story generator
- Poem creator
- Design assistant
- Color palette generator

**Typical features:**
- Content generation
- Style customization
- Save/share functionality
- Gallery of creations

### 🤖 AI Assistant
**What it creates:** Intelligent assistant bots

**Example ideas:**
- ChatGPT-like assistant
- Code reviewer
- Translator
- Summarizer
- Research assistant

**Typical features:**
- Natural language processing
- Context awareness
- Multi-turn conversations
- Knowledge base integration

### 🎵 Music Bot
**What it creates:** Music-related tools

**Example ideas:**
- Playlist manager
- Music recommendation engine
- Lyric finder
- Music quiz
- Artist info bot

**Typical features:**
- Search functionality
- Playlist organization
- Recommendations
- User history

### 📊 Data Bot
**What it creates:** Analytics and data visualization

**Example ideas:**
- Dashboard creator
- Analytics reporter
- Data aggregator
- Statistics calculator
- Chart generator

**Typical features:**
- Data collection
- Visualization
- Report generation
- Export options

### ✏️ Custom Bot
**What it creates:** Anything you want!

**Example ideas:**
- Pet care reminder
- Fitness tracker
- Recipe suggester
- Book club manager
- Anything unique!

**Typical features:**
- Completely customizable
- Based on your specifications
- Tailored to your needs

## Features & Customization

### Writing Good Feature Descriptions

**Structure:** Feature + Purpose + Details

**Examples:**

❌ "Good chat"
✅ "Chat functionality with context memory, multi-turn conversations, and ability to remember user preferences"

❌ "Games"
✅ "Multiplayer trivia game with 5 difficulty levels, score tracking, and weekly leaderboard"

❌ "Task management"
✅ "Task management with categories, due dates, reminders, priority levels, and recurring task support"

### Customization Options

**Performance**
- "Fast response time (< 1 second)"
- "Optimized for low bandwidth"
- "Supports 10,000+ concurrent users"

**Integration**
- "Database integration (PostgreSQL)"
- "Webhook support for external APIs"
- "Payment gateway integration"
- "Third-party service integration"

**Language & Localization**
- "Multilingual (English, Spanish, French)"
- "Right-to-left text support"
- "Timezone awareness"

**User Experience**
- "Inline buttons for easy navigation"
- "Keyboard shortcuts"
- "Dark/light mode support"
- "Accessibility features"

**Security & Privacy**
- "User authentication"
- "Data encryption"
- "GDPR compliance"
- "Rate limiting"

**Advanced Features**
- "Machine learning integration"
- "Real-time updates"
- "File upload/download"
- "Scheduled tasks"

## Running Generated Bots

### Step-by-Step Guide

1. **Navigate to bot directory**
   ```bash
   cd generated_bots/[YOUR_USER_ID]/[BOT_NAME]
   ```

2. **Create virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create .env file**
   ```bash
   cp ../../../.env.example .env
   # Edit .env with your bot token
   ```

5. **Run the bot**
   ```bash
   python bot.py
   ```

6. **Test in Telegram**
   - Find your bot
   - Send `/start`
   - Try the available commands

### Managing Multiple Bots

You can run multiple bots simultaneously:

```bash
# Terminal 1
cd generated_bots/[ID]/bot1
python bot.py

# Terminal 2
cd generated_bots/[ID]/bot2
python bot.py

# And so on...
```

Or use a process manager like `tmux` or `screen`.

## Tips & Tricks

### Getting Better Results

1. **Be Specific**
   - More detail = better bot
   - Include exact feature names
   - Mention any integrations needed

2. **Think About Flow**
   - How users interact
   - What commands are needed
   - Error handling

3. **Test Thoroughly**
   - Try all commands
   - Test edge cases
   - Check error messages

### Improving Generated Code

1. **Code Review**
   - Check the generated code
   - Understand the structure
   - Look for improvements

2. **Customization**
   - Add your own functions
   - Integrate real APIs
   - Add database connection

3. **Deployment**
   - Set up proper environment
   - Configure logging
   - Set up monitoring

### Iterative Development

1. **Start Simple**
   - Create basic bot first
   - Test and deploy
   - Add features gradually

2. **Use Version Control**
   ```bash
   git init
   git add .
   git commit -m "Initial bot version"
   ```

3. **Keep Notes**
   - Document changes
   - Track feature requests
   - Note improvements

## Troubleshooting

### Bot doesn't start

**Error: ModuleNotFoundError**
```bash
# Solution: Install dependencies
pip install -r requirements.txt
```

**Error: Invalid token**
```bash
# Check your .env file
cat .env
# Make sure TELEGRAM_BOT_TOKEN is correct
```

### AI Generation fails

**Error: Invalid API key**
```
# Verify ANTHROPIC_API_KEY in .env
# Check API key in Anthropic console
```

**Error: JSON parsing failed**
```
# This is rare - try again
# The AI response might have been malformed
```

### Generated code has issues

**Syntax errors**
```bash
# Try running with verbose mode
python -m py_compile bot.py
```

**Missing imports**
```bash
# Install missing packages
pip install [package_name]
```

**Runtime errors**
```bash
# Check error messages
# Review generated code
# Verify API keys and tokens
```

### Telegram API issues

**Bot not responding**
- Check internet connection
- Verify bot token
- Check Telegram server status

**Slow response**
- Check server load
- Optimize code
- Use async operations

**Commands not working**
- Check command syntax
- Verify permissions
- Review command handlers

### File not found errors

**config.json missing**
```bash
# Check generated_bots directory
ls -la generated_bots/
# Make sure files were created
```

**requirements.txt missing**
```bash
# Download from repository
wget https://raw.github.com/.../requirements.txt
```

## Getting Help

### Documentation
- Read [README.md](../README.md)
- Check [ARCHITECTURE.md](./ARCHITECTURE.md)
- Review generated bot code

### External Resources
- [python-telegram-bot Docs](https://python-telegram-bot.readthedocs.io/)
- [Anthropic API Docs](https://docs.anthropic.com/)
- [Telegram Bot API](https://core.telegram.org/bots/api)

### Community
- GitHub Issues
- Stack Overflow
- Telegram Bot API group

---

**Happy bot building! 🚀**
