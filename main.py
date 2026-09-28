import sys

from PyQt6.QtWidgets import QApplication

from features.manage.repository import MovieRepository
from features.manage.service import MovieService
from features.manage.view import ManageMoviesView


repository = MovieRepository()
service = MovieService(repository)

app = QApplication(sys.argv)

window = ManageMoviesView(service)
window.show()

sys.exit(app.exec())
