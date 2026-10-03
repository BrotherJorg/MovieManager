from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QFrame
)
from PyQt6.QtCore import Qt


class DashboardView(QWidget):

    def __init__(self, service):
        super().__init__()

        self.service = service

        self.setWindowTitle("Dashboard")
        self.resize(900, 600)

        self.setup_ui()
        self.loadDashboard()

    def setup_ui(self):

        mainLayout = QVBoxLayout()
        self.setLayout(mainLayout)

        # TITLE

        title = QLabel("Dashboard")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        mainLayout.addWidget(title)

        # STATISTICS

        statsLayout = QHBoxLayout()

        moviesCard = QFrame()
        moviesLayout = QVBoxLayout(moviesCard)

        moviesTitle = QLabel("Movies")
        self.moviesValue = QLabel("0")
        self.moviesValue.setAlignment(Qt.AlignmentFlag.AlignCenter)

        moviesLayout.addWidget(moviesTitle)
        moviesLayout.addWidget(self.moviesValue)

        watchedCard = QFrame()
        watchedLayout = QVBoxLayout(watchedCard)

        watchedTitle = QLabel("Watched")
        self.watchedValue = QLabel("0")
        self.watchedValue.setAlignment(Qt.AlignmentFlag.AlignCenter)

        watchedLayout.addWidget(watchedTitle)
        watchedLayout.addWidget(self.watchedValue)

        watchingCard = QFrame()
        watchingLayout = QVBoxLayout(watchingCard)

        watchingTitle = QLabel("Watching")
        self.watchingValue = QLabel("0")
        self.watchingValue.setAlignment(Qt.AlignmentFlag.AlignCenter)

        watchingLayout.addWidget(watchingTitle)
        watchingLayout.addWidget(self.watchingValue)

        statsLayout.addWidget(moviesCard)
        statsLayout.addWidget(watchedCard)
        statsLayout.addWidget(watchingCard)

        mainLayout.addLayout(statsLayout)

        # STATISTICS AREA

        statisticsLayout = QHBoxLayout()

        genreFrame = QFrame()
        genreLayout = QVBoxLayout(genreFrame)

        genreTitle = QLabel("Genre Statistics")
        genreTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        genreLayout.addWidget(genreTitle)

        self.genreLabel = QLabel()
        self.genreLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        genreLayout.addWidget(self.genreLabel)

        statusFrame = QFrame()
        statusLayout = QVBoxLayout(statusFrame)

        statusTitle = QLabel("Status Statistics")
        statusTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        statusLayout.addWidget(statusTitle)

        self.statusLabel = QLabel()
        self.statusLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        statusLayout.addWidget(self.statusLabel)

        statisticsLayout.addWidget(genreFrame)
        statisticsLayout.addWidget(statusFrame)

        mainLayout.addLayout(statisticsLayout, 1)

        # AVERAGE RATING

        self.averageRatingLabel = QLabel(
            "Average Rating: 0"
        )

        self.averageRatingLabel.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        mainLayout.addWidget(self.averageRatingLabel)

    def loadDashboard(self):

        stats = self.service.getStats()

        self.moviesValue.setText(
            str(stats.totalMovies)
        )

        self.watchedValue.setText(
            str(stats.watched)
        )

        self.watchingValue.setText(
            str(stats.watching)
        )

        self.averageRatingLabel.setText(
            f"Average Rating: {stats.averageRating:.1f}"
        )

        genreText = ""

        for genre, count in stats.genreCounts.items():
            genreText += f"{genre}: {count}\n"

        self.genreLabel.setText(genreText)

        statusText = (
            f"Watched: {stats.watched}\n"
            f"Watching: {stats.watching}\n"
            f"Unwatched: {stats.unwatched}"
        )

        self.statusLabel.setText(statusText)