from aiogram.dispatcher.filters.state import State, StatesGroup


class PasswordStates(StatesGroup):
    waiting_for_password = State()