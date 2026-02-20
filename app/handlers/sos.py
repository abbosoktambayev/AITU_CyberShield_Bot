from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext

from app.utils.texts import TEXTS
from app.keyboards.sos import get_sos_keyboard
from app.keyboards.main_menu import get_main_menu


def register_sos_handlers(dp: Dispatcher):

    @dp.message_handler(lambda m: "SOS" in m.text)
    async def sos(message: types.Message, state: FSMContext):
        data = await state.get_data()
        lang = data.get("lang", "ru")

        await message.answer(
            TEXTS[lang]["sos_question"],
            reply_markup=get_sos_keyboard(lang)
        )

    @dp.message_handler(lambda m: m.text in [
        TEXTS["ru"]["sos_account"],
        TEXTS["kz"]["sos_account"],
        TEXTS["uz"]["sos_account"],
        TEXTS["en"]["sos_account"],
    ])
    async def sos_account(message: types.Message, state: FSMContext):
        data = await state.get_data()
        lang = data.get("lang", "ru")

        await message.answer(
            TEXTS[lang]["sos_account_text"],
            reply_markup=get_main_menu(lang)
        )

    @dp.message_handler(lambda m: m.text in [
        TEXTS["ru"]["sos_money"],
        TEXTS["kz"]["sos_money"],
        TEXTS["uz"]["sos_money"],
        TEXTS["en"]["sos_money"],
    ])
    async def sos_money(message: types.Message, state: FSMContext):
        data = await state.get_data()
        lang = data.get("lang", "ru")

        await message.answer(
            TEXTS[lang]["sos_money_text"],
            reply_markup=get_main_menu(lang)
        )