import asyncio
import logging

from services.button import router
from services.config import Token


from aiogram import Bot, Dispatcher
from aiogram.client.bot import DefaultBotProperties

bot=Bot(Token, default=DefaultBotProperties(parse_mode="HTML"))
dp=Dispatcher()


async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__=="__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')