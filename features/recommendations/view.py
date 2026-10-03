from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel
)
from PyQt6.QtCore import Qt


class RecommendationsView(QWidget):

    def __init__(self, service):
        super().__init__()

        self.service = service

        self.setWindowTitle("Recommendations")
        self.resize(600, 600)

        self.setup_ui()
        self.loadRecommendations()

    def setup_ui(self):

       
        mainLayout = QVBoxLayout()
        self.setLayout(mainLayout)

        title = QLabel("Recommendations")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        mainLayout.addWidget(title)

        description = QLabel("Movies you may want to watch")
        description.setAlignment(Qt.AlignmentFlag.AlignCenter)
        mainLayout.addWidget(description)

        self.recommendationsLayout = QVBoxLayout()
        mainLayout.addLayout(self.recommendationsLayout, 1)


    def loadRecommendations(self):

        recommendations = self.service.getRecommendations()

        if not recommendations:
            self.recommendationsLayout.addWidget(
                QLabel("No recommendations available.")
            )
            return

        for recommendation in recommendations:

            movie = recommendation.movie

            card = QWidget()
            card.setFixedWidth(500)

            cardLayout = QVBoxLayout(card)

            titleLabel = QLabel(
                movie[1]
            )

            detailsLabel = QLabel(
                f"{movie[2]} • {movie[3]}"
            )

            ratingLabel = QLabel(
                f"Rating: {movie[4]}"
            )

            reasonLabel = QLabel(
                recommendation.reason
            )

            cardLayout.addWidget(titleLabel)
            cardLayout.addWidget(detailsLabel)
            cardLayout.addWidget(ratingLabel)
            cardLayout.addWidget(reasonLabel)

            self.recommendationsLayout.addWidget(
                card,
                alignment=Qt.AlignmentFlag.AlignHCenter
            )