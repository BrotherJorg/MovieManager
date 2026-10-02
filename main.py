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

repository = MovieRepository()
service = MovieService(repository)  

watchStatusService = WatchStatusService(repository)

reviewNotesRepository = ReviewNotesRepository()
reviewNotesService = ReviewNotesService(reviewNotesRepository)

dashboardRepository = DashboardRepository()
dashboardService = DashboardService(dashboardRepository)

app = QApplication(sys.argv)

window = ManageMoviesView(service, watchStatusService, reviewNotesService, dashboardService)
window.show()

sys.exit(app.exec()) 
