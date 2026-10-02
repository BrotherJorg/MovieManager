from PyQt6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QLabel,
    QTextEdit,
    QPushButton,
    QHBoxLayout
)


class ReviewNotesView(QDialog):
    
    def __init__(self, movie, service):
        super().__init__()

        self.movie = movie
        self.service = service

        self.setWindowTitle("Review and Notes")
        self.resize(600, 500)

        self.setup_ui()
        self.loadReviewNotes()

    def setup_ui(self):
        layout = QVBoxLayout()

        movieLabel = QLabel(
            f"{self.movie.title} ({self.movie.title})" 
        )

        reviewLabel = QLabel("Review")
        self.reviewInput = QTextEdit()
        self.reviewInput.setPlaceholderText("Enter review...")

        notesLabel = QLabel("Notes")
        self.notesInput = QTextEdit()
        self.notesInput.setPlaceholderText("Enter note...")

        buttonLayout = QHBoxLayout()
        saveButton = QPushButton("Save")
        cancelButton = QPushButton("Cancel")

        buttonLayout.addStretch()
        buttonLayout.addWidget(cancelButton)
        buttonLayout.addWidget(saveButton)

        layout.addWidget(movieLabel)
        layout.addWidget(reviewLabel)
        layout.addWidget(self.reviewInput)
        layout.addWidget(notesLabel)
        layout.addWidget(self.notesInput)
        layout.addLayout(buttonLayout)

        self.setLayout(layout)
        
        saveButton.clicked.connect(self.saveReviewNotes)
        cancelButton.clicked.connect(self.reject)


    def loadReviewNotes(self):
        reviewNotes = self.service.getReviewNotes(
            self.movie.id
        )
        if reviewNotes is not None:
            self.reviewInput.setPlainText(
                reviewNotes.review or ""
            )

            self.notesInput.setPlainText(
                reviewNotes.notes or ""
            )

    def saveReviewNotes(self):
        review = self.reviewInput.toPlainText()
        notes = self.notesInput.toPlainText()

        self.service.saveReviewNotes(
            self.movie.id,
            review,
            notes
        )

        self.accept()
    

