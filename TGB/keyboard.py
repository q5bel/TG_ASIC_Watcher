from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


btn_1 = KeyboardButton('/antpool')
btn_2 = KeyboardButton('/emcd')

keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

keyboard.add(btn_1).add(btn_2)
