from aiogram import Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardButton, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
import keyboards as kb
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup 
from aiogram.filters import StateFilter

dp = Dispatcher()

class Form(StatesGroup):
    start_washing = State()
    end_washing = State()


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
async def menu_handler(callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer('Виберіть подальшу дію:', reply_markup = kb.menu)

@dp.callback_query(F.data == 'choose_wm')
async def choose_wm_handler(callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer('Виберіть пральну машину:', reply_markup =kb.wm)
    
@dp.callback_query(F.data == '4f1p')
async def set_4f1p(callback_query: CallbackQuery, state: FSMContext):
    await state.set_state(Form.start_washing)
    await callback_query.message.answer('Введіть час початку прання:')
    await callback_query.answer()

@dp.message(StateFilter(Form.start_washing))
async def set_4f1p_processing(message: Message, state: FSMContext):
    start_washing = message.text
    await message.answer(f"Час початку прання встановлено: {start_washing}")
    await state.clear()

@dp.callback_query(F.data == '6f1p')
async def set_4f1p(callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer('Введіть час початку прання:', reply_markup = kb.set_wm)

@dp.callback_query(F.data == '6f2p')
async def set_4f1p(callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer('Введіть час початку прання:', reply_markup = kb.set_wm)

