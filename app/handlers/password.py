import re
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext

from app.utils.texts import TEXTS
from app.states.password import PasswordStates
from app.keyboards.back import get_back_keyboard
from app.keyboards.main_menu import get_main_menu


def register_password_handlers(dp: Dispatcher):

    @dp.message_handler(
        lambda message: message.text in [
            "🔐 Проверка пароля",
            "🔐 Құпиясөзді тексеру",
            "🔐 Parolni tekshirish",
            "🔐 Check password",
        ]
    )
    async def password_start(message: types.Message, state: FSMContext):
        # 👉 ЗДЕСЬ ПОЛУЧАЕМ ЯЗЫК
        data = await state.get_data()
        lang = data.get("lang", "ru")

        await PasswordStates.waiting_for_password.set()
        await message.answer(
            TEXTS[lang]["ask_password"],
            reply_markup=get_back_keyboard(lang)
        )
    @dp.message_handler(state=PasswordStates.waiting_for_password)
    async def password_process(message: types.Message, state: FSMContext):
        # 👉 И ЗДЕСЬ ТОЖЕ ПОЛУЧАЕМ ЯЗЫК
        data = await state.get_data()
        lang = data.get("lang", "ru")

        password = message.text

        if message.text == TEXTS[lang]["back"]:
            await message.answer(
                TEXTS[lang]["menu"],
                reply_markup=get_main_menu(lang)
            )
            await state.reset_state(with_data=False)
            return

        score = 0
        if len(password) >= 8:
            score += 1
        if re.search(r"\d", password):
            score += 1
        if re.search(r"[A-Z]", password):
            score += 1
        if re.search(r"[!@#$%^&*]", password):
            score += 1

        if score <= 1:
            result = {
                "ru": "❌ Очень слабый пароль",
                "kz": "❌ Өте әлсіз құпиясөз",
                "uz": "❌ Juda kuchsiz parol",
                "en": "❌ Very weak password",
            }[lang]
        elif score == 2:
            result = {
                "ru": "⚠️ Средний пароль",
                "kz": "⚠️ Орташа құпиясөз",
                "uz": "⚠️ O‘rtacha parol",
                "en": "⚠️ Medium password",
            }[lang]
        else:
            result = {
                "ru": "✅ Надёжный пароль",
                "kz": "✅ Мықты құпиясөз",
                "uz": "✅ Kuchli parol",
                "en": "✅ Strong password",
            }[lang]

        await message.answer(result)
        await message.answer(
            TEXTS[lang]["menu"],
            reply_markup=get_main_menu(lang)
        )
        await state.reset_state(with_data=False)