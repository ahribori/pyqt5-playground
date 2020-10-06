from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QBoxLayout, QPushButton, QSplitter, QLabel, QGridLayout, QLineEdit, QTextEdit, \
    QVBoxLayout


class BasicTab(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        vbox = QVBoxLayout()
        self.setLayout(vbox)

        button1 = QPushButton('Button1')
        button1.setStyleSheet('background-color: red; color:white; padding: 8px;')
        vbox.addWidget(button1)
        vbox.addWidget(QPushButton('Button2'))
        vbox.addWidget(QPushButton('Button3'))
