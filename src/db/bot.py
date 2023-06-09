import asyncio
from aiogram import Bot, Dispatcher, executor

from config import BOT_TOKEN

loop= asyncio.new_event_loop()
bot=Bot(BOT_TOKEN, parse_mode="HTML")
db = Dispatcher(bot,loop=loop)

if __name__ == '__main__':
    from handler import db
    executor.start_polling(db)