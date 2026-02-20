from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from app.utils.texts import TEXTS


def get_phishing_keyboard(lang: str):
    kb = InlineKeyboardMarkup()
    kb.add(
        InlineKeyboardButton(TEXTS[lang]["quiz_fake"], callback_data="phish_fake"),
        InlineKeyboardButton(TEXTS[lang]["quiz_real"], callback_data="phish_real"),
    )
    return kb


def get_quiz_nav_keyboard(lang: str):
    kb = InlineKeyboardMarkup()
    kb.add(
        InlineKeyboardButton("➡️ Следующий вопрос", callback_data="quiz_next"),
        InlineKeyboardButton(TEXTS[lang]["back"], callback_data="quiz_back"),
    )
    return kb