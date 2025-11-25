from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from keyboards import get_main_keyboard

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    keyboard = await get_main_keyboard()
    await message.answer('Witaj!\nJesteśmy Sośnierz Logistic.\nW czym możemy pomóc?', reply_markup=keyboard)



@router.callback_query(F.data.startswith('contact'))
async def contact(callback_data: CallbackQuery):
    with open('texts/kontakt.txt', 'r', encoding='utf-8') as file:
        await callback_data.message.edit_text(file.read())
