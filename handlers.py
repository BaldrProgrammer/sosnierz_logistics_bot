from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery, FSInputFile, InputMediaPhoto, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from keyboards import get_main_keyboard, write_or_back, back_keyboard
from emailtest import send_email

router = Router()


class FSMForm(StatesGroup):
    name: str = State()
    email: str = State()
    number: str = State()
    theme: str = State()
    text: str = State()


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
async def write_fsm_name(callback_data: CallbackQuery, state: FSMContext):
    await state.set_state(FSMForm.name)
    await callback_data.message.edit_text('Proszę o wprowadzenie swojego imienia')


@router.message(FSMForm.name)
async def write_fsm_email(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(FSMForm.email)
    await message.answer('Proszę podać swój e-mail')


@router.message(FSMForm.email)
async def write_fsm_number(message: Message, state: FSMContext):
    await state.update_data(email=message.text)
    button_phone = KeyboardButton(text='Wyślij numer', request_contact=True)
    keyboard = ReplyKeyboardMarkup(
        keyboard=[[button_phone]],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    await state.set_state(FSMForm.number)
    await message.answer('Proszę podać swój numer telefonu', reply_markup=keyboard)


@router.message(F.contact)
async def write_fsm_theme(message: Message, state: FSMContext):
    await state.update_data(number=message.contact.phone_number)
    await state.set_state(FSMForm.theme)
    await message.answer('Proszę podać temat zgłoszenia', reply_markup=ReplyKeyboardRemove())


@router.message(FSMForm.theme)
async def write_fsm_text(message: Message, state: FSMContext):
    await state.update_data(theme=message.text)
    await state.set_state(FSMForm.text)
    await message.answer('I treść zgłoszenia')


@router.message(FSMForm.text)
async def write_email(message: Message, state: FSMContext):
    await state.update_data(text=message.text)
    data = await state.get_data()
    tresc = f'''
Człowiek o imieniu {data['name']} zgłosił się do bota Telegram Sośnierz.

Temat zgłoszenia:
{data['theme']}
    
Treść zgłoszenia:
{data['text']}
    
---
Dane kontaktowe:
Numer telefonu: {data['number']}
Adres e-mail: {data['email']}
'''
    send_email(
        smtp_host="smtp.gmail.com",
        smtp_port=465,
        username="sosnierzbot@gmail.com",
        password="nnsu nldw bgbb edjr",
        sender="sosnierzbot@gmail.com",
        to="boliklevik@gmail.com",
        subject=f"OTRZYMANO ZGŁOSZENIE PRZEZ TELEGRAM OD {data['name']}",
        body=tresc
    )

    keyboard = await back_keyboard()
    await message.answer_photo(photo=FSInputFile("media/tresc_wyslana.png"),
                               caption='Zgłoszenie zostało wysłane do naszego personelu. Proszę oczekiwać odpowiedzi telefonicznie lub mailowo.',
                               reply_markup=keyboard)
