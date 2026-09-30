from pickletools import read_uint1
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
                row[4],
                row[0]
                )

            movies.append(movie)
            
        return movies
    
    def updateMovie(self, movie):
        cursor = self.database.connection.cursor()
        cursor.execute("""
            UPDATE Movies
            SET title = ?, genre = ?, year = ?, rating = ?
            where id = ?
        """, (
            movie.title,
            movie.genre,
            movie.year, 
            movie.rating,
            movie.id
            )
        )   
        self.database.connection.commit()

    def deleteMovie(self, movie_id):
        cursor = self.database.connection.cursor()

        cursor.execute("""
            DELETE FROM Movies
            WHERE id = ?
        """, 
        (movie_id,))

        self.database.connection.commit()


    def searchMovies(self, searchText, genre):

        conditions = []
        values = []

        if searchText:
            conditions.append("title LIKE ?")
            values.append(f"%{searchText}%")

        if genre != "All Genres":
            conditions.append("genre = ?")
            values.append(genre)

        query = ("""
            SELECT id, title, genre, year, rating
            FROM Movies
        """)


        if conditions:
            query += " WHERE " + " AND ".join(conditions) 

        cursor = self.database.connection.cursor()
        cursor.execute(query, values)

        rows = cursor.fetchall()

        movies = []
        for row in rows:
            movie = Movie(
                row[1],
                row[2],
                row[3],
                row[4],
                row[0]
            )
            movies.append(movie)

        return movies