from .repository import RecommendationRepository
from .model import Recommendation


class RecommendationService:

    def __init__(self, repository):
        self.repository = repository

    def getRecommendations(self):

        movies = self.repository.getMovies()

        recommendations = []

        for movie in movies[:5]:

            recommendation = Recommendation(
                movie,
                "Highly rated movie in your collection"
            )

            recommendations.append(recommendation)

        return recommendations