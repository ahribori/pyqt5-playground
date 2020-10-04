from random import random, randint

from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QWidget, QBoxLayout, QTableWidget, QTableWidgetItem


class TableTab(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.layout = QBoxLayout(QBoxLayout.TopToBottom)
        self.table = QTableWidget(self)
        self.table.horizontalHeader().hide()
        self.table.verticalHeader().hide()
        self.table.setRowCount(3)
        self.table.setColumnCount(3)
        self.table.adjustSize()
        self.setItem(0, 1, "(0,1)")
        self.setLabelItem(0, 0, "(0,0)")
        self.setLabelItem(1, 0, "(1,0)")
        self.setItem(1, 1, "(1,1)")
        self.layout.addWidget(self.table)

        interval = QTimer(self)
        interval.setInterval(100)
        interval.timeout.connect(self._interval)
        interval.start()

        self.table.itemSelectionChanged.connect(lambda: print("cellPressed"))

    def setItem(self, row, col, data):
        item = QTableWidgetItem(data)
        item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        self.table.setItem(row, col, item)

    def setLabelItem(self, row, col, data):
        item = QTableWidgetItem(data)
        item.setFlags(Qt.ItemIsSelectable)
        self.table.setItem(row, col, item)

    def _interval(self):
        self.setItem(2, 0, randint(0, 100).__str__())
