import sys

from PyQt6.QtWidgets import QApplication

from features.manage_movies.repository import MovieRepository
from features.manage_movies.service import MovieService
from features.manage_movies.view import ManageMoviesView
from features.movie_status.service import watchStatusService


repository = MovieRepository()
service = MovieService(repository)  
watchStatusService = watchStatusService(repository)

app = QApplication(sys.argv)

window = ManageMoviesView(service, watchStatusService)
window.show()

sys.exit(app.exec()) 
