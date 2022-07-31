import sqlite3
from config import bot

def sql_create():
    global db, cursor
    db = sqlite3.connect("bot.sqlite3")
    cursor = db.cursor()

    if db:
        print("База данных подключена!")

    db.execute("CREATE TABLE IF NOT EXISTS menu "
               "(id INTEGER PRIMARY KEY, username TEXT,"
               "photo TEXT, dish TEXT, description TEXT, price INTEGER)")
    db.commit()

async def sql_command_insert(state):
    async with state.proxy() as data:
        cursor.execute("INSERT INTO menu VALUES "
        "(?, ?, ?, ?, ?, ?)", tuple(data.values()))
        db.commit()


    