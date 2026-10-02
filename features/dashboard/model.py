class DashboardStats:
    def __init__(
        self,
        totalMovies,
        watched,
        watching,
        unwatched,
        averageRating,
        genreCounts
    ):

        self.totalMovies = totalMovies
        self.watched = watched
        self.watching = watching
        self.unwatched = unwatched
        self.averageRating = averageRating
        self.genreCounts = genreCounts