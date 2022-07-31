from pydoc import text
from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode
from config import bot, dp
from keyboards import client_kb
import random

# @dp.message_handler(commands=['start'])
async def hello(message: types.Message):
    await message.reply("Hay")
    await bot.send_message(message.chat.id, "Hello suka im first your bot",
                            reply_markup=client_kb.start_markup)

async def help(message: types.Message):
    await  message.reply(f"Hello {message.from_user.first_name}😘\n"
                         f"I\'m your bot for filtering messages, "
                         f"so that\'s why be careful, i can ban you for curse words😎\n"
                         f"Also i have some commands\n"
                         f"1. /quiz1 this command for funny quiz questions"
                         f", quiz has continue by clicking "
                         f"button *Следующая викторина*\n"
                         f"2. Also u can share location or info about u")


async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("Следующая Викторина",
                                         callback_data="button_call_1")
    markup.add(button_call_1)
    question = "Who invented Tesla"
    answers = [
        "Atam",
        "Apam",
        "Brat",
        "Ilon Mask"
    ]
    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type="quiz",
        correct_option_id=3,
        explanation="I do not know either",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )

async def send_mem(message: types.Message):
    mem = open("media/мем2.jpg", 'rb')
    await bot.send_photo(message.chat.id, photo=mem, caption="Рассмишныл?" )

    
async def echo(message: types.Message): 
    if message.text.isdigit():
        message.text=int(message.text)
        await bot.send_message(message.chat.id, message.text**2)
    else:
        await bot.send_message(message.chat.id, message.text)
    
    if message.text.startswith('pin'):
        await bot.pin_chat_message(message.chat.id, message.message_id) 
    
    if message.text.lower() == 'game':
        emoji=['🎲','⚽️','🎯','🎰','🎳','🏀']
        i=random.randint(0, 5)
        random_emoji = emoji[i]
        await bot.send_dice(message.chat.id, emoji=random_emoji)
       
        
       


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(hello, commands=['start'])
    dp.register_message_handler(help, commands=['help'])
    dp.register_message_handler(quiz_1, commands=['quiz1'])
    dp.register_message_handler(send_mem, commands=['mem'])
    dp.register_message_handler(echo)



