import sys

from PyQt6.QtWidgets import QApplication

from features.manage_movies.repository import MovieRepository
from features.manage_movies.service import MovieService
from features.manage_movies.view import ManageMoviesView
from features.movie_status.service import WatchStatusService

from features.review_notes.service import ReviewNotesService

from features.review_notes.repository import ReviewNotesRepository

from features.dashboard.repository import DashboardRepository
from features.dashboard.service import DashboardService

from features.movie_picker.repository import MoviePickerRepository
from features.movie_picker.service import MoviePickerService

from features.recommendations.repository import RecommendationRepository
from features.recommendations.service import RecommendationService

repository = MovieRepository()
service = MovieService(repository)  

watchStatusService = WatchStatusService(repository)

reviewNotesRepository = ReviewNotesRepository()
reviewNotesService = ReviewNotesService(reviewNotesRepository)

dashboardRepository = DashboardRepository()
dashboardService = DashboardService(dashboardRepository)


moviePickerRepository = MoviePickerRepository()
moviePickerService = MoviePickerService(moviePickerRepository)

recommendationRepository = RecommendationRepository()
recommendationService = RecommendationService(   recommendationRepository)

app = QApplication(sys.argv)

window = ManageMoviesView(service, watchStatusService, reviewNotesService, dashboardService, moviePickerService, recommendationService)
window.show()

sys.exit(app.exec()) 
