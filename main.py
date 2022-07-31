
from config import bot, dp
import asyncio
from aiogram.utils import executor
from handlers import client, callback_quiz, extra, admin, fsmAdminMenu, fsm_anketa, notification
from database.bot_db import sql_create



async def on_startup(_):
    asyncio.create_task(notification.scheduler())

    sql_create()


admin.register_handler_admin(dp)
client.register_handlers_client(dp)
callback_quiz.register_handlers_callback_quiz(dp)
fsmAdminMenu.register_handler_fsmAdminMenu(dp)
fsm_anketa.register_handler_fsmadmin(dp)
notification.register_handler_notification(dp)
extra.register_handlers_extra(dp)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

