from aiogram import Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardButton, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
from core_functions import menu_keyboard

dp = Dispatcher()

@dp.message(CommandStart())
async def start_command(message: Message):
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text = 'Меню',
        callback_data='menu'
    ))
    await message.answer("""
                         Вітаємо у боті, для продовження натисність кнопку меню 
                         """,
                         reply_markup = builder.as_markup()
                         )
                         


@dp.callback_query(F.data == 'menu')
async def menu_handler(message: Message, callback_query: CallbackQuery):
    await message.answer("""
                         Виберіть подальшу дію:
                         """, reply_markup = menu_keyboard()
                         )
    


