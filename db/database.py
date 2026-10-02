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
            rating REAL NOT NULL,
            status TEXT NOT NULL DEFAULT 'Unwatched'
            )
        """)

        cursor.execute("PRAGMA table_info(movies)")
        columns = [column[1] for column in cursor.fetchall()]

        if "review" not in columns:
            cursor.execute("""
            ALTER TABLE movies
            ADD COLUMN review TEXT
        """)

        if "notes" not in columns:
            cursor.execute("""
            ALTER TABLE movies
            ADD COLUMN notes TEXT
        """)
        self.connection.commit()
