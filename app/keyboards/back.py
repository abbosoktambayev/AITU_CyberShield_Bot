from aiogram.types import ReplyKeyboardMarkup
from app.utils.texts import TEXTS


def get_back_keyboard(lang: str):
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(TEXTS[lang]["back"])
    return kb