
from db.database import Database


class CollectionRepository:

    def __init__(self):
        self.database = Database()

    def createCollection(self, name):
        cursor = self.database.connection.cursor()

        cursor.execute("""
            INSERT INTO collections (name)
            VALUES (?)
        """, (name,))

        self.database.connection.commit()

    def getAllCollections(self):
        cursor = self.database.connection.cursor()

        cursor.execute("""
            SELECT id, name
            FROM collections
            ORDER BY name
        """)

        return cursor.fetchall()

    def deleteCollection(self, collection_id):
        cursor = self.database.connection.cursor()

        cursor.execute("""
            DELETE FROM collections
            WHERE id = ?
        """, (collection_id,))

        self.database.connection.commit()

    def addMovieToCollection(self, movie_id, collection_id):
        cursor = self.database.connection.cursor()

        cursor.execute("""
            INSERT OR IGNORE INTO movie_collections
            (movie_id, collection_id)
            VALUES (?, ?)
        """, (movie_id, collection_id))

        self.database.connection.commit()

    def removeMovieFromCollection(self, movie_id, collection_id):
        cursor = self.database.connection.cursor()

        cursor.execute("""
            DELETE FROM movie_collections
            WHERE movie_id = ? AND collection_id = ?
        """, (movie_id, collection_id))

        self.database.connection.commit()

    def getMoviesInCollection(self, collection_id):
        cursor = self.database.connection.cursor()

        cursor.execute("""
            SELECT movies.id, movies.title, movies.genre,
                   movies.year, movies.rating, movies.status
            FROM movies
            INNER JOIN movie_collections
                ON movies.id = movie_collections.movie_id
            WHERE movie_collections.collection_id = ?
            ORDER BY movies.title
        """, (collection_id,))

        return cursor.fetchall()

    def getAllMovies(self):
        cursor = self.database.connection.cursor()

        cursor.execute("""
            SELECT id, title, genre, year, rating, status
            FROM movies
            ORDER BY title
        """)

        return cursor.fetchall()
