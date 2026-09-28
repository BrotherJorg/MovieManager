class MovieService:

    def __init__(self, repository):
        self.repository = repository

    def addMovie(self, movie):
        self.repository.add(movie)

    def getMovie(self):
        return self.repository.getAll()
