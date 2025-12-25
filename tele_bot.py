from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters, CommandHandler
from dotenv import load_dotenv
import os
from ai_agent import AIAgent



load_dotenv()
agent = AIAgent()



# Replace with your bot's token


# Replace with your chat ID (this is my group ID name is my automation team)

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID  = os.getenv("CHAT_ID")
# Define command handler


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text

    
    #AI Chat
    #ai_reply = AIAgent.ai_chat(agent2, user_text)
    ai_reply = agent.ai_chat(user_text)
    await update.message.reply_text(ai_reply)






# Main entry
app = ApplicationBuilder().token(BOT_TOKEN).build()

# Register commands

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))


app.run_polling()