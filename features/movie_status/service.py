from features.manage_movies.repository import MovieRepository

class WatchStatusService:
    def __init__(self, repository):
        self.repository = repository

    def updateStatus(self, movie_id, status):
            validStatuses = [
                "Unwatched",
                "Watching",
                "Watched"
            ]

            if status not in validStatuses:
                return

            self.repository.updateStatus(movie_id, status)