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
    QComboBox
    
)
from PyQt6.QtCore import Qt
from .model import Movie
from features.review_notes.view import ReviewNotesView

class WatchStatusView(QDialog):

    def __init__(self, service, movie, parent=None):
        super().__init__(parent)

        self.service = service
        self.movie = movie

        self.setWindowTitle("Watch Status")

        layout = QVBoxLayout()
        self.setLayout(layout)

        layout.addWidget(QLabel(f"Movie: {movie.title}"))

        self.statusCombo = QComboBox()
        self.statusCombo.addItems([
            "Unwatched",
            "Watching",
            "Watched"
        ])

        self.statusCombo.setCurrentText(movie.status)
        layout.addWidget(self.statusCombo)

        saveButton = QPushButton("Save")
        saveButton.clicked.connect(self.saveStatus)

        layout.addWidget(saveButton)

    def saveStatus(self):

        status = self.statusCombo.currentText()

        self.service.updateStatus(
            self.movie.id,
            status
        )

        self.accept()




class ManageMoviesView(QWidget):

    def __init__(self, service, reviewNotesService):
        super().__init__()

        self.service = service
        self.reviewNotesService = reviewNotesService

        self.setWindowTitle("MovieOWL")
        self.resize(1280 , 720  )

        self.setup_ui()
        self.loadGenres()
        self.loadMovies()
        

    def setup_ui(self):

        main_layout = QHBoxLayout()
        self.setLayout(main_layout)

        sidebarwidget = QWidget()
        sidebarwidget.setFixedWidth(180)

        side_layout = QVBoxLayout()
        sidebarwidget.setLayout(side_layout)

        main_layout.addWidget(sidebarwidget)

        right_layout = QVBoxLayout()
        main_layout.addLayout(right_layout)

        search_layout = QHBoxLayout()
        right_layout.addLayout(search_layout)

        # MAIN UI BUTTONS

        self.searchInput = QLineEdit()
        self.searchInput.setPlaceholderText("Search movies...")
        search_layout.addWidget(self.searchInput)

        searchButton = QPushButton("Search")
        search_layout.addWidget(searchButton)

        searchButton.clicked.connect(self.searchMovies)
        self.searchInput.returnPressed.connect(self.searchMovies)

        self.genreCombo = QComboBox()
        self.genreCombo.addItem("All Genres")
        self.genreCombo.currentIndexChanged.connect(self.searchMovies)
        search_layout.addWidget(self.genreCombo)

        self.statusCombo = QComboBox()
        self.statusCombo.addItems([
            "All status",
            "Unwatched",
            "Watching",
            "Watched"
        ])

        self.statusCombo.currentIndexChanged.connect(self.searchMovies)
        search_layout.addWidget(self.statusCombo)

        # sidebar buttons 

        addButton = QPushButton("Add Movie")
        addButton.clicked.connect(self.addMovie)

        viewButton = QPushButton("View Details")
        viewButton.clicked.connect(self.viewDetails)

        editButton = QPushButton("Edit Movie")
        editButton.clicked.connect(self.editMovie)

        deleteButton = QPushButton("Delete Movie")
        deleteButton.clicked.connect(self.deleteMovie)

        statusButton = QPushButton("Watch Status")
        statusButton.clicked.connect(self.changeWatchStatus)

        self.reviewNotesButton = QPushButton("Reviews & Notes")
        self.reviewNotesButton.clicked.connect(self.openReviewNotes)    

        side_layout.addWidget(addButton)
        side_layout.addWidget(viewButton)
        side_layout.addWidget(editButton)
        side_layout.addWidget(deleteButton)
        side_layout.addWidget(statusButton)
        side_layout.addWidget(self.reviewNotesButton)
    

        # GUI TABLE 

        self.movieTable = QTableWidget()
        self.movieTable.setColumnCount(5)

        self.movieTable.setHorizontalHeaderLabels([
            "Title",
            "Genre",
            "Year",
            "Rating",
            "Status"
        ])
        self.movieTable.horizontalHeader().setStretchLastSection(True)

        right_layout.addWidget(self.movieTable)


    def loadMovies(self):
        movies = self.service.getMovie()
        self.movieTable.setRowCount(len(movies))

        for row, movie in enumerate(movies):
            titleItem =QTableWidgetItem(movie.title)
            titleItem.setData(Qt.ItemDataRole.UserRole, movie.id)

            self.movieTable.setItem(row, 0, titleItem)
            self.movieTable.setItem(row, 1, QTableWidgetItem(str(movie.genre)))
            self.movieTable.setItem(row, 2, QTableWidgetItem(str(movie.year)))
            self.movieTable.setItem(row, 3, QTableWidgetItem(str(movie.rating)))
            self.movieTable.setItem(row, 4, QTableWidgetItem(movie.status))


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

       
        movie_id = self.movieTable.item(row, 0).data(Qt.ItemDataRole.UserRole)

        movies = self.service.getMovie()

        movie = next(
            movie for movie in movies
            if movie.id == movie_id
            )       

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
        

        movie_id = self.movieTable.item(row, 0).data(Qt.ItemDataRole.UserRole)

        movies = self.service.getMovie()
        
        movie = next (
            movie for movie in movies 
            if movie.id == movie_id
        )

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

        self.service.updateMovie(movie)

        dialog.accept()
        self.searchMovies()


    def deleteMovie(self):
        row = self.movieTable.currentRow()

        if row == -1:
         return

        movie_id = self.movieTable.item( row, 0).data(Qt.ItemDataRole.UserRole)
        
        self.service.deleteMovie(movie_id)

        self.searchMovies()


    def searchMovies(self):
        searchText =  self.searchInput.text()
        genre = self.genreCombo.currentText()
        status = self.statusCombo.currentText()

        movies = self.service.searchMovies(searchText, genre, status)

        self.movieTable.setRowCount(len(movies))

        for row, movie in enumerate(movies):
            titleItem = QTableWidgetItem(movie.title)
            titleItem.setData(Qt.ItemDataRole.UserRole, movie.id)
            self.movieTable.setItem(row, 0, titleItem)

            self.movieTable.setItem(row, 1, QTableWidgetItem(str(movie.genre)))
            self.movieTable.setItem(row, 2, QTableWidgetItem(str(movie.year)))
            self.movieTable.setItem(row, 3, QTableWidgetItem(str(movie.rating)))
            self.movieTable.setItem(row, 4, QTableWidgetItem(movie.status))


    def loadGenres(self):
        genres = self.service.getGenres()
        
        self.genreCombo.blockSignals(True)

        self.genreCombo.clear()
        self.genreCombo.addItem("All Genres")
        self.genreCombo.addItems(genres)

        self.genreCombo.blockSignals(False)


    def changeWatchStatus(self):
        row = self.movieTable.currentRow()

        if row == -1:
            return
       
        movie_id = self.movieTable.item(row, 0).data(Qt.ItemDataRole.UserRole)
        
        movies = self.service.getMovie()

        movie = next (
            movie for movie in movies
            if movie.id == movie_id
        )

        dialog = WatchStatusView(
            self.service,
            movie,
            self
        )

        if dialog.exec():
            self.searchMovies()

    def openReviewNotes(self):

        row = self.movieTable.currentRow()

        if row < 0:
            return

        movie_id = self.movieTable.item(
            row, 0
        ).data(Qt.ItemDataRole.UserRole)

        movies = self.service.getMovie()

        movie = next(
            movie for movie in movies
            if movie.id == movie_id
        )

        dialog = ReviewNotesView(
            movie,
            self.reviewNotesService
        )

        dialog.exec()

        self.searchMovies()

