from .repository import ReviewNotesRepository

class ReviewNotesService:

    def __init__(self, repository):
        self.repository = repository

    def getReviewNotes(self, movie_id):
        return self.repository.getReviewNotes(movie_id)

    def saveReviewNotes(self, movie_id, review, notes):
        self.repository.saveReviewNotes(movie_id, review, notes )