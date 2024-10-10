from aiogram.types import Message, InlineKeyboardButton, CallbackQuery, InlineKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

menu = InlineKeyboardMarkup(inline_keyboard= [
        [InlineKeyboardButton(text = 'Обрати пральну машину', callback_data = 'choose_wm')],
        [InlineKeyboardButton(text = 'Повідомити про проблему з пралкою', callback_data = 'wm_problem')],
        [InlineKeyboardButton(text = "Додати відгук та зв'язок", callback_data = 'feedback')]
        ])

wm = InlineKeyboardMarkup(inline_keyboard= [ 
        [InlineKeyboardButton(text = '4 поверх 1 пралка', callback_data = '4f1wm')],
        [InlineKeyboardButton(text = '6 поверх 1 пралка', callback_data = '6f1wm')],
        [InlineKeyboardButton(text = '6 поверх 2 пралка', callback_data = '6f2wm')]])

set_wm = InlineKeyboardMarkup(inline_keyboard= [ 
        [InlineKeyboardButton(text = '1h', callback_data = '1h')],
        [InlineKeyboardButton(text = '1h 30m', callback_data = '1h30m')],
        [InlineKeyboardButton(text = '15m', callback_data = '15m')]])