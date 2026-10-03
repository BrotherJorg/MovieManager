from db.database import Database


class MoviePickerRepository:

    def __init__(self):
        self.database = Database()

    def getRandomMovie(self):

        cursor = self.database.connection.cursor()

        cursor.execute("""
            SELECT id, title, genre, year, rating, status
            FROM Movies
            ORDER BY RANDOM()
            LIMIT 1
        """)

        row = cursor.fetchone()

        if row is None:
            return None

        return row