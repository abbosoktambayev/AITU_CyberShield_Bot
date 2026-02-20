from aiogram.types import ReplyKeyboardMarkup


def get_language_keyboard():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add("🇷🇺 Русский", "🇰🇿 Қазақша")
    kb.add("🇺🇿 O'zbekcha", "🇬🇧 English")
    return kb