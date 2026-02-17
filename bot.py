import time
import random
from telegram import Bot

TOKEN = "YOUR_REAL_BOT_TOKEN"
CHAT_ID = "-1003870214565"

bot = Bot(token=TOKEN)

messages = [
    "💻 New online job opportunity posted!",
    "🔥 Earn from home using your phone.",
    "📌 Daily online job updates available.",
    "🚀 Start earning online today!"
]

while True:
    message = random.choice(messages)
    bot.send_message(chat_id=CHAT_ID, text=message)
    time.sleep(600)
