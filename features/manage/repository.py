from .model import Movie


class MovieRepository:

    def __init__(self):
        self.movies = [
            Movie("Alien", "Horror", 1979, 8.5)
        ]

    def add(self, movie):
        self.movies.append(movie)

    def getAll(self):
        return self.movies
