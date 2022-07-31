from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


help_button = KeyboardButton("/help")
quiz_button = KeyboardButton("/quiz1")
location_button = KeyboardButton("Share Location",
                                 request_location=True)
info_button = KeyboardButton("Share Info",
                             request_contact=True)

start_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
start_markup.row(
    help_button,
    quiz_button,
    location_button,
    info_button,
    
)

gender_1 = KeyboardButton("Я парень")
gender_2 = KeyboardButton("Я девушка")
gender_3 = KeyboardButton("Я помидор")
gender_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
gender_markup.row(
    gender_1,
    gender_2,
    gender_3
)

cancel_button = KeyboardButton("Cancel")
cancel_markup = ReplyKeyboardMarkup(resize_keyboard=True,
                                    one_time_keyboard=True)