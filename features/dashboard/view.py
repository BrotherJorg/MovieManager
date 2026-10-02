from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QGroupBox
)


class DashboardView(QWidget):

    def __init__(self, service):
        super().__init__()

        self.service = service

        self.setup_ui()
        self.loadStats()

    def setup_ui(self):

        mainLayout = QVBoxLayout()

        titleLabel = QLabel("MovieOWL Dashboard")

        self.totalLabel = QLabel()
        self.watchedLabel = QLabel()
        self.watchingLabel = QLabel()
        self.unwatchedLabel = QLabel()
        self.averageRatingLabel = QLabel()

        statsLayout = QHBoxLayout()

        totalBox = QGroupBox("Total Movies")
        totalLayout = QVBoxLayout()
        totalLayout.addWidget(self.totalLabel)
        totalBox.setLayout(totalLayout)

        watchedBox = QGroupBox("Watched")
        watchedLayout = QVBoxLayout()
        watchedLayout.addWidget(self.watchedLabel)
        watchedBox.setLayout(watchedLayout)

        watchingBox = QGroupBox("Watching")
        watchingLayout = QVBoxLayout()
        watchingLayout.addWidget(self.watchingLabel)
        watchingBox.setLayout(watchingLayout)

        unwatchedBox = QGroupBox("Unwatched")
        unwatchedLayout = QVBoxLayout()
        unwatchedLayout.addWidget(self.unwatchedLabel)
        unwatchedBox.setLayout(unwatchedLayout)

        statsLayout.addWidget(totalBox)
        statsLayout.addWidget(watchedBox)
        statsLayout.addWidget(watchingBox)
        statsLayout.addWidget(unwatchedBox)

        ratingBox = QGroupBox("Average Rating")
        ratingLayout = QVBoxLayout()
        ratingLayout.addWidget(self.averageRatingLabel)
        ratingBox.setLayout(ratingLayout)

        genreBox = QGroupBox("Genre Breakdown")
        genreLayout = QVBoxLayout()

        self.genreLabel = QLabel()
        genreLayout.addWidget(self.genreLabel)

        genreBox.setLayout(genreLayout)

        mainLayout.addWidget(titleLabel)
        mainLayout.addLayout(statsLayout)
        mainLayout.addWidget(ratingBox)
        mainLayout.addWidget(genreBox)

        self.setLayout(mainLayout)

    def loadStats(self):

        stats = self.service.getStats()

        self.totalLabel.setText(str(stats.totalMovies))
        self.watchedLabel.setText(str(stats.watched))
        self.watchingLabel.setText(str(stats.watching))
        self.unwatchedLabel.setText(str(stats.unwatched))

        self.averageRatingLabel.setText(
            f"{stats.averageRating:.2f}"
        )

        genreText = ""

        for genre, count in stats.genreCounts.items():
            genreText += f"{genre}: {count}\n"

        self.genreLabel.setText(genreText)