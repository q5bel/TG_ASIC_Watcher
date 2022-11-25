from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from data import TG_TOKEN


bot = Bot(token=TG_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler()
async def echo_send(message: types.Message):
    await message.answer(message.text)



executor.start_polling(dp, skip_updates=True)