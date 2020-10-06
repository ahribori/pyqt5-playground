from PyQt5.QtWidgets import QMainWindow, QTabWidget

from src.ui.tab.basic import BasicTab
from src.ui.tab.chart import ChartTab
from src.ui.tab.draw import DrawTab
from src.ui.tab.grid import GridTab
from src.ui.tab.plt import MatPlotLibTab
from src.ui.tab.table import TableTab


class Window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setGeometry(30, 50, 1000, 800)
        self.tab = QTabWidget()
        self.setCentralWidget(self.tab)
        self._initTab()

    def _initTab(self):
        self.tab.addTab(BasicTab(), 'Basic')
        self.tab.addTab(TableTab(), 'Table')
        self.tab.addTab(GridTab(), 'Grid')
        self.tab.addTab(ChartTab(), 'Chart')
        self.tab.addTab(DrawTab(), 'Draw')
        self.tab.addTab(MatPlotLibTab(), 'Matplotlib')
        self.tab.setCurrentIndex(5)
