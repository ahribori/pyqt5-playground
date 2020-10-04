from random import randint

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtWidgets import QWidget


class DrawTab(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.qp = QPainter(self)

    def paintEvent(self, e):
        print('paint')
        self.qp.begin(self)

        pen = QPen(Qt.gray, 3)
        self.qp.setPen(pen)
        size = self.size()

        for i in range(700):
            x = randint(1, size.width() - 1)
            y = randint(1, size.height() - 1)
            self.qp.drawPoint(x, y)
        self.qp.end()
