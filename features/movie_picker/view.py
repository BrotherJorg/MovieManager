from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton
)
from PyQt6.QtCore import Qt


class MoviePickerView(QWidget):

    def __init__(self, service):
        super().__init__()

        self.service = service

        self.setWindowTitle("Movie Picker")
        self.resize(500, 350)

        self.setup_ui()

    def setup_ui(self):

        layout = QVBoxLayout()
        self.setLayout(layout)

        titleLabel = QLabel("Movie Picker")
        titleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        titleLabel.setObjectName("moviePickerTitle")

        self.movieLabel = QLabel(
            "Click the button to pick a movie."
        )
        self.movieLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.movieLabel.setMinimumHeight(150)
        self.movieLabel.setObjectName("moviePickerResult")

        pickButton = QPushButton("Pick a Movie")
        pickButton.setObjectName("moviePickerButton")

        layout.addStretch()

        layout.addWidget(titleLabel)

        layout.addSpacing(15)

        layout.addWidget(
            self.movieLabel,
            alignment=Qt.AlignmentFlag.AlignHCenter
        )

        layout.addSpacing(15)

        layout.addWidget(
            pickButton,
            alignment=Qt.AlignmentFlag.AlignHCenter
        )

        layout.addStretch()

        pickButton.clicked.connect(
            self.pickMovie
        )

    def pickMovie(self):

        movie = self.service.getRandomMovie()

        if movie is None:
            self.movieLabel.setText(
                "No movies available."
            )
            return

        movie_id = movie[0]
        title = movie[1]
        genre = movie[2]
        year = movie[3]
        rating = movie[4]
        status = movie[5]

        self.movieLabel.setText(
            f"{title} ({year})\n"
            f"Genre: {genre}\n"
            f"Rating: {rating}\n"
            f"Status: {status}"
        )