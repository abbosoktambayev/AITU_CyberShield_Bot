from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext

from app.utils.texts import TEXTS
from app.keyboards.main_menu import get_main_menu


def register_language_handlers(dp: Dispatcher):

    @dp.message_handler(
        lambda message: message.text in [
            "🇷🇺 Русский",
            "🇰🇿 Қазақша",
            "🇺🇿 O'zbekcha",
            "🇬🇧 English",
        ]
    )
    async def set_language(message: types.Message, state: FSMContext):
        if "Рус" in message.text:
            lang = "ru"
        elif "Қазақ" in message.text:
            lang = "kz"
        elif "O'zbek" in message.text:
            lang = "uz"
        else:
            lang = "en"

        await state.update_data(lang=lang)
        await message.answer(
            TEXTS[lang]["menu"],
            reply_markup=get_main_menu(lang)
        )