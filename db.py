import sqlite3 as sq


def sql_start():
    global base, cur
    base = sq.connect('users.db')
    cur = base.cursor()

async def add_user(id):
    cur.execute("INSERT INTO users VALUES(?)", (id,))
    base.commit()

async def get_all_ids():
    return cur.execute("SELECT * FROM users").fetchall()