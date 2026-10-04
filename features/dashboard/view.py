from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QFrame,
    QScrollArea
)
from PyQt6.QtCore import Qt


class DashboardView(QWidget):

    def __init__(self, service):
        super().__init__()

        self.service = service

        self.setWindowTitle("Dashboard")
        self.resize(900, 600)
        self.setObjectName("dashboardView")

        self.setup_ui()
        self.loadDashboard()

    def setup_ui(self):

        mainLayout = QVBoxLayout()
        mainLayout.setContentsMargins(20, 20, 20, 20)
        mainLayout.setSpacing(12)
        self.setLayout(mainLayout)

        title = QLabel("Dashboard")
        title.setObjectName("dashboardTitle")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        mainLayout.addWidget(title)

        statsLayout = QHBoxLayout()
        statsLayout.setSpacing(12)

        moviesCard = QFrame()
        moviesCard.setObjectName("dashboardCard")
        moviesLayout = QVBoxLayout(moviesCard)

        moviesTitle = QLabel("Movies")
        moviesTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.moviesValue = QLabel("0")
        self.moviesValue.setObjectName("dashboardValue")
        self.moviesValue.setAlignment(Qt.AlignmentFlag.AlignCenter)

        moviesLayout.addWidget(moviesTitle)
        moviesLayout.addWidget(self.moviesValue)

        watchedCard = QFrame()
        watchedCard.setObjectName("dashboardCard")
        watchedLayout = QVBoxLayout(watchedCard)

        watchedTitle = QLabel("Watched")
        watchedTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.watchedValue = QLabel("0")
        self.watchedValue.setObjectName("dashboardValue")
        self.watchedValue.setAlignment(Qt.AlignmentFlag.AlignCenter)

        watchedLayout.addWidget(watchedTitle)
        watchedLayout.addWidget(self.watchedValue)

        watchingCard = QFrame()
        watchingCard.setObjectName("dashboardCard")
        watchingLayout = QVBoxLayout(watchingCard)

        watchingTitle = QLabel("Watching")
        watchingTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.watchingValue = QLabel("0")
        self.watchingValue.setObjectName("dashboardValue")
        self.watchingValue.setAlignment(Qt.AlignmentFlag.AlignCenter)

        watchingLayout.addWidget(watchingTitle)
        watchingLayout.addWidget(self.watchingValue)

        statsLayout.addWidget(moviesCard)
        statsLayout.addWidget(watchedCard)
        statsLayout.addWidget(watchingCard)

        mainLayout.addLayout(statsLayout)

        statisticsLayout = QHBoxLayout()
        statisticsLayout.setSpacing(12)

        genreFrame = QFrame()
        genreFrame.setObjectName("dashboardSection")
        genreFrame.setFixedHeight(250)

        genreLayout = QVBoxLayout(genreFrame)
        genreLayout.setContentsMargins(12, 12, 12, 12)
        genreLayout.setSpacing(8)

        genreTitle = QLabel("Genre Statistics")
        genreTitle.setObjectName("dashboardSectionTitle")
        genreTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        genreLayout.addWidget(genreTitle)

        genreScroll = QScrollArea()
        genreScroll.setWidgetResizable(True)

        genreScroll.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )

        genreScroll.setVerticalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAsNeeded
        )

        genreContent = QWidget()

        genreContentLayout = QVBoxLayout(genreContent)
        genreContentLayout.setContentsMargins(4, 4, 4, 4)

        self.genreLabel = QLabel()

        self.genreLabel.setAlignment(
            Qt.AlignmentFlag.AlignLeft |
            Qt.AlignmentFlag.AlignTop
        )

        self.genreLabel.setWordWrap(True)

        genreContentLayout.addWidget(self.genreLabel)
        genreContentLayout.addStretch()

        genreScroll.setWidget(genreContent)

        genreLayout.addWidget(genreScroll)

        statusFrame = QFrame()
        statusFrame.setObjectName("dashboardSection")
        statusFrame.setFixedHeight(250)

        statusLayout = QVBoxLayout(statusFrame)
        statusLayout.setContentsMargins(12, 12, 12, 12)
        statusLayout.setSpacing(8)

        statusTitle = QLabel("Status Statistics")
        statusTitle.setObjectName("dashboardSectionTitle")
        statusTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        statusLayout.addWidget(statusTitle)

        self.statusLabel = QLabel()

        self.statusLabel.setAlignment(
            Qt.AlignmentFlag.AlignLeft |
            Qt.AlignmentFlag.AlignTop
        )

        statusLayout.addWidget(self.statusLabel)
        statusLayout.addStretch()

        statisticsLayout.addWidget(genreFrame)
        statisticsLayout.addWidget(statusFrame)

        mainLayout.addLayout(statisticsLayout)

        averageRatingCard = QFrame()
        averageRatingCard.setObjectName("dashboardCard")

        averageRatingLayout = QVBoxLayout(averageRatingCard)

        averageRatingTitle = QLabel("Average Rating")
        averageRatingTitle.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.averageRatingLabel = QLabel("0.0")
        self.averageRatingLabel.setObjectName("dashboardValue")
        self.averageRatingLabel.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        averageRatingDescription = QLabel(
            "Average rating across your movie collection"
        )

        averageRatingDescription.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        averageRatingDescription.setWordWrap(True)

        averageRatingLayout.addWidget(averageRatingTitle)
        averageRatingLayout.addWidget(self.averageRatingLabel)
        averageRatingLayout.addWidget(
            averageRatingDescription
        )

        mainLayout.addWidget(averageRatingCard)

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
            f"{stats.averageRating:.1f}"
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

    def refresh(self):
        self.loadDashboard()
