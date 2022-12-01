import asyncio

from aiogram import executor

from create_bot import dp, bot
import handlers
from config import USERS
from pool_req import get_reg, get_act


async def on_startup(_):
    print('Bot is online')
    for user in USERS:
        await bot.send_message(user, 'Bot is online.')
        await bot.send_message(user, await get_act())
    asyncio.create_task(get_reg())



handlers.register_handlers(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
