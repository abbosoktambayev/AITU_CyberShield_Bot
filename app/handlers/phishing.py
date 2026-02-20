import random
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext

from app.states.quiz import QuizStates
from app.keyboards.quiz import get_quiz_keyboard, get_next_keyboard
from app.keyboards.main_menu import get_main_menu
from app.utils.texts import TEXTS


def register_phishing_handlers(dp: Dispatcher):
    # ▶️ Старт квиза (ловим по эмодзи 🎣, чтобы работало на всех языках)
    @dp.message_handler(lambda m: "🎣" in m.text)
    async def start_quiz(message: types.Message, state: FSMContext):
        data = await state.get_data()
        lang = data.get("lang", "ru")

        questions = TEXTS[lang]["quiz_questions"].copy()
        random.shuffle(questions)

        await state.update_data(
            quiz_questions=questions,
            quiz_index=0,
            quiz_score=0,
        )

        await QuizStates.in_quiz.set()

        # ❗ убираем главное меню
        await message.answer(
            questions[0]["text"],
            reply_markup=types.ReplyKeyboardRemove()
        )

        # Передаем язык в текст и клавиатуру
        await message.answer(
            TEXTS[lang]["choose_option"],
            reply_markup=get_quiz_keyboard(lang)
        )

    # ✅ / ❌ Ответ
    @dp.callback_query_handler(
        lambda c: c.data in ["quiz_fake", "quiz_real"],
        state=QuizStates.in_quiz
    )
    async def answer(call: types.CallbackQuery, state: FSMContext):
        data = await state.get_data()
        lang = data.get("lang", "ru")

        idx = data["quiz_index"]
        question = data["quiz_questions"][idx]

        if call.data == f"quiz_{question['correct']}":
            await state.update_data(quiz_score=data["quiz_score"] + 1)
            text = TEXTS["quiz_answer"]["correct"][lang]
        else:
            text = TEXTS["quiz_answer"]["wrong"][lang]

        await call.message.answer(text, reply_markup=get_next_keyboard(lang))
        await call.answer()

    # ▶️ Следующий вопрос
    @dp.callback_query_handler(lambda c: c.data == "quiz_next", state=QuizStates.in_quiz)
    async def next_q(call: types.CallbackQuery, state: FSMContext):
        data = await state.get_data()
        lang = data.get("lang", "ru")

        idx = data["quiz_index"] + 1
        questions = data["quiz_questions"]

        if idx >= len(questions):
            score = data["quiz_score"]
            await state.finish()

            # Формируем финальный текст из словаря
            finish_text = TEXTS[lang]["test_finished"].format(score=score, total=len(questions))

            await call.message.answer(
                finish_text,
                reply_markup=get_main_menu(lang)
            )
            await call.answer()
            return

        await state.update_data(quiz_index=idx)
        await call.message.answer(
            questions[idx]["text"],
            reply_markup=get_quiz_keyboard(lang)
        )
        await call.answer()

    # ⬅️ В меню
    @dp.callback_query_handler(lambda c: c.data == "quiz_back", state=QuizStates.in_quiz)
    async def back(call: types.CallbackQuery, state: FSMContext):
        data = await state.get_data()
        lang = data.get("lang", "ru")

        await state.finish()
        await call.message.answer(
            TEXTS[lang]["menu"],
            reply_markup=get_main_menu(lang)
        )
        await call.answer()