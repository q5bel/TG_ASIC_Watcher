from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


btn_1 = KeyboardButton('/antpool_subscribe')
btn_2 = KeyboardButton('/emcd_subscribe')
btn_3 = KeyboardButton('/antpool_unsubscribe')
btn_4 = KeyboardButton('/emcd_unsubscribe')

keyboard = ReplyKeyboardMarkup(resize_keyboard=True)


keyboard.row(btn_1, btn_2)
keyboard.row(btn_3, btn_4)


