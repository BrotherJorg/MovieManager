from PyQt6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QLabel,
    QComboBox,
    QPushButton
)

class WatchStatusView(QDialog):
    def __init__(self, service, movie, parent=None):
        super().__init__(parent)

        self.service = service
        self.movie = movie

        self.setWindowTitle("Watch Status")

        layout = QVBoxLayout()
        self.setLayout(layout)

        layout.addWidget(QLabel(f"Movie: {movie.title}"))

        self.statusCombo = QComboBox()
        self.statusCombo.addItems([
            "Unwatched",
            "Watching",
            "Watched"
        ])

        self.statusCombo.setCurrentText(movie.status)
        layout.addWidget(self.statusCombo)

        saveButton = QPushButton("Save")
        saveButton.clicked.connect(self.saveStatus)

        
        layout.addWidget(saveButton)
        

    def saveStatus(self):
        
        status = self.statusCombo.currentText()

        self.service.updateStatus(
            self.movie.id,
            status
        )

        self.accept()