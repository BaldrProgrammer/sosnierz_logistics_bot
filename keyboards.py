from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def get_main_keyboard():
    buttons = [
        [
            InlineKeyboardButton(text='Strona główna'),
            InlineKeyboardButton(text='O nas'),
            InlineKeyboardButton(text='Oferta'),
            InlineKeyboardButton(text='Kariera'),
            InlineKeyboardButton(text='Kontakt'),
        ]
    ]
    return InlineKeyboardMarkup(
        inline_keyboard=buttons
    )
