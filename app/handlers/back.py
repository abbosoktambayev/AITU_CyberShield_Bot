from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext

from app.utils.texts import TEXTS
from app.keyboards.main_menu import get_main_menu


def register_back_handlers(dp: Dispatcher):

    @dp.message_handler(
        lambda m: m.text in [
            "🔙 Назад",
            "🔙 Артқа",
            "🔙 Orqaga",
            "🔙 Back",
        ]
    )
    async def back_to_menu(message: types.Message, state: FSMContext):
        data = await state.get_data()
        lang = data.get("lang", "ru")

        await message.answer(
            TEXTS[lang]["menu"],
            reply_markup=get_main_menu(lang)
        )
        await state.finish()