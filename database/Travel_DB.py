import sqlite3


db_name = "travel.db"


class SQLTravelDB():
    def __init__(self):
        with sqlite3.connect(db_name) as con:
            con.execute('CREATE TABLE IF NOT EXISTS restaurant(name TEXT NOT NULL, address TEXT NOT NULL)')
            con.execute('CREATE TABLE IF NOT EXISTS concert(name TEXT NOT NULL, address TEXT NOT NULL)')

