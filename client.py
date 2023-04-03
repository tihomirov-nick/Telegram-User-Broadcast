from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from create_bot import bot
import db

async def client(mes: types.Message, state: FSMContext):
    await state.finish()
    await bot.send_message(mes.from_user.id, text=f"Привет, {mes.from_user.first_name}!")


class Sender(StatesGroup):
    text = State()
    img = State()


async def admin(mes: types.Message, state: FSMContext):
    await state.finish()
    await bot.send_message(mes.from_user.id, text="Введите текст сообщения для рассылки")
    await Sender.text.set()


async def add_text(mes: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['text'] = mes.text
    await bot.send_message(mes.from_user.id, text="Отправьте фото для рассылки")
    await Sender.img.set()


async def add_img(mes: types.Message, state: FSMContext):
    id = mes.photo[0].file_id
    async with state.proxy() as data:
        all_ids = await db.get_all_ids()
        for user_id in all_ids:
            await bot.send_photo(user_id, photo=id, caption=data['text'])


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(client, commands=['start'], state='*')
    dp.register_message_handler(admin, commands=['admin'], state='*')
    dp.register_message_handler(add_text, state=Sender.text)
    dp.register_message_handler(add_img, content_types=['photo'], state=Sender.img)