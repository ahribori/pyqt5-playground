from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QBoxLayout, QPushButton, QSplitter, QLabel, QGridLayout, QLineEdit, QTextEdit, \
    QVBoxLayout


class BasicTab(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        vbox = QVBoxLayout()
        self.setLayout(vbox)

        vbox.addWidget(QPushButton('Button1'))
        vbox.addWidget(QPushButton('Button2'))
        vbox.addWidget(QPushButton('Button3'))
