import asyncio
from datetime import datetime
import pytz
from telegram import Bot
import random

BOT_TOKEN = "8880293130:AAHnQStWb4kqEAlhokJqVfVjUt2AwWsrOEc"
CHAT_ID = "-1003875136588"
TIMEZONE = "Asia/Kolkata"

MESSAGES = [
    "乛٭ＫＡＳＩＭ Madarchod randi, teri chut mein lund daal ke chod dunga",
    "乛٭ＫＡＳＩＭ Behenchod sali, teri maa ki chut aur teri gaand dono marunga",
    "乛٭ＫＡＳＩＭ Chutiya ladki, teri fuddi mein mera lawda ghusa ke rakh dunga",
    "乛٭ＫＡＳＩＭ Gandu randi, teri behan ki tarah gaand marwa",
    "乛٭ＫＡＳＩＭ Madarchod kaminey, teri maa chod ke tujhe paida kiya tha kya?",
    "乛٭ＫＡＳＩＭ Behenchod harami, teri chut faad ke rakh dunga",
    "乛٭ＫＡＳＩＭ Randi ki beti, teri gaand mein lund daal ke chillana",
    "乛٭ＫＡＳＩＭ Chutmarike, teri fuddi ko mera baap chodta tha",
    "乛٭ＫＡＳＩＭ Bhosdiki ladki, teri maa aur behen dono ki chut mein muh daal",
    "乛٭ＫＡＳＩＭ Madarchod sali, teri chut ke baal kaat ke khelunga",
    "乛٭ＫＡＳＩＭ Behenchod gandu, tujhe doggy style mein chod ke rone dunga",
    "乛٭ＫＡＳＩＭ Lawdi randi, teri gaand faad dunga itna ki baith na paye",
    "乛٭ＫＡＳＩＭ Kaminey chutiya, teri maa ki fuddi se nikal ke aayi hai tu",
    "乛٭ＫＡＳＩＭ Harami behenchod, teri chut mein thook ke chodunga",
    "乛٭ＫＡＳＩＭ Madarchod ladki, teri behan ko bhi saath mein le lunga",
    "乛٭ＫＡＳＩＭ Madarchod ladki, teri behan ko bhi saath mein le lunga",
    "乛٭ＫＡＳＩＭ Bhosdike randi, teri gaand mein mera pura lund pel dunga",
    "乛٭ＫＡＳＩＭ Chut ke dhakkan, teri maa chod ke tujhe paida kiya",
    "乛٭ＫＡＳＩＭ Gandmara sali, teri fuddi ko roz chodne aayunga",
    "乛٭ＫＡＳＩＭ Randi ka maal, teri chut aur gaand dono ki seva karunga"
]

async def send_messages():

    bot = Bot(token=BOT_TOKEN)

    while True:

        try:

            tz = pytz.timezone(TIMEZONE)
            now = datetime.now(tz)

            date_str = now.strftime("%d %B %Y - %I:%M:%S %p")

            message = random.choice(MESSAGES)

            full_message = f"{message}\n\n📅 {date_str}"

            await bot.send_message(
                chat_id=CHAT_ID,
                text=full_message
            )

            print("✅ Message bhej diya!")
            print(full_message)

        except Exception as e:
            print(f"❌ Error: {e}")

        # 20 second wait
        await asyncio.sleep(20)

print("🚀 Bot start ho gaya! Har 20 second mein message jayega...")

asyncio.run(send_messages())