from .model import Movie
from db.database import Database

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
            SELECT id, title, genre, year, rating, status 
            FROM Movies
        """)

        rows = cursor.fetchall()
        movies = []
         
        for row in rows:
            movie = Movie(
                row[1],
                row[2],
                row[3],
                row[4],
                row[0],
                row[5]
                )

            movies.append(movie)
            
        return movies
    

    def updateMovie(self, movie):
        cursor = self.database.connection.cursor()

        cursor.execute("""
            UPDATE Movies
            SET title = ?, genre = ?, year = ?, rating = ?
            WHERE id = ?
        """, (
            movie.title,
            movie.genre,
            movie.year, 
            movie.rating,
            movie.id
        ))   

        self.database.connection.commit()


    def deleteMovie(self, movie_id):
        cursor = self.database.connection.cursor()

        cursor.execute("""
            DELETE FROM Movies
            WHERE id = ?
        """, (movie_id,))

        self.database.connection.commit()


    def searchMovies(self, searchText, genre, status):
            print("SEARCH:", searchText)
            print("GENRE:", genre)
            print("STATUS:", status)
        
            conditions = []
            values = []

            if searchText:
                conditions.append("title LIKE ?")
                values.append(f"%{searchText}%")

            if genre != "All Genres":
                conditions.append("genre = ?")
                values.append(genre)

            if status != "All status":
                conditions.append("status = ?")
                values.append(status)

            query = ("""
                SELECT id, title, genre, year, rating, status
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
                    row[0],
                    row[5]
                )
                movies.append(movie)

            return movies


    def getGenres(self):
        cursor = self.database.connection.cursor()

        cursor.execute("""
            SELECT DISTINCT genre
            FROM Movies
            ORDER BY genre
        """)

        rows = cursor.fetchall()

        genres = []

        for row in rows:
            genres.append(row[0])

        return genres


    def updateStatus(self, movie_id, status):
        cursor = self.database.connection.cursor()

        cursor.execute("""
            UPDATE Movies
            SET status = ?
            WHERE id = ?
        """, (status, movie_id))

        self.database.connection.commit()
