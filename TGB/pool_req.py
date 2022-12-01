from API.antpool import ant_request
from API.emcd import emcd_request
from create_bot import bot
from keyboards import keyboard
from config import USERS

import asyncio


async def get_reg():
    for user in USERS:
        await bot.send_message(user, 'Start checking pools.', reply_markup=keyboard)
    while True:
        print("New loop " + "#" * 15)
        t = await get_act()
        print("Sleep 30 seconds")
        await asyncio.sleep(150)
        data = await get_act()
        if data != t:
            for user in USERS:
                await bot.send_message(user, '📣 Look! Some changes at pool', reply_markup=keyboard)
                await bot.send_message(user, data, reply_markup=keyboard)
        print("Sleep 30 seconds")
        await asyncio.sleep(150)


async def get_act():
    print('Making get_act #################')
    a = ant_request()
    e = emcd_request()

    t = f"""
️🐜ANTPOOL WORKERS
🔴 Inactive: {a[0]}
🟢 Active: {a[1]}

🏧 EMCD WORKERS
🔴️ Inactive: {e[0]}
🟢 Active: {e[1]}"""
    return t

