import asyncio
import aioschedule
from aiogram import types, Dispatcher
from config import bot

async def get_chat(message: types.Message):
    global chat_id
    chat_id = message.from_user.id
    await bot.send_message(chat_id=chat_id, text="OK")


async def go_to_study():
    await bot.send_message(chat_id=chat_id, text="Пора учиться!")

async def scheduler():
    aioschedule.every().saturday.at("0:59").do(go_to_study)
    
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(2)


def register_handler_notification(dp: Dispatcher):
    dp.register_message_handler(get_chat,
                                lambda word: 'напомни' in word.text)