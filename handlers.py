from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery, FSInputFile, InputMediaPhoto
from keyboards import get_main_keyboard, write_or_back
from emailtest import send_email

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    keyboard = await get_main_keyboard()
    await message.answer_photo(photo=FSInputFile("media/home.png"),
                               caption='Witaj!\nJesteśmy Sośnierz Logistic.\nW czym możemy pomóc?',
                               reply_markup=keyboard)


@router.callback_query(F.data.startswith('about'))
async def contact(callback_data: CallbackQuery):
    keyboard = await write_or_back()
    with open('texts/about.txt', 'r', encoding='utf-8') as file:
        await callback_data.message.edit_media(
            media=InputMediaPhoto(
                media=FSInputFile("media/about.png"),
                caption=file.read()
            ),
            reply_markup=keyboard
        )


@router.callback_query(F.data.startswith('offer'))
async def contact(callback_data: CallbackQuery):
    keyboard = await write_or_back()
    with open('texts/oferta.txt', 'r', encoding='utf-8') as file:
        await callback_data.message.delete()
        await callback_data.message.answer(file.read(), reply_markup=keyboard)


@router.callback_query(F.data.startswith('career'))
async def contact(callback_data: CallbackQuery):
    keyboard = await write_or_back()
    with open('texts/career.txt', 'r', encoding='utf-8') as file:
        await callback_data.message.delete()
        await callback_data.message.answer(file.read(), reply_markup=keyboard)


@router.callback_query(F.data.startswith('contact'))
async def contact(callback_data: CallbackQuery):
    keyboard = await write_or_back()
    with open('texts/kontakt.txt', 'r', encoding='utf-8') as file:
        await callback_data.message.edit_media(
            media=InputMediaPhoto(
                media=FSInputFile("media/contact.png"),
                caption=file.read()
            ),
            reply_markup=keyboard
        )


@router.callback_query(F.data.startswith('home'))
async def contact(callback_data: CallbackQuery):
    keyboard = await get_main_keyboard()
    await callback_data.message.edit_media(
        media=InputMediaPhoto(
            media=FSInputFile("media/home.png"),
            caption="Witaj!\nJesteśmy Sośnierz Logistic.\nW czym możemy pomóc?"
        ),
        reply_markup=keyboard
    )


@router.callback_query(F.data.startswith('write'))
async def write(callback_data: CallbackQuery):
    send_email(
        smtp_host="smtp.gmail.com",
        smtp_port=465,
        username="sosnierzbot@gmail.com",
        password="nnsu nldw bgbb edjr",
        sender="sosnierzbot@gmail.com",
        to="boliklevik@gmail.com",
        subject="Тестовое письмо",
        body="Привет! Это письмо отправлено из Python."
    )

