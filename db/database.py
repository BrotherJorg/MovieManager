import sqlite3

class Database():
    def __init__(self):
        self.connection = sqlite3.connect("Movies.db")
        self.createTable()

    def createTable(self):
        cursor = self.connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            genre TEXT NOT NULL,
            year INTEGER NOT NULL,
            rating REAL NOT NULL
            )
        """)
        self.connection.commit()
