import os
from app.handlers.password import register_password_handlers
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from app.keyboards.language import get_language_keyboard
from app.handlers.language import register_language_handlers
from app.handlers.phishing import register_phishing_handlers
from app.handlers.sos import register_sos_handlers
from app.handlers.back import register_back_handlers

from app.utils.texts import TEXTS

load_dotenv()

API_TOKEN = os.getenv("BOT_TOKEN")
if not API_TOKEN:
    raise RuntimeError("BOT_TOKEN not found")

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
register_phishing_handlers(dp)
register_password_handlers(dp)
register_language_handlers(dp)
register_sos_handlers(dp)
register_back_handlers(dp)


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer(
        TEXTS["ru"]["start"],
        reply_markup=get_language_keyboard()
    )


if __name__ == "__main__":
    print("Bot started")
    executor.start_polling(dp, skip_updates=True)