class MovieService:

    def __init__(self, repository):
        self.repository = repository

    def addMovie(self, movie):
        self.repository.add(movie)

    def getMovie(self):
        return self.repository.getAll()

    def updateMovie(self, movie):
        self.repository.updateMovie(movie)

    def deleteMovie(self, movie_id):
        self.repository.deleteMovie(movie_id)