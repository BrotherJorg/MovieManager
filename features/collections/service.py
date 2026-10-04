from .repository import CollectionRepository


class CollectionService:

    def __init__(self, repository):
        self.repository = repository

    def createCollection(self, name):
        name = name.strip()

        if not name:
            return False

        self.repository.createCollection(name)

        return True

    def getAllCollections(self):
        return self.repository.getAllCollections()

    def deleteCollection(self, collection_id):
        self.repository.deleteCollection(collection_id)

    def addMovieToCollection(self, movie_id, collection_id):
        self.repository.addMovieToCollection(
            movie_id,
            collection_id
        )

    def removeMovieFromCollection(
        self,
        movie_id,
        collection_id
    ):
        self.repository.removeMovieFromCollection(
            movie_id,
            collection_id
        )

    def getMoviesInCollection(self, collection_id):
        return self.repository.getMoviesInCollection(
            collection_id
        )

    def getAllMovies(self):
        return self.repository.getAllMovies()

