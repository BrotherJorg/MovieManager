from db.database import Database


class RecommendationRepository:

    def __init__(self):
        self.database = Database()

    def getMovies(self):

        cursor = self.database.connection.cursor()

        cursor.execute("""
            SELECT id, title, genre, year, rating, status
            FROM Movies
            ORDER BY rating DESC
        """)

        return cursor.fetchall()