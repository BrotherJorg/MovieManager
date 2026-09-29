from PyQt6.QtCore import QDataStream
from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QTableWidget,
    QTableWidgetItem,
    QPushButton,
    QDialog,
    QLineEdit,
    QLabel,
    QFormLayout,
)

from PyQt6.QtCore import Qt
from .model import Movie


class ManageMoviesView(QMainWindow):

    def __init__(self, service):
        super().__init__()

        self.service = service

        self.setWindowTitle("MovieOWL")
        self.resize(800, 600)

        self.setup_ui()
        self.loadMovies()

    def setup_ui(self):

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QHBoxLayout()
        central_widget.setLayout(main_layout)

        sideBarwidget = QWidget()
        sideBarwidget.setFixedWidth(180)

        side_layout = QVBoxLayout()
        sideBarwidget.setLayout(side_layout)

        main_layout.addWidget(sideBarwidget)

        right_layout = QVBoxLayout()
        main_layout.addLayout(right_layout)

        addButton = QPushButton("Add Movie")
        addButton.clicked.connect(self.addMovie)
        viewButton = QPushButton("View Details")
        viewButton.clicked.connect(self.viewDetails)
        editButton = QPushButton("Edit Movie")
        editButton.clicked.connect(self.editMovie)
        delButton = QPushButton("Delete Movie")
        delButton.clicked.connect(self.deleteMovie)

        side_layout.addWidget(addButton)
        side_layout.addWidget(viewButton)
        side_layout.addWidget(editButton)
        side_layout.addWidget(delButton)

        self.movieTable = QTableWidget()
        self.movieTable.setColumnCount(4)

        self.movieTable.setHorizontalHeaderLabels([
            "title",
            "genre",
            "year",
            "rating"
        ])
        right_layout.addWidget(self.movieTable)



    def loadMovies(self):
        movies = self.service.getMovie()
        self.movieTable.setRowCount(len(movies))

        for row, movie in enumerate(movies):
            self.movieTable.setItem(row, 0, QTableWidgetItem(movie.title))
            self.movieTable.setItem(row, 1, QTableWidgetItem(str(movie.genre)))
            self.movieTable.setItem(row, 2, QTableWidgetItem(str(movie.year)))
            self.movieTable.setItem(row, 3, QTableWidgetItem(str(movie.rating)))

    def addMovie(self):
       dialog = QDialog(self)
       dialog.setWindowTitle("Add Movie")

       formLayout = QFormLayout()
       dialog.setLayout(formLayout)

       self.titleInput = QLineEdit()
       self.yearInput = QLineEdit()
       self.genreInput = QLineEdit()
       self.ratingInput = QLineEdit()
       
       formLayout.addRow("Title:", self.titleInput)
       formLayout.addRow("Genre:", self.genreInput)
       formLayout.addRow("Year:", self.yearInput)
       formLayout.addRow("Rating:", self.ratingInput)

       addButton = QPushButton("Add")
       canButton = QPushButton("Cancel")
       formLayout.addRow(addButton, canButton)

       addButton.clicked.connect(self.saveMovie)
       canButton.clicked.connect(dialog.reject)
       dialog.exec()

    def saveMovie(self):
        title = self.titleInput.text()
        genre = self.genreInput.text()
        year = int(self.yearInput.text())
        rating = float(self.ratingInput.text())
       
        movie = Movie(title, genre, year, rating)

        self.service.addMovie(movie)

        self.loadMovies()


    def viewDetails(self):
        row = self.movieTable.currentRow()

        if row == -1:
            return

        movies = self.service.getMovie()
        movie = movies[row]

        dialog = QDialog(self)
        dialog.setWindowTitle("Movie Details")

        layout = QFormLayout()
        dialog.setLayout(layout)

        layout.addRow("Title:", QLabel(movie.title))
        layout.addRow("Genre:", QLabel(movie.genre))
        layout.addRow("Year:", QLabel(str(movie.year)))
        layout.addRow("Rating:", QLabel(str(movie.rating)))

        dialog.exec()

    def editMovie(self):
        row = self.movieTable.currentRow()

        if row == -1:
            return

        movies = self.service.getMovie()
        movie = movies[row]

        dialog = QDialog(self)
        dialog.setWindowTitle("Edit Movie")

        formLayout = QFormLayout()
        dialog.setLayout(formLayout)

        self.titleInput = QLineEdit(movie.title)
        self.yearInput = QLineEdit(str(movie.year))
        self.genreInput = QLineEdit(movie.genre)
        self.ratingInput = QLineEdit(str(movie.rating))

        formLayout.addRow("Title:", self.titleInput)
        formLayout.addRow("Genre:", self.genreInput)
        formLayout.addRow("Year:", self.yearInput)
        formLayout.addRow("Rating:", self.ratingInput)

        saveButton = QPushButton("Save")
        cancelButton = QPushButton("Cancel")

        formLayout.addRow(saveButton, cancelButton)

        saveButton.clicked.connect(lambda: self.saveEdit(dialog, movie))
        cancelButton.clicked.connect(dialog.reject)

        dialog.exec()


    def saveEdit(self, dialog, movie):
        movie.title = self.titleInput.text()
        movie.genre = self.genreInput.text()
        movie.year = int(self.yearInput.text())
        movie.rating = float(self.ratingInput.text())

        dialog.accept()
        self.loadMovies()

    def deleteMovie(self):
        row = self.movieTable.currentRow()

        if row == -1:
         return

        movies = self.service.getMovie()
        movie = movies[row]
        
        movies.remove(movie)
        self.loadMovies()