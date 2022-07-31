
from aiogram import Dispatcher, types
from config import bot
from keyboards import admin_kb
from config import ADMIN_ID

async def is_admin_function(message: types.Message):
    
    if message.from_user.id == ADMIN_ID:
        await bot.send_message(message.chat.id,
                               "Hello Admin",
                               reply_markup=admin_kb.admin_markup)
    else:
        await bot.send_message(message.chat.id,
                               "Hello, u r not allowed to this function")
    await bot.delete_message(message.chat.id,
                             message.message_id)
    print(message.from_user.id)
    await bot.delete_message(message.chat.id,
                            message.message_id)


def register_handler_admin(dp: Dispatcher):
    dp.register_message_handler(is_admin_function,
                                commands=['admin'])
