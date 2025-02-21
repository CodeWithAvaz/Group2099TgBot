from aiogram.fsm.state import State, StatesGroup


class SherikState(StatesGroup):
    ism_familiya = State()
    texnologiya = State()
    aloqa = State()
    hudud = State()
    narx = State()
    kasb = State()
    murojat = State()
    maqsad = State()
    tekshir = State()


class UztozKerakState(StatesGroup):
    pass


class ShogirdKerakState(StatesGroup):
    pass


class HodimKerakState(StatesGroup):
    pass


class IShKerakState(StatesGroup):
    pass