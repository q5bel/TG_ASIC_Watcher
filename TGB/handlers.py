from aiogram import types, Dispatcher

from start_bot import bot
from keyboard import keyboard
import messages

from API.antpool import ant_request
from API.emcd import emcd_request


async def antpool_request(message: types.Message):
    await bot.send_message(message.from_user.id, ant_request(), reply_markup=keyboard)


async def emcdpool_request(message: types.Message):
    await bot.send_message(message.from_user.id, emcd_request(), reply_markup=keyboard)


async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, messages.hello_msg, reply_markup=keyboard)


async def unknown_command(message: types.Message):
    await bot.send_message(message.from_user.id, messages.unknown_msg, reply_markup=keyboard)


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(antpool_request, commands=['antpool'])
    dp.register_message_handler(emcdpool_request, commands=['emcd'])
    dp.register_message_handler(unknown_command)
