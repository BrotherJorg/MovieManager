from .model import ReviewNotes
from db.database import Database

class ReviewNotesRepository:

    def __init__(self):
        self.database = Database()
    
    def getReviewNotes(self, movie_id):
        cursor = self.database.connection.cursor()
        
        cursor.execute("""
            SELECT review, notes
            FROM Movies
            where id = ?
        """, (movie_id,))

        row = cursor.fetchone()

        if row is None:
            return None

        return ReviewNotes(
            movie_id,
            row[0],
            row[1]
        )


    def saveReviewNotes(self, movie_id, review, notes):
        cursor = self.database.connection.cursor()

        cursor.execute("""
            UPDATE Movies
            set review = ?, notes = ?
            where id =?
        """,(review, notes, movie_id))

        self.database.connection.commit()
