from aiogram.types import ReplyKeyboardMarkup


def get_main_menu(lang: str) -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)

    if lang == "ru":
        kb.add("🔐 Проверка пароля")
        kb.add("🎣 Фишинг-тест")
        kb.add("🆘 SOS")
    elif lang == "kz":
        kb.add("🔐 Құпиясөзді тексеру")
        kb.add("🎣 Фишинг-тест")
        kb.add("🆘 SOS")
    elif lang == "uz":
        kb.add("🔐 Parolni tekshirish")
        kb.add("🎣 Phishing test")
        kb.add("🆘 SOS")
    else:  # en
        kb.add("🔐 Check password")
        kb.add("🎣 Phishing quiz")
        kb.add("🆘 SOS")

    return kb