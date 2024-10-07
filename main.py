import aiogram
import asyncio
from aiogram import Bot
from handlers import dp

bot = Bot(token = '7729651316:AAGhuO1Pv024FNWhv3fwOX1fnXU4_pn5TS8')

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())