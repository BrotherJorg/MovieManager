from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel
)


class RecommendationsView(QWidget):

    def __init__(self, service):
        super().__init__()

        self.service = service

        self.setWindowTitle("Recommendations")
        self.resize(500, 400)

        self.setup_ui()
        self.loadRecommendations()

    def setup_ui(self):

        layout = QVBoxLayout()

        titleLabel = QLabel("Movie Recommendations")

        self.recommendationsLabel = QLabel()

        layout.addWidget(titleLabel)
        layout.addWidget(self.recommendationsLabel)

        self.setLayout(layout)

    def loadRecommendations(self):

        recommendations = self.service.getRecommendations()

        if not recommendations:
            self.recommendationsLabel.setText(
                "No recommendations available."
            )
            return

        text = ""

        for recommendation in recommendations:

            movie = recommendation.movie

            text += (
                f"{movie[1]} ({movie[3]})\n"
                f"Genre: {movie[2]}\n"
                f"Rating: {movie[4]}\n"
                f"{recommendation.reason}\n\n"
            )

        self.recommendationsLabel.setText(text)