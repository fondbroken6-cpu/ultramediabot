from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import Message
from fastapi import FastAPI, Request
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
import uvicorn
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)

dp = Dispatcher()
app = FastAPI()


# START
@dp.message(CommandStart())
async def start_handler(message: Message):
    text = """
🚀 <b>UltraMediaBot</b>

📥 TikTok, Instagram va YouTube videolarini yuklab oling
🎵 Musiqa qidiring va yuklab oling
🎧 Videolarni MP3 formatga aylantiring

📎 Link yuboring 👇
"""
    await message.answer(text)


# LINK HANDLER
@dp.message()
async def downloader(message: Message):
    url = message.text

    if "tiktok.com" in url:
        await message.answer("⏳ TikTok video yuklanmoqda...")
        
        # KEYIN API ULAYMIZ
        # Hozircha test
        
        await message.answer(
            "✅ TikTok link qabul qilindi.\nAPI keyin ulanadi 🚀"
        )

    elif "instagram.com" in url:
        await message.answer("📸 Instagram video yuklanmoqda...")

    elif "youtube.com" in url or "youtu.be" in url:
        await message.answer("▶️ YouTube video yuklanmoqda...")

    else:
        await message.answer(
            "❌ Linkni to‘g‘ri yuboring.\n\n"
            "TikTok / Instagram / YouTube link yuboring."
        )


# WEBHOOK
@app.post("/bot/{token}")
async def webhook(request: Request):
    data = await request.json()
    update = types.Update.model_validate(data)

    await dp.feed_update(bot, update)
    return {"ok": True}


# ROOT
@app.get("/")
async def root():
    return {"status": "UltraMediaBot ishlayapti 🚀"}


if __name__ == "main":
    uvicorn.run(app, host="0.0.0.0", port=10000)