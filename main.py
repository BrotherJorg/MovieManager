import sys
from PyQt6.QtGui import QFont, QFontDatabase

from PyQt6.QtWidgets import QApplication
from features.main_Window.view import MainWindow

from features.manage_movies.repository import MovieRepository
from features.manage_movies.service import MovieService
from features.manage_movies.view import ManageMoviesView


from features.review_notes.service import ReviewNotesService

from features.review_notes.repository import ReviewNotesRepository

from features.dashboard.repository import DashboardRepository
from features.dashboard.service import DashboardService

from features.movie_picker.repository import MoviePickerRepository
from features.movie_picker.service import MoviePickerService

from features.recommendations.repository import RecommendationRepository
from features.recommendations.service import RecommendationService

from features.dashboard.view import DashboardView
from features.movie_picker.view import MoviePickerView
from features.recommendations.view import RecommendationsView

repository = MovieRepository()
service = MovieService(repository)  

reviewNotesRepository = ReviewNotesRepository()
reviewNotesService = ReviewNotesService(reviewNotesRepository)

dashboardRepository = DashboardRepository()
dashboardService = DashboardService(dashboardRepository)


moviePickerRepository = MoviePickerRepository()
moviePickerService = MoviePickerService(moviePickerRepository)

recommendationRepository = RecommendationRepository()
recommendationService = RecommendationService(   recommendationRepository)

app = QApplication(sys.argv)

fontId = QFontDatabase.addApplicationFont(
    "assets/fonts/static/manrope-latin-400-normal.ttf"
)

if fontId != -1:
    fontFamily = QFontDatabase.applicationFontFamilies(fontId)[0]
    app.setFont(QFont(fontFamily, 10))

with open("styles/main.qss", "r") as file:
   app.setStyleSheet(file.read())

manageMoviesView = ManageMoviesView(
    service,
    reviewNotesService
)

dashboardView = DashboardView(dashboardService)
moviePickerView = MoviePickerView(moviePickerService)
recommendationsView = RecommendationsView(recommendationService)

window = MainWindow(
    manageMoviesView,
    dashboardView,
    moviePickerView,
    recommendationsView
)

window.show()

sys.exit(app.exec()) 
