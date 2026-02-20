from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from app.utils.texts import TEXTS


def get_sos_keyboard(lang: str):
    kb = ReplyKeyboardMarkup(resize_keyboard=True)

    kb.add(
        KeyboardButton(TEXTS[lang]["sos_account"]),
        KeyboardButton(TEXTS[lang]["sos_money"]),
    )
    kb.add(
        KeyboardButton(TEXTS[lang]["back"])
    )

    return kb