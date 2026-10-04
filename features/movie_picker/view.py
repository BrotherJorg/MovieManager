from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QFrame
)
from PyQt6.QtCore import Qt


class MoviePickerView(QWidget):

    def __init__(self, service):
        super().__init__()

        self.service = service

        self.setObjectName("moviePickerView")

        self.setup_ui()

    def setup_ui(self):

        layout = QVBoxLayout()
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(12)
        self.setLayout(layout)

        # Page header

        titleLabel = QLabel("Movie Picker")
        titleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        titleLabel.setObjectName("moviePickerTitle")

        descriptionLabel = QLabel(
            "Randomly select a movie from your collection"
        )
        descriptionLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        descriptionLabel.setObjectName("moviePickerDescription")

        # Result card

        resultCard = QFrame()
        resultCard.setObjectName("moviePickerCard")

        resultLayout = QHBoxLayout(resultCard)

        self.posterLabel = QLabel()
        self.posterLabel.setObjectName("moviePickerPoster")
        self.posterLabel.setFixedSize(120, 180)

        infoLayout = QVBoxLayout()

        self.movieTitleLabel = QLabel("No movie selected")
        self.movieTitleLabel.setObjectName("moviePickerMovieTitle")

        self.movieDetailsLabel = QLabel()
        self.movieDetailsLabel.setObjectName("moviePickerDetails")

        self.movieRatingLabel = QLabel()
        self.movieRatingLabel.setObjectName("moviePickerRating")

        self.movieStatusLabel = QLabel()
        self.movieStatusLabel.setObjectName("moviePickerStatus")

        infoLayout.addWidget(self.movieTitleLabel)
        infoLayout.addWidget(self.movieDetailsLabel)
        infoLayout.addSpacing(8)
        infoLayout.addWidget(self.movieRatingLabel)
        infoLayout.addWidget(self.movieStatusLabel)
        infoLayout.addStretch()

        resultLayout.addWidget(self.posterLabel)
        resultLayout.addLayout(infoLayout)

        # Pick button

        pickButton = QPushButton("Pick a Movie")
        pickButton.setObjectName("moviePickerButton")

        # Main layout

        layout.addStretch()

        layout.addWidget(titleLabel)

        layout.addWidget(descriptionLabel)

        layout.addSpacing(15)

        layout.addWidget(
            resultCard,
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
            self.movieTitleLabel.setText("No movies available.")
            self.movieDetailsLabel.setText("")
            self.movieRatingLabel.setText("")
            self.movieStatusLabel.setText("")
            self.posterLabel.setText("No Poster")
            return

        movie_id = movie[0]
        title = movie[1]
        genre = movie[2]
        year = movie[3]
        rating = movie[4]
        status = movie[5]

        self.posterLabel.setText("POSTER")

        self.movieTitleLabel.setText(title)

        self.movieDetailsLabel.setText(
            f"{genre} • {year}"
        )

        self.movieRatingLabel.setText(
            f"Rating: {rating}"
        )

        self.movieStatusLabel.setText(
            f"Status: {status}"
        )