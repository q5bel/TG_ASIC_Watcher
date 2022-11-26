from aiogram import executor, types

from create_bot import dp, bot
import handlers


async def on_startup(_):
    print('Bot is online')
    # sql_start()

handlers.register_handlers(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
