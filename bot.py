import time
import random
import os
from telegram import Bot, __version__ as ptb_version

TOKEN = os.environ.get("BOT_TOKEN")  # your token from Render environment variable
CHAT_ID = "-1003870214565"

bot = Bot(token=TOKEN)

messages = [
"💻 Don’t wait! A brand-new online job has just been posted! Start earning from home today and take control of your income!",

"🔥 Looking for a legit way to make money from your phone? Check out this online job opportunity and start earning immediately!",

"🚀 Why wait for payday? Launch your online side hustle today and watch your earnings grow with just a few simple tasks!",

"📌 Daily online jobs are here! Grab the best opportunities before they disappear — your chance to earn extra cash is now!",

"🏠 Work from the comfort of your home and make money on your schedule! Flexible online jobs are waiting for you!",

"💰 Don’t miss out on this opportunity! Start working remotely today and boost your monthly income without leaving your house!",

"📱 Earn money online with just your smartphone or laptop! Quick, simple, and reliable ways to make extra income are here!",

"🌟 Attention beginners! These top online jobs are perfect to start your journey to financial freedom. Don’t wait — start now!",

"💡 Want fast money online? Try these easy gigs that pay instantly and require minimal experience — perfect for beginners!",

"✨ Remote work just got easier! Grab today’s best online jobs and start earning from anywhere in the world right now!",

"📈 Increase your income with flexible online jobs! Work when you want, from wherever you want, and get paid reliably!",

"🖥️ Simple online tasks that anyone can do! Complete them today and see how quickly your earnings add up!",

"🔔 Hot new online jobs are live! Check today’s opportunities and start earning remotely without any hassle!",

"🎯 Earn money while learning! These online jobs help you build skills and get paid at the same time — double benefit!",

"💸 Get paid daily for completing online work! Flexible, beginner-friendly opportunities are available now — don’t miss out!",

"🏆 This week’s best online jobs are here! Work from home, earn extra income, and take advantage of these top opportunities!",

"📤 Submit tasks online and get paid instantly! Perfect for students, freelancers, or anyone looking for extra income!",

"💎 Exclusive online jobs for our subscribers! Be among the first to grab high-paying, trusted remote tasks today!",

"🌐 Work remotely and grow your income fast! Flexible online jobs let you earn on your terms without leaving home!",

"💬 Share these online jobs with your friends! Everyone deserves the chance to earn extra money from home!",

"✍️ Complete easy online tasks and earn cash! These beginner-friendly jobs are perfect for anyone looking to start earning quickly!",

"📊 Make extra income online by completing simple jobs anyone can do! Start today and watch your earnings grow steadily!",

"🌟 Step up your online earning game! Flexible remote jobs pay well for your efforts and fit perfectly into your schedule!",

"🎉 Fun online jobs that pay you to work from home! Enjoy completing tasks while earning reliable extra income!",

"📌 Don’t wait — grab today’s remote work opportunities! Online jobs fill up fast, so act now and secure your spot!",

"🚀 Work online and take control of your financial freedom! Flexible jobs let you earn without strict schedules or commute!",

"🏠 Flexible home-based jobs are available now! Work at your own pace, make money easily, and enjoy full freedom!",

"💡 Quick ways to earn money online today! Start small, grow your skills, and steadily increase your income without stress!",

"🔥 Hot online jobs are live now! Perfect for anyone looking to earn extra cash safely, quickly, and reliably!",

"💰 Start earning online in minutes! Beginner-friendly, flexible, and reliable tasks are ready for you — don’t miss out!",

"🌟 Incredible online opportunities are waiting! Work from home, earn extra income, and enjoy full flexibility today!"
]

while True:
    message = random.choice(messages)
    bot.send_message(chat_id=CHAT_ID, text=message)
    time.sleep(600)
