from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards import client_kb
from config import bot
from config import ADMIN_ID
from database import bot_db


class FSMAdmin(StatesGroup):
    photo_of_the_dish = State()
    dish_name = State()
    description_of_the_dish = State()
    dish_price = State()
    
async def fsm_start(message: types.Message):
    if message.chat.type == "private":
        if message.from_user.id == ADMIN_ID:
            await FSMAdmin.photo_of_the_dish.set()
            await message.answer(f"Привет {message.from_user.full_name} "
                                 f"Отправьте фотку...", reply_markup=client_kb.cancel_markup)
        else:
            await message.reply("Вам нет доступа!")
    else:
        await message.reply("Пиши в личку")


async def load_photo(message: types.Message,
                     state: FSMContext):
    async with state.proxy() as data:
        data['id'] = message.from_user.id
        data['username'] = f"@{message.from_user.username}"
        data['photo'] = message.photo[0].file_id
    await FSMAdmin.next()
    await message.answer("Название блюда:")

async def load_name(message: types.Message,
                     state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.answer("Описание блюда:")

async def load_description(message: types.Message,
                     state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
    await FSMAdmin.next()
    await message.answer("Цена:")    


async def load_price(message: types.Message,
                     state: FSMContext):
    try:
        if int(message.text) > 5000 or int(message.text) < 0:
            await message.answer("Доступ запрещен!")
        else:
            async with state.proxy() as data:
                data['price'] = int(message.text)
            await FSMAdmin.next()
    except:
        await message.answer("Пиши цифрами!")
    
    async with state.proxy() as data:
        await bot.send_photo(message.from_user.id, data['photo'],
                            caption=f"Ваше меню:\n\n"
                                    f"Название блюда: {data['name']}\n"
                                    f"Описание блюда: {data['description']}\n"
                                    f"Цена блюда: {data['price']}\n\n"
                                    f"{data['username']}")
        await message.answer(data['username'])
        print(data)
        
        
    await bot_db.sql_command_insert(state)
    await state.finish()
    

async def cancel_registration(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    else:
        await state.finish()
        await message.answer("Попробуйте еще раз")


def register_handler_fsmAdminMenu(dp: Dispatcher):
    dp.register_message_handler(cancel_registration, state="*", commands=['cancel'])
    dp.register_message_handler(cancel_registration, Text(equals='cancel',
                                                          ignore_case=True), state="*")

    dp.register_message_handler(fsm_start, commands=['menu'])
    dp.register_message_handler(load_photo, state=FSMAdmin.photo_of_the_dish,
                                content_types=['photo'])
    dp.register_message_handler(load_name, state=FSMAdmin.dish_name)
    dp.register_message_handler(load_description, state=FSMAdmin.description_of_the_dish)
    dp.register_message_handler(load_price, state=FSMAdmin.dish_price)
    



