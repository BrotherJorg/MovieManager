class FavoritesService:

    def __init__(self, collectionService):
        self.collectionService = collectionService

    def getFavoritesCollection(self):
        return self.collectionService.getCollectionByName(
            "Favorites"
        )

    def isFavorite(self, movieId):

        collection = self.getFavoritesCollection()

        if collection is None:
            return False

        movies = self.collectionService.getMoviesInCollection(
            collection[0]
        )

        for movie in movies:
            if movie[0] == movieId:
                return True

        return False

    def toggleFavorite(self, movieId):

        collection = self.getFavoritesCollection()

        if collection is None:
            return False

        collectionId = collection[0]

        if self.isFavorite(movieId):
            self.collectionService.removeMovieFromCollection(
                movieId,
                collectionId
            )
            return False

        self.collectionService.addMovieToCollection(
            movieId,
            collectionId
        )

        return True

    def getFavorites(self):

        collection = self.getFavoritesCollection()

        if collection is None:  
            return []

        return self.collectionService.getMoviesInCollection(
            collection[0]
        )