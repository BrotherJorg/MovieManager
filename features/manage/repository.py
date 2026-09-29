from .model import Movie
from db.database import Database
import sqlite3

class MovieRepository:

    def __init__(self):
        self.database = Database()

    def add(self, movie):
        cursor = self.database.connection.cursor()
       
        values = (
            movie.title,
            movie.genre,
            movie.year,
            movie.rating
)

        cursor.execute("""
            INSERT INTO Movies (title, genre, year, rating)
            VALUES(?, ?, ?, ?)
        """, values)

        self.database.connection.commit()

    def getAll(self):
        cursor = self.database.connection.cursor()

        cursor.execute("""
        SELECT id, title, genre, year, rating FROM Movies
        """)

        rows = cursor.fetchall()
        movies = []
         
         
        for row in rows:
            movie = Movie(
                    row[1],
                    row[2],
                    row[3],
                    row[4]
                )

            movies.append(movie)
            
        return movies
        