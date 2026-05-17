#!/usr/bin/env python3
"""
Bot Factory - AI-Powered Bot Generator
Creates custom bots on demand using Claude AI
Deployed on Railway
"""

import os
import json
import asyncio
import logging
from typing import Optional
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, ConversationHandler, CallbackQueryHandler
import anthropic

load_dotenv()

# Setup logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Environment variables
TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

if not TELEGRAM_TOKEN or not ANTHROPIC_API_KEY:
    raise ValueError(
        "Missing required environment variables!\n"
        "Please set TELEGRAM_BOT_TOKEN and ANTHROPIC_API_KEY"
    )

logger.info("✅ Configuration loaded successfully")

# Conversation states
ASKING_BOT_TYPE = 1
ASKING_FEATURES = 2
ASKING_CUSTOMIZATION = 3
GENERATING = 4

class BotFactory:
    def __init__(self):
        self.client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
        self.bot_configs = {}
        self.generated_bots = {}
        logger.info("🏭 BotFactory initialized")
        
    async def generate_bot_code(self, bot_type: str, features: str, customization: str, user_id: int) -> dict:
        """
        Uses Claude AI to generate complete bot code
        """
        logger.info(f"Generating {bot_type} bot for user {user_id}")
        
        prompt = f"""
You are an expert Python Telegram bot developer. Generate a complete, production-ready Telegram bot.

Bot Type: {bot_type}
Required Features: {features}
Customization Requests: {customization}

Provide a response in JSON format with the following structure:
{{
    "bot_name": "name_of_bot",
    "description": "brief description",
    "main_code": "complete bot.py code",
    "requirements": "list of pip packages needed",
    "setup_instructions": "step by step setup guide",
    "commands": "list of available commands",
    "features_implemented": "list of implemented features"
}}

Make the code:
- Production-ready and well-documented
- Include error handling
- Have at least 5-10 useful commands
- Be well-structured with classes and functions
- Include docstrings
- Handle edge cases

Ensure the JSON is valid and the code is complete.
        """
        
        try:
            response = self.client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=4000,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            
            response_text = response.content[0].text
            
            # Extract JSON from response
            json_start = response_text.find("{")
            json_end = response_text.rfind("}") + 1
            json_str = response_text[json_start:json_end]
            bot_config = json.loads(json_str)
            bot_config['user_id'] = user_id
            
            logger.info(f"✅ Bot code generated successfully: {bot_config.get('bot_name')}")
            return bot_config
        except json.JSONDecodeError as e:
            logger.error(f"JSON parse error: {e}")
            return {
                "error": "Failed to parse AI response",
                "raw_response": response_text[:500]
            }
        except Exception as e:
            logger.error(f"Generation error: {e}")
            return {
                "error": str(e)
            }
    
    async def create_bot_files(self, bot_config: dict, user_id: int) -> str:
        """
        Creates bot files in a directory
        """
        bot_name = bot_config.get('bot_name', 'custom_bot').replace(' ', '_').lower()
        bot_dir = f"generated_bots/{user_id}/{bot_name}"
        
        try:
            os.makedirs(bot_dir, exist_ok=True)
            
            # Save main bot code
            with open(f"{bot_dir}/bot.py", "w") as f:
                f.write(bot_config.get('main_code', ''))
            
            # Save requirements
            with open(f"{bot_dir}/requirements.txt", "w") as f:
                f.write(bot_config.get('requirements', 'python-telegram-bot\nrequests\npython-dotenv'))
            
            # Save setup instructions
            with open(f"{bot_dir}/SETUP.md", "w") as f:
                f.write(f"# {bot_config.get('bot_name', 'Custom Bot')} Setup\n\n")
                f.write(bot_config.get('setup_instructions', ''))
                f.write("\n\n## Commands\n")
                f.write(bot_config.get('commands', ''))
            
            # Save config
            with open(f"{bot_dir}/config.json", "w") as f:
                json.dump(bot_config, f, indent=2)
            
            logger.info(f"Bot files created at: {bot_dir}")
            return bot_dir
        except Exception as e:
            logger.error(f"File creation error: {e}")
            return ""


bot_factory = BotFactory()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Start the bot creation process"""
    logger.info(f"User {update.effective_user.id} started bot creation")
    
    keyboard = [
        [InlineKeyboardButton("🎮 Gaming Bot", callback_data="type_gaming")],
        [InlineKeyboardButton("📚 Educational Bot", callback_data="type_education")],
        [InlineKeyboardButton("💼 Business Bot", callback_data="type_business")],
        [InlineKeyboardButton("🎨 Creative Bot", callback_data="type_creative")],
        [InlineKeyboardButton("🤖 AI Assistant", callback_data="type_ai")],
        [InlineKeyboardButton("🎵 Music Bot", callback_data="type_music")],
        [InlineKeyboardButton("📊 Data Bot", callback_data="type_data")],
        [InlineKeyboardButton("✏️ Custom Bot", callback_data="type_custom")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "🚀 Welcome to Bot Factory!\n\n"
        "I'm an AI-powered bot generator. I can create any Telegram bot you can imagine.\n\n"
        "What type of bot would you like me to create?",
        reply_markup=reply_markup
    )
    return ASKING_BOT_TYPE


async def handle_bot_type(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Handle bot type selection"""
    query = update.callback_query
    await query.answer()
    
    bot_type = query.data.replace("type_", "").title()
    context.user_data['bot_type'] = bot_type
    
    logger.info(f"User {update.effective_user.id} selected: {bot_type}")
    
    await query.edit_message_text(
        text=f"✅ You selected: {bot_type} Bot\n\n"
             f"Now, what specific features do you want? (e.g., 'chat, image processing, user profiles')"
    )
    
    return ASKING_FEATURES


async def handle_features(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Get desired features"""
    context.user_data['features'] = update.message.text
    
    logger.info(f"User {update.effective_user.id} features: {update.message.text[:100]}")
    
    await update.message.reply_text(
        "Great! Any specific customizations or requirements?\n"
        "(e.g., 'multilingual, fast response, database integration') or just type 'none'"
    )
    
    return ASKING_CUSTOMIZATION


async def handle_customization(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Get customization requirements and generate bot"""
    context.user_data['customization'] = update.message.text
    
    logger.info(f"User {update.effective_user.id} customization: {update.message.text[:100]}")
    
    # Show generating message
    generating_msg = await update.message.reply_text(
        "🤖 AI is thinking... Creating your custom bot from scratch...\n"
        "This may take a moment..."
    )
    
    try:
        # Generate bot code using Claude AI
        bot_config = await bot_factory.generate_bot_code(
            context.user_data['bot_type'],
            context.user_data['features'],
            context.user_data['customization'],
            update.effective_user.id
        )
        
        if 'error' in bot_config:
            await generating_msg.edit_text(
                f"❌ Error: {bot_config['error']}\n\nPlease try again."
            )
            return ConversationHandler.END
        
        # Create bot files
        bot_dir = await bot_factory.create_bot_files(bot_config, update.effective_user.id)
        
        if not bot_dir:
            await generating_msg.edit_text("❌ Failed to create bot files.")
            return ConversationHandler.END
        
        # Prepare response
        response = (
            f"✅ Bot Created Successfully!\n\n"
            f"📝 Bot Name: {bot_config.get('bot_name', 'Custom Bot')}\n"
            f"📄 Description: {bot_config.get('description', 'N/A')[:100]}\n\n"
            f"🎯 Features Implemented:\n"
        )
        
        features_list = bot_config.get('features_implemented', 'N/A')
        if isinstance(features_list, str):
            response += features_list[:500]
        else:
            response += "\n".join(f"  • {f}" for f in features_list[:10])
        
        response += f"\n\n🛠️ Setup Instructions:\n{bot_config.get('setup_instructions', 'N/A')[:300]}...\n\n"
        response += f"📂 Bot files saved!\n"
        response += "\n✨ Your bot is ready to deploy!"
        
        await generating_msg.edit_text(response, parse_mode="Markdown")
        
        # Store generated bot config
        bot_factory.generated_bots[update.effective_user.id] = bot_config
        
        keyboard = [
            [InlineKeyboardButton("🚀 Create Another Bot", callback_data="start_over")],
            [InlineKeyboardButton("📖 View Full Code", callback_data="view_code")],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await update.message.reply_text(
            "What would you like to do next?",
            reply_markup=reply_markup
        )
        
    except Exception as e:
        logger.error(f"Generation failed: {e}")
        await generating_msg.edit_text(f"❌ Error generating bot: {str(e)[:200]}")
    
    return ConversationHandler.END


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Show help information"""
    help_text = (
        "🤖 Bot Factory Help\n\n"
        "I can create any Telegram bot you want using AI!\n\n"
        "Available Bot Types:\n"
        "  • 🎮 Gaming Bots - Trivia, word games, etc\n"
        "  • 📚 Educational Bots - Learning tools, quizzes\n"
        "  • 💼 Business Bots - CRM, scheduling, analytics\n"
        "  • 🎨 Creative Bots - Image generation, design tools\n"
        "  • 🤖 AI Assistants - Chat, translation, summarization\n"
        "  • 🎵 Music Bots - Playlist management, recommendations\n"
        "  • 📊 Data Bots - Analytics, reporting, dashboards\n"
        "  • ✏️ Custom Bots - Anything else you can imagine!\n\n"
        "Commands:\n"
        "  /start - Begin creating a bot\n"
        "  /help - Show this help message\n"
        "  /examples - See example bots\n"
    )
    await update.message.reply_text(help_text)


async def examples_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Show example bots that can be created"""
    examples = (
        "📋 Example Bots I Can Create:\n\n"
        "🎮 Gaming Examples:\n"
        "  • Wordle game bot\n"
        "  • 20 questions game\n"
        "  • Chess multiplayer bot\n\n"
        "🤖 AI Examples:\n"
        "  • ChatGPT-like assistant\n"
        "  • Code review bot\n"
        "  • Translation bot\n\n"
        "💼 Business Examples:\n"
        "  • Task management bot\n"
        "  • Invoice generator\n"
        "  • Appointment scheduler\n\n"
        "📚 Educational Examples:\n"
        "  • Language learning bot\n"
        "  • Daily quote bot\n"
        "  • Quiz master bot\n\n"
        "Use /start to create your own!"
    )
    await update.message.reply_text(examples)


async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Handle button callbacks"""
    query = update.callback_query
    await query.answer()
    
    if query.data == "start_over":
        await query.delete_message()
        await start(update, context)
        return ASKING_BOT_TYPE
    elif query.data == "view_code":
        user_id = update.effective_user.id
        if user_id in bot_factory.generated_bots:
            bot_config = bot_factory.generated_bots[user_id]
            code = bot_config.get('main_code', 'Code not available')[:2000]
            await query.message.reply_text(
                f"📝 Generated Bot Code:\n\n```python\n{code}\n...\n```",
                parse_mode="Markdown"
            )
        return ConversationHandler.END
    
    # Handle bot type selection
    if query.data.startswith("type_"):
        return await handle_bot_type(update, context)
    
    return ConversationHandler.END


async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle errors"""
    logger.error(f'Update {update} caused error {context.error}')


def main() -> None:
    """Start the bot"""
    logger.info("🚀 Starting Bot Factory...")
    logger.info(f"Token loaded: {TELEGRAM_TOKEN[:20]}...")
    
    # Create application
    application = Application.builder().token(TELEGRAM_TOKEN).build()
    
    # Create conversation handler
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            ASKING_BOT_TYPE: [
                CommandHandler("start", start),
                CallbackQueryHandler(handle_bot_type),
            ],
            ASKING_FEATURES: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, handle_features),
            ],
            ASKING_CUSTOMIZATION: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, handle_customization),
            ],
        },
        fallbacks=[CommandHandler("start", start)],
    )
    
    # Add handlers
    application.add_handler(conv_handler)
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("examples", examples_command))
    application.add_handler(CallbackQueryHandler(button_callback))
    application.add_error_handler(error_handler)
    
    # Start bot
    logger.info("✅ Bot Factory is running...")
    print("\n" + "="*50)
    print("🏭 BOT FACTORY IS LIVE!")
    print("="*50)
    print("Waiting for messages...\n")
    
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
