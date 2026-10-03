from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QStackedWidget
)


class MainWindow(QMainWindow):

    def __init__(
        self,
        manageMoviesView,
        dashboardView,
        moviePickerView,
        recommendationsView
    ):
        super().__init__()

        self.manageMoviesView = manageMoviesView
        self.dashboardView = dashboardView
        self.moviePickerView = moviePickerView
        self.recommendationsView = recommendationsView

        self.setWindowTitle("MovieOWL")
        self.resize(1000, 700)

        self.setup_ui()

    def setup_ui(self):

        centralWidget = QWidget()
        mainLayout = QHBoxLayout()

        sidebar = QVBoxLayout()

        manageButton = QPushButton("Manage Movies")
        dashboardButton = QPushButton("Dashboard")
        moviePickerButton = QPushButton("Movie Picker")
        recommendationsButton = QPushButton("Recommendations")

        sidebar.addWidget(manageButton)
        sidebar.addWidget(dashboardButton)
        sidebar.addWidget(moviePickerButton)
        sidebar.addWidget(recommendationsButton)
        sidebar.addStretch()

        self.stack = QStackedWidget()

        self.stack.addWidget(self.manageMoviesView)
        self.stack.addWidget(self.dashboardView)
        self.stack.addWidget(self.moviePickerView)
        self.stack.addWidget(self.recommendationsView)

        mainLayout.addLayout(sidebar)
        mainLayout.addWidget(self.stack)

        centralWidget.setLayout(mainLayout)

        self.setCentralWidget(centralWidget)

        manageButton.clicked.connect(
            lambda: self.stack.setCurrentWidget(
                self.manageMoviesView
            )
        )

        dashboardButton.clicked.connect(
            lambda: self.stack.setCurrentWidget(
                self.dashboardView
            )
        )

        moviePickerButton.clicked.connect(
            lambda: self.stack.setCurrentWidget(
                self.moviePickerView
            )
        )

        recommendationsButton.clicked.connect(
            lambda: self.stack.setCurrentWidget(
                self.recommendationsView
            )
        )