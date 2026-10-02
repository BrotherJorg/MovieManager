from .model import DashboardStats
from db.database import Database

class DashboardRepository:

    def __init__(self):
        self.database = Database()

    def getStats(self):
        cursor = self.database.connection.cursor()

        cursor.execute("""
            SELECT COUNT(*)
            FROM Movies
         """)
        totalMovies = cursor.fetchone()[0]

        cursor.execute("""
            SELECT COUNT(*)
            FROM Movies
            WHERE status = 'Watched'
        """)
        watched = cursor.fetchone()[0]

        cursor.execute("""
            SELECT COUNT(*)
            FROM Movies
            WHERE status = 'Watching'
        """)
        watching = cursor.fetchone()[0]

        cursor.execute("""
            SELECT COUNT(*)
            FROM Movies
            WHERE status = 'Unwatched'
        """)
        unwatched = cursor.fetchone()[0]

        cursor.execute("""
            SELECT AVG(rating)
            FROM Movies
        """)
        averageRating = cursor.fetchone()[0]

        if averageRating is None:
            averageRating = 0

        cursor.execute("""
            SELECT genre, COUNT(*)
            FROM Movies
            GROUP BY genre
            ORDER BY COUNT(*) DESC
        """)
        genreCounts = dict(cursor.fetchall())

        return DashboardStats(
            totalMovies,
            watched,
            watching,
            unwatched,
            averageRating,
            genreCounts
        )