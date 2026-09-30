class Movie:

    def __init__(self, title, genre, year, rating, id = None):
        self.id = id
        self.title = title
        self.genre = genre
        self.year = year
        self.rating = rating
