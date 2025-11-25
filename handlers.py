from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from keyboards import get_main_keyboard

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer('Witaj!\nJesteśmy Sośnierz Logistic.\nW czym możemy pomóc?')
