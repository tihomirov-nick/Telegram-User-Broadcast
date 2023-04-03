from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import db

bot = Bot(token="5801122202:AAF5vrX4uoqUSBxmB4PQuk5clys2OnwNJ7Q")
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


@dp.chat_join_request_handler()
async def join_request(update: types.ChatJoinRequest):
    user_id=update.from_user.id
    await bot.send_message(user_id, 'Реклама')
    #тут можно добавить пользователя в бд для дальнейших рассылок
    await update.approve() #.decline() если отклоняем


@dp.message_handler(commands=['send'])
async def client(mes: types.Message, state: FSMContext):
    await bot.send_message(mes.from_user.id, text=f"Привет, {mes.from_user.first_name}!")


@dp.message_handler()
async def send_1()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)