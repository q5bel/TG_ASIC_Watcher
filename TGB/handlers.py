from aiogram import types, Dispatcher
from asyncio import sleep

from TGB.create_bot import bot
from keyboard import keyboard
import TGB.messages as msgs

from API.antpool import ant_request
from API.emcd import emcd_request

users_id = (
    1236837656, # @asicgarant
    229051322, # @q5bel
    1286337392, # булыгин
)


async def command_start(message: types.Message):
    print(f'Press start button ID: {message.from_user.id}')
    await bot.send_message(message.from_user.id, msgs.hello_msg, reply_markup=keyboard)
    await message.delete()


async def antpool_sub(message: types.Message):
    print(f'Press button ANTpool ID: {message.from_user.id}')
    if message.from_user.id in users_id:
        if message.text == '/antpool_subscribe':
            await bot.send_message(message.from_user.id, msgs.ant_sub_success, reply_markup=keyboard)
        await bot.send_message(message.from_user.id, ant_request(), reply_markup=keyboard)

        while message.text != '/antpool_unsubscribe':
            last_notify = ant_request()
            print(last_notify)
            await sleep(900)
            last_notify_2 = ant_request()
            if last_notify_2 != last_notify:
                await bot.send_message(message.from_user.id, last_notify_2, reply_markup=keyboard)
        await bot.send_message(message.from_user.id, msgs.ant_sub_denied, reply_markup=keyboard)

    else:
        await bot.send_message(message.from_user.id, msgs.not_sub, reply_markup=keyboard)


async def emcdpool_sub(message: types.Message):
    print(f'Press button EMCDpool ID: {message.from_user.id}')

    if message.from_user.id in users_id:
        if message.text == '/emcd_subscribe':
            await bot.send_message(message.from_user.id, msgs.emcd_sub_success, reply_markup=keyboard)
        await bot.send_message(message.from_user.id, emcd_request(), reply_markup=keyboard)

        while message.text != '/emcd_unsubscribe':
            last_notify = emcd_request()
            print(last_notify)
            await sleep(900)
            last_notify_2 = emcd_request()
            if last_notify_2 != last_notify:
                await bot.send_message(message.from_user.id, last_notify_2, reply_markup=keyboard)
        await bot.send_message(message.from_user.id, msgs.emcd_sub_denied, reply_markup=keyboard)
    else:
        await bot.send_message(message.from_user.id, msgs.not_sub, reply_markup=keyboard)


async def unknown_command(message: types.Message):
    print(f'Press unknown button ID: {message.from_user.id}')
    await bot.send_message(message.from_user.id, msgs.unknown_msg, reply_markup=keyboard)
    await message.delete()


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(antpool_sub, commands=['antpool_subscribe', 'antpool_unsubscribe'])
    dp.register_message_handler(emcdpool_sub, commands=['emcd_subscribe', 'emcd_unsubscribe'])
    dp.register_message_handler(unknown_command)

