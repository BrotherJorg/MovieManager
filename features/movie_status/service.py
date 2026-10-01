from features.manage_movies.repository import MovieRepository

class watchStatusService:
    def __init__(self, repository):
        self.repository = repository

    def updateStatus(self, movie_id, status):
            validStatuses = [
                "Unwatched",
                "Wathcing",
                "Watched"
            ]

            if status not in validStatuses:
                return

            self.repository.updateStatus(movie_id, status)