from .repository import MoviePickerRepository


class MoviePickerService:

    def __init__(self, repository):
        self.repository = repository

    def getRandomMovie(self):
        return self.repository.getRandomMovie()