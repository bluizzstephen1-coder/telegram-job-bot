import time
import random
import os
from telegram import Bot, __version__ as ptb_version

TOKEN = os.environ.get("BOT_TOKEN")  # your token from Render environment variable
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
