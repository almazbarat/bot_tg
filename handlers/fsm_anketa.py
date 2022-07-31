from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from datetime import datetime
from keyboards import client_kb
from config import bot
from database import bot_db

class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    age = State()
    sex = State()
    region = State()

async def fsm_start(message: types.Message):
    if message.chat.type == "private":
        await FSMAdmin.photo.set()
        await message.answer(f"Привет {message.from_user.full_name} "
                             f"Отправьте фотку...", reply_markup=client_kb.cancel_markup)
    else:
        await message.reply("Пиши в личку")

async def load_photo(message: types.Message,
                     state: FSMContext):
    async with state.proxy() as data:
        data['id'] = message.from_user.id
        data['username'] = f"@{message.from_user.username}"
        data['photo'] = message.photo[0].file_id
    await FSMAdmin.next()
    await message.answer("Как звать?")

async def load_name(message: types.Message,
                     state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.answer("Какого ты года?")

async def load_age(message: types.Message,
                     state: FSMContext):
    try:
        if int(message.text) > 2007 or int(message.text) < 1950:
            await message.answer("Доступ запрещен!")
        else:
            async with state.proxy() as data:
                data['age'] = datetime.now().year - int(message.text)
            await FSMAdmin.next()
            await message.answer("Какого ты пола?",
                                 reply_markup=client_kb.gender_markup)
    except:
        await message.answer("Пиши цифрами!")

async def load_sex(message: types.Message,
                     state: FSMContext):
    async with state.proxy() as data:
        data['sex'] = message.text
    await FSMAdmin.next()
    await message.answer("Где проживаешь?", reply_markup=client_kb.cancel_markup)

async def load_region(message: types.Message,
                     state: FSMContext):
    async with state.proxy() as data:
        data['region'] = message.text
        await bot.send_photo(message.from_user.id, data['photo'],
                            caption=f"Name: {data['name']}\n"
                                    f"Age: {data['age']}\n"
                                    f"Sex {data['sex']}\n"
                                    f"Region {data['region']}\n\n"
                                    f"{data['username']}")
        print(data)
    await bot_db.sql_command_insert(state)
    await state.finish()
    await message.answer("Майли давай)!")

async def cancel_registration(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    else:
        await state.finish()
        await message.answer("Регистрация прервана")


def register_handler_fsmadmin(dp: Dispatcher):
    dp.register_message_handler(cancel_registration, state="*", commands=['cancel'])
    dp.register_message_handler(cancel_registration, Text(equals='cancel',
                                                          ignore_case=True), state="*")

    dp.register_message_handler(fsm_start, commands=['anketa'])
    dp.register_message_handler(load_photo, state=FSMAdmin.photo,
                                content_types=['photo'])
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_age, state=FSMAdmin.age)
    dp.register_message_handler(load_sex, state=FSMAdmin.sex)
    dp.register_message_handler(load_region, state=FSMAdmin.region)



