from aiogram.types import Message, InlineKeyboardButton, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder

def menu_keyboard():
    kb = [
        [InlineKeyboardButton(text = 'Обрати пралку', callback_data = 'choose_wm')],
        [InlineKeyboardButton(text = 'Додати відгук', callback_data = 'add_fedback')]
    ]
    
    return kb