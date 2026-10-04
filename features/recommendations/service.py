from .repository import RecommendationRepository
from .model import Recommendation


class RecommendationService:

    def __init__(self, repository):
        self.repository = repository

    def getRecommendations(self):

        movies = self.repository.getMovies()

        scoredMovies = []

        for movie in movies:

            rating = movie[4]
            status = movie[5]

            score = rating * 10

            if status == "Unwatched":
                score += 15

            elif status == "Watching":
                score += 5

            elif status == "Watched":
                score -= 10

            scoredMovies.append((score, movie))

        scoredMovies.sort(
            key=lambda item: item[0],
            reverse=True
        )

        recommendations = []

        for score, movie in scoredMovies[:5]:

            if movie[5] == "Unwatched":
                reason = "Highly rated and unwatched"

            elif movie[5] == "Watching":
                reason = "Highly rated and currently watching"

            else:
                reason = "Highly rated"

            recommendation = Recommendation(
                movie,
                reason
            )

            recommendations.append(recommendation)

        return recommendations