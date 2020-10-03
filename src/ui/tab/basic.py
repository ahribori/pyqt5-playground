from PyQt5.QtWidgets import QWidget, QBoxLayout, QLabel, QPushButton, QDockWidget


class BasicTab(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.layout = QBoxLayout(QBoxLayout.TopToBottom)
        button = QPushButton("&Button", self)
        button.setGeometry(10, 10, 100, 40)
        self.layout.addWidget(button)
