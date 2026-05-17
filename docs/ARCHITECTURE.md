# Bot Factory Architecture

## Overview

Bot Factory is an AI-powered Telegram bot that generates custom bots on demand. It uses Claude 3.5 Sonnet to understand user requirements and generate production-ready Python code.

## Components

### 1. Main Application (`bot_factory.py`)

#### Core Classes

**BotFactory**
- Manages bot generation process
- Communicates with Claude AI
- Creates bot file structure
- Stores bot configurations

#### Conversation States

```
start() → ASKING_BOT_TYPE
          ↓
    handle_bot_type() → ASKING_FEATURES
                        ↓
                  handle_features() → ASKING_CUSTOMIZATION
                                      ↓
                            handle_customization() → GENERATING
                                                      ↓
                                                    [AI Generation]
                                                      ↓
                                            Conversation Ends
```

### 2. AI Integration

**Anthropic Claude AI**
- Model: Claude 3.5 Sonnet
- Purpose: Generate bot code based on user specifications
- Prompt Engineering: Detailed instructions for code generation quality

**Prompt Structure**
```
Bot Type: [Type selected]
Required Features: [User specifications]
Customization Requests: [Additional requirements]

→ Response in JSON format:
  {
    "bot_name": "...",
    "description": "...",
    "main_code": "...",
    "requirements": "...",
    "setup_instructions": "...",
    "commands": "...",
    "features_implemented": "..."
  }
```

### 3. File Structure

```
Bot Factory/
├── bot_factory.py           # Main application
├── requirements.txt         # Dependencies
├── .env.example            # Configuration template
├── .gitignore              # Git ignore rules
├── README.md               # User documentation
├── docs/
│   └── ARCHITECTURE.md     # This file
├── examples.json           # Example bot templates
└── generated_bots/         # Generated bot storage
    └── [user_id]/
        └── [bot_name]/
            ├── bot.py
            ├── requirements.txt
            ├── config.json
            └── SETUP.md
```

## Data Flow

### 1. User Input Collection
```
User → /start command
   ↓
Presents bot type options (8 categories)
   ↓
User selects type
   ↓
Asks for desired features
   ↓
User describes features
   ↓
Asks for customizations
   ↓
User provides customizations
```

### 2. AI Code Generation
```
Collected User Data → Prompt Construction
   ↓
Claude AI Processing
   ↓
JSON Response Parsing
   ↓
Bot Configuration Object
```

### 3. File Creation
```
Bot Config → Directory Structure Creation
   ↓
Write bot.py (main code)
Write requirements.txt (dependencies)
Write SETUP.md (instructions)
Write config.json (metadata)
   ↓
Return directory path
```

### 4. Response to User
```
Bot creation successful
   ↓
Display bot details
Show features implemented
Provide setup instructions
Offer next actions
```

## Key Technologies

### Libraries
- **python-telegram-bot**: Telegram API interface
- **anthropic**: Claude AI API client
- **python-dotenv**: Environment variable management

### External APIs
- **Telegram Bot API**: Bot communication
- **Anthropic API**: AI-powered code generation

## Security Considerations

1. **API Keys**
   - Stored in `.env` file (not committed)
   - Never logged or displayed
   - Validated before use

2. **User Data**
   - Isolated by user ID
   - Generated bots stored locally
   - No external data storage

3. **Code Generation**
   - Claude generates code, not directly executed
   - Code review recommended before use
   - Dependencies validated

## Error Handling

### 1. AI Response Errors
```python
try:
    bot_config = json.loads(response)
except json.JSONDecodeError:
    return error_message
```

### 2. File System Errors
```python
os.makedirs(bot_dir, exist_ok=True)
with open(file_path, 'w') as f:
    f.write(content)
```

### 3. API Errors
```python
try:
    response = client.messages.create(...)
except anthropic.APIError:
    handle_error()
```

## Performance

### Async Operations
- Uses async/await for non-blocking I/O
- Telegram updates processed concurrently
- File operations in separate tasks

### Optimization
- Bot configs cached in memory
- Minimal database usage
- Efficient prompt engineering

## Scalability

### Current Limitations
- Single-threaded Telegram polling
- Local file storage
- No distributed processing

### Future Improvements
- Webhook-based Telegram connection
- Cloud storage integration
- Message queue for concurrent generations
- Database for user history

## Testing

### Manual Testing Checklist
- [ ] Bot starts correctly
- [ ] All commands work
- [ ] Conversation flow is logical
- [ ] Generated code is valid Python
- [ ] Files created in correct locations
- [ ] API keys validated
- [ ] Error messages are helpful

### Automated Testing (Future)
```python
# Unit tests for BotFactory
# Integration tests for Telegram API
# API mock tests for Claude
```

## Deployment

### Local Development
```bash
python bot_factory.py
```

### Cloud Deployment (Recommended)
- Railway.app
- Heroku
- AWS Lambda + API Gateway
- Google Cloud Run
- DigitalOcean

### Environment Variables (Cloud)
```
TELEGRAM_BOT_TOKEN=xxx
ANTHROPIC_API_KEY=xxx
GENERATED_BOTS_PATH=/tmp/bots
```

## Monitoring

### Logging
```python
import logging
logging.basicConfig(level=logging.INFO)
```

### Metrics to Track
- Bots generated per user
- Generation success rate
- Average generation time
- Error frequency
- API usage

## Future Enhancements

1. **Web Interface**
   - HTML/CSS interface
   - Direct code download
   - Preview before generation

2. **Bot Deployment**
   - One-click deployment
   - Cloud integration
   - Hosting options

3. **Marketplace**
   - Share generated bots
   - Bot templates
   - Community contributions

4. **Advanced Features**
   - Multi-bot projects
   - Team collaboration
   - Version control
   - Testing framework generation

5. **AI Improvements**
   - Fine-tuned models
   - Custom prompt templates
   - Code quality scoring
   - Automated testing

## References

- [python-telegram-bot Docs](https://python-telegram-bot.readthedocs.io/)
- [Anthropic API Docs](https://docs.anthropic.com/)
- [Telegram Bot API](https://core.telegram.org/bots/api)
