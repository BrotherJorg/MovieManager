from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton
)


class MoviePickerView(QWidget):

    def __init__(self, service):
        super().__init__()

        self.service = service

        self.setWindowTitle("Movie Picker")
        self.resize(500, 350)

        self.setup_ui()

    def setup_ui(self):

        layout = QVBoxLayout()

        titleLabel = QLabel("Movie Picker")

        self.movieLabel = QLabel(
            "Click the button to pick a movie."
        )

        pickButton = QPushButton("Pick a Movie")

        layout.addWidget(titleLabel)
        layout.addWidget(self.movieLabel)
        layout.addWidget(pickButton)

        self.setLayout(layout)

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