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

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS collections (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS movie_collections (
            movie_id INTEGER NOT NULL,
            collection_id INTEGER NOT NULL,
            PRIMARY KEY (movie_id, collection_id),
            FOREIGN KEY (movie_id) REFERENCES movies(id) ON DELETE CASCADE,
            FOREIGN KEY (collection_id) REFERENCES collections(id) ON DELETE CASCADE
            )
        """)


        cursor.execute("""
            INSERT OR IGNORE INTO collections (name)
            VALUES ('Favorites')
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