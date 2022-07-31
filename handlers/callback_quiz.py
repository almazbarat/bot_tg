from aiogram import types, Dispatcher
from aiogram.types import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton
from config import bot


async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton("Следующая Викторина",
                                         callback_data="button_call_2")
    markup.add(button_call_2)
    question = "Who invented me"
    answers = [
        "Atam",
        "Apam",
        "Akam",
        "Ilon Mask"
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type="quiz",
        correct_option_id=0,
        explanation="I do not know either",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )


async def quiz_3(call: types.CallbackQuery):
    question = "who are you"
    answers = [
        "Atam",
        "Apam",
        "Akam",
        "You are you"
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type="quiz",
        correct_option_id=3,
        explanation="I do not know either",
        explanation_parse_mode=ParseMode.MARKDOWN_V2)



def register_handlers_callback_quiz(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, lambda call: call.data == "button_call_1")
    dp.register_callback_query_handler(quiz_3, lambda call: call.data == "button_call_2")