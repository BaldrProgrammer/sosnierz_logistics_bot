from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from handlers import router

import os
import logging
import asyncio

env = load_dotenv()
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher()

try:
    logging.basicConfig(level=logging.INFO)
    dp.include_router(router)
    asyncio.run(dp.start_polling(bot))
except KeyboardInterrupt:
    print('end')
