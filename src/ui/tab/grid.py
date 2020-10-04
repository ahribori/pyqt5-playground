from PyQt5.QtWidgets import QWidget, QTextEdit, QLineEdit, QLabel, QGridLayout, QBoxLayout


class GridTab(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.layout = QBoxLayout(QBoxLayout.LeftToRight)

        grid = QGridLayout()
        self.setLayout(grid)

        grid.addWidget(QLabel('Title:'), 0, 0)
        grid.addWidget(QLabel('Author:'), 1, 0)
        grid.addWidget(QLabel('Review:'), 2, 0)

        grid.addWidget(QLineEdit(), 0, 1)
        grid.addWidget(QLineEdit(), 1, 1)
        grid.addWidget(QTextEdit(), 2, 1)
