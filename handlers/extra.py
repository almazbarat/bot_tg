from aiogram import types, Dispatcher
from config import bot, dp
from datetime import datetime,timedelta


async def ban_for_bad_words(message: types.Message):
    ban_words = ["fuck", "жетим", "сучка"]
    for word in ban_words:
        if word in message.text.lower().replace(" ", ""):
            await bot.send_message(message.chat.id,
                                   f"Пошел на*уй из группы!: {message.from_user.full_name}")
            await bot.ban_chat_member(message.chat.id,
                                      message.from_user.id,
                                      until_date=datetime.now() + timedelta(minutes=1) )

            await bot.delete_message(message.chat.id,
                                     message.message_id)
        await message.reply("Незарегистрированная команда или текст")

def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(ban_for_bad_words)


