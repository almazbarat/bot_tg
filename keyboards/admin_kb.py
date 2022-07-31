from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

upload_button = KeyboardButton("/upload")
# cancel_button = KeyboardButton("/cancel")

admin_markup = ReplyKeyboardMarkup(resize_keyboard=True)

admin_markup.row(
    upload_button,
    # cancel_button
)