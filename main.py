from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

import os
import logging
import asyncio

env = load_dotenv()
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher()

try:
    logging.basicConfig(level=logging.INFO)
    asyncio.run(dp.start_polling(bot))
except KeyboardInterrupt:
    print('end')
