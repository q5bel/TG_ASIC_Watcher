from aiogram import executor

from start_bot import dp
import handlers

handlers.register_handlers(dp)

executor.start_polling(dp, skip_updates=True)
