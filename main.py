import sys

from PyQt6.QtWidgets import QApplication

from features.manage_movies.repository import MovieRepository
from features.manage_movies.service import MovieService
from features.manage_movies.view import ManageMoviesView
from features.movie_status.service import WatchStatusService

from features.review_notes.service import ReviewNotesService

from features.review_notes.repository import ReviewNotesRepository

repository = MovieRepository()
service = MovieService(repository)  
watchStatusService = WatchStatusService(repository)

reviewNotesRepository = ReviewNotesRepository()
reviewNotesService = ReviewNotesService(reviewNotesRepository)

app = QApplication(sys.argv)

window = ManageMoviesView(service, watchStatusService, reviewNotesService)
window.show()

sys.exit(app.exec()) 
