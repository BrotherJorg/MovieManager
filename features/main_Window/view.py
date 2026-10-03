from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QStackedWidget
)


class MainWindow(QMainWindow):
    EXPANDED_WIDTH = 180
    COLLAPSED_WIDTH = 56

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
        mainLayout = QHBoxLayout(centralWidget)
        mainLayout.setContentsMargins(0, 0, 0, 0)
        mainLayout.setSpacing(0)


        # Sidebar should collapse
        self.sidebarWidget = QWidget()
        self.sidebarWidget.setFixedWidth(self.EXPANDED_WIDTH)

        sidebar = QVBoxLayout()
        sidebar.setSpacing(10)
        sidebar.setContentsMargins(10, 10, 10, 10)
        self.sidebarWidget.setLayout(sidebar)



        self.manageButton = QPushButton("Manage Movies")
        self.dashboardButton = QPushButton("Dashboard")
        self.moviePickerButton = QPushButton("Movie Picker")
        self.recommendationsButton = QPushButton("Recommendations")

        sidebar.addWidget(self.dashboardButton)
       
        sidebar.addWidget(self.manageButton)
       
        sidebar.addWidget(self.moviePickerButton)
        
        sidebar.addWidget(self.recommendationsButton)

        sidebar.addStretch()
        self.collapseButton = QPushButton("Collapse")
        self.collapseButton.clicked.connect(self.toggleSidebar)

        sidebar.addWidget(self.collapseButton)
        sidebar.addStretch()
       

        self.stack = QStackedWidget()

        self.stack.addWidget(self.manageMoviesView)
        self.stack.addWidget(self.dashboardView)
        self.stack.addWidget(self.moviePickerView)
        self.stack.addWidget(self.recommendationsView)

        mainLayout.addWidget(self.sidebarWidget)
        mainLayout.addWidget(self.stack, 1)

        centralWidget.setLayout(mainLayout)

        self.setCentralWidget(centralWidget)

        self.manageButton.clicked.connect(
            lambda: self.stack.setCurrentWidget(
                self.manageMoviesView
            )
        )

        self.dashboardButton.clicked.connect(
            lambda: self.stack.setCurrentWidget(
                self.dashboardView
            )
        )

        self.moviePickerButton.clicked.connect(
            lambda: self.stack.setCurrentWidget(
                self.moviePickerView
            )
        )

        self.recommendationsButton.clicked.connect(
            lambda: self.stack.setCurrentWidget(
                self.recommendationsView
            )
        )

        self.stack.setCurrentWidget(self.dashboardView)
    

    def toggleSidebar(self):

        if self.sidebarWidget.width() == self.EXPANDED_WIDTH:

            self.sidebarWidget.setFixedWidth( self.COLLAPSED_WIDTH)

            self.manageButton.setText("M")
            self.dashboardButton.setText("D")
            self.moviePickerButton.setText("P")
            self.recommendationsButton.setText("R")
            self.collapseButton.setText(">>")

        else:

            self.sidebarWidget.setFixedWidth(self.EXPANDED_WIDTH)

            self.manageButton.setText("Manage Movies")
            self.dashboardButton.setText("Dashboard")
            self.moviePickerButton.setText("Movie Picker")
            self.recommendationsButton.setText("Recommendations")
            self.collapseButton.setText("Collapse")