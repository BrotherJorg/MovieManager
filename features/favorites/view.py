from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QListWidget,
    QListWidgetItem
)
from PyQt6.QtCore import Qt


class FavoritesView(QWidget):

    def __init__(self, service):
        super().__init__()

        self.service = service

        self.setObjectName("favoritesView")

        self.setup_ui()
        self.loadFavorites()

    def setup_ui(self):

        mainLayout = QVBoxLayout()
        mainLayout.setContentsMargins(30, 30, 30, 30)
        mainLayout.setSpacing(12)

        self.setLayout(mainLayout)

        titleLabel = QLabel("Favorites")
        titleLabel.setObjectName("favoritesTitle")
        titleLabel.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        mainLayout.addWidget(titleLabel)

        self.movieList = QListWidget()
        self.movieList.setObjectName(
            "favoritesMovieList"
        )

        mainLayout.addWidget(
            self.movieList
        )

    def loadFavorites(self):

        self.movieList.clear()

        favorites = self.service.getFavorites()

        if not favorites:
            item = QListWidgetItem(
                "No favorite movies yet."
            )
            self.movieList.addItem(item)
            return

        for movie in favorites:

            movieId = movie[0]
            title = movie[1]
            genre = movie[2]
            year = movie[3]
            rating = movie[4]
            status = movie[5]

            text = (
                f"{title}  |  "
                f"{genre}  |  "
                f"{year}  |  "
                f"Rating: {rating}  |  "
                f"{status}"
            )

            item = QListWidgetItem(text)

            item.setData(
                Qt.ItemDataRole.UserRole,
                movieId
            )

            self.movieList.addItem(item)

    def refresh(self):
        self.loadFavorites()