from aiogram import types, Dispatcher

from create_bot import bot
from keyboards import keyboard
from config import USERS
import messages as msgs

from pool_req import get_act


async def command_start(message: types.Message):
    print(f'Press start button ID: {message.from_user.id}')
    await bot.send_message(message.from_user.id, msgs.hello_msg, reply_markup=keyboard)
    await message.delete()


async def get_actual(message: types.Message):
    print(f'Press button get_actual ID: {message.from_user.id}')
    if message.from_user.id in USERS:
        await bot.send_message(message.from_user.id, await get_act(), reply_markup=keyboard)
        await message.delete()
    else:
        await bot.send_message(message.from_user.id, msgs.not_user, reply_markup=keyboard)


async def unknown_command(message: types.Message):
    print(f'Press unknown button ID: {message.from_user.id}')
    await bot.send_message(message.from_user.id, msgs.unknown_msg, reply_markup=keyboard)
    await message.delete()


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(get_actual, commands=['get_actual'])
    # dp.register_message_handler(get_regular, commands=['get_regular', 'stop'])
    dp.register_message_handler(unknown_command)

