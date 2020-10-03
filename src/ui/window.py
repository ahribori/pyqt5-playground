from PyQt5.QtWidgets import QMainWindow, QTabWidget

from src.ui.tab.basic import BasicTab
from src.ui.tab.list import ListTab


class Window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setGeometry(30, 50, 1000, 800)
        self.tab = QTabWidget()
        self.setCentralWidget(self.tab)
        self._initTab()

    def _initTab(self):
        self.tab.addTab(BasicTab(), 'Basic')
        self.tab.addTab(ListTab(), 'List')
