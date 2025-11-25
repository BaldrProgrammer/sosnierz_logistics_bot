from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def get_main_keyboard():
    buttons = [
        [
            InlineKeyboardButton(text='Strona główna', callback_data='home'),
            InlineKeyboardButton(text='O nas', callback_data='about'),
            InlineKeyboardButton(text='Oferta', callback_data='offer'),
            InlineKeyboardButton(text='Kariera', callback_data='career'),
            InlineKeyboardButton(text='Kontakt', callback_data='contact'),
        ]
    ]
    return InlineKeyboardMarkup(
        inline_keyboard=buttons
    )
