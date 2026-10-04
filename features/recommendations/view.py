from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QScrollArea
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
        title.setObjectName("recommendationPageTitle")
        title.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        mainLayout.addWidget(title)

        description = QLabel(
            "Movies you may want to watch"
        )

        description.setObjectName(
            "recommendationPageDescription"
        )

        description.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        mainLayout.addWidget(description)

        # Scrollable recommendation area

        self.scrollArea = QScrollArea()
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )
        self.scrollArea.setVerticalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAsNeeded
        )

        # Content widget inside the scroll area

        self.scrollContent = QWidget()

        self.recommendationsLayout = QVBoxLayout(
            self.scrollContent
        )

        self.recommendationsLayout.setAlignment(
            Qt.AlignmentFlag.AlignTop
        )

        self.scrollArea.setWidget(
            self.scrollContent
        )

        mainLayout.addWidget(
            self.scrollArea,
            1
        )

    def loadRecommendations(self):

        # Remove previous recommendation cards

        while self.recommendationsLayout.count():

            item = self.recommendationsLayout.takeAt(0)

            widget = item.widget()

            if widget is not None:
                widget.deleteLater()

        recommendations = (
            self.service.getRecommendations()
        )

        if not recommendations:

            emptyLabel = QLabel(
                "No recommendations available."
            )

            emptyLabel.setAlignment(
                Qt.AlignmentFlag.AlignCenter
            )

            self.recommendationsLayout.addWidget(
                emptyLabel
            )

            return

        for recommendation in recommendations:

            movie = recommendation.movie

            card = QWidget()
            card.setObjectName(
                "recommendationCard"
            )
            card.setFixedWidth(500)

            cardLayout = QVBoxLayout(card)

            titleLabel = QLabel(movie[1])
            titleLabel.setObjectName(
                "recommendationTitle"
            )

            detailsLabel = QLabel(
                f"{movie[2]} • {movie[3]}"
            )

            detailsLabel.setObjectName(
                "recommendationDetails"
            )

            ratingLabel = QLabel(
                f"Rating: {movie[4]}"
            )

            ratingLabel.setObjectName(
                "recommendationRating"
            )

            reasonLabel = QLabel(
                recommendation.reason
            )

            reasonLabel.setObjectName(
                "recommendationReason"
            )

            cardLayout.addWidget(titleLabel)
            cardLayout.addWidget(detailsLabel)
            cardLayout.addWidget(ratingLabel)
            cardLayout.addWidget(reasonLabel)

            self.recommendationsLayout.addWidget(
                card,
                alignment=Qt.AlignmentFlag.AlignHCenter
            )

        # Keep the cards starting from the top

        self.recommendationsLayout.addStretch()

    def refresh(self):
        self.loadRecommendations()