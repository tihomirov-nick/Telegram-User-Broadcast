from aiogram import types
from aiogram.utils import executor

from create_bot import dp, bot
import client
import db


async def on_startup(dp):
    db.sql_start()
    await dp.bot.set_my_commands([
        types.BotCommand("start", "Запустить бота")])


@dp.chat_join_request_handler()
async def join_request(update: types.ChatJoinRequest):
    user_id = update.from_user.id
    await db.add_user(user_id)
    await bot.send_message(user_id, 'Реклама')
    await update.approve()


client.register_handlers_client(dp)
# admin.register_handlers_admin(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)