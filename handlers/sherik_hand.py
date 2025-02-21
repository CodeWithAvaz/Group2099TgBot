from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext


from states.state_menu import SherikState

sherik_router = Router()


@sherik_router.message(F.text == "Sherik kerak")
async def start_sherik(msg: Message, state: FSMContext):
    await msg.answer("Ism, familiyangizni kiriting?")
    await state.set_state(SherikState.ism_familiya)


@sherik_router.message(SherikState.ism_familiya)
async def get_name(msg: Message, state: FSMContext):
    await state.update_data(ism_familiya=msg.text)
    data = """
📚 Texnologiya:

Talab qilinadigan texnologiyalarni kiriting?
Texnologiya nomlarini vergul bilan ajrating. Masalan, 

Java, C++, C#

"""
    await msg.answer(data)
    await state.set_state(SherikState.texnologiya)
