from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from app.utils.texts import TEXTS

def get_quiz_keyboard(lang: str = "ru") -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton(text=TEXTS[lang]["btn_fake"], callback_data="quiz_fake"),
        InlineKeyboardButton(text=TEXTS[lang]["btn_real"], callback_data="quiz_real")
    )
    return keyboard

def get_next_keyboard(lang: str = "ru") -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        InlineKeyboardButton(text=TEXTS[lang]["btn_next"], callback_data="quiz_next"),
        InlineKeyboardButton(text=TEXTS[lang]["btn_menu"], callback_data="quiz_back")
    )
    return keyboard