from datetime import datetime

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QComboBox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np
import matplotlib.dates as dt
from matplotlib.pyplot import plot_date
from mplfinance.original_flavor import candlestick_ohlc

"""
이벤트 목록
'button_press_event'	MouseEvent - mouse button is pressed
'button_release_event'	MouseEvent - mouse button is released
'draw_event'	DrawEvent - canvas draw (but before screen update)
'key_press_event'	KeyEvent - key is pressed
'key_release_event'	KeyEvent - key is released
'motion_notify_event'	MouseEvent - mouse motion
'pick_event'	PickEvent - an object in the canvas is selected
'resize_event'	ResizeEvent - figure canvas is resized
'scroll_event'	MouseEvent - mouse scroll wheel is rolled
'figure_enter_event'	LocationEvent - mouse enters a new figure
'figure_leave_event'	LocationEvent - mouse leaves a figure
'axes_enter_event'	LocationEvent - mouse enters a new axes
'axes_leave_event'	LocationEvent - mouse leaves an axes
"""


class MatPlotLibTab(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.fig = plt.Figure()
        self.canvas = FigureCanvas(self.fig)
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        cb = QComboBox()
        cb.addItem('Graph1')
        cb.addItem('Graph2')
        cb.addItem('Graph3')
        cb.activated[str].connect(self.onComboBoxChanged)
        layout.addWidget(cb)
        self.layout = layout
        self.onComboBoxChanged(cb.currentText())
        self.setLayout(self.layout)
        self.canvas.mpl_connect('button_press_event', lambda e: print(e))
        self.canvas.mpl_connect('scroll_event', lambda e: print(e))
        self.canvas.mpl_connect('motion_notify_event', self.onMouseMove)

    def onMouseMove(self, event):
        print(event)

    def onComboBoxChanged(self, text):
        if text == 'Graph1':
            self.doGraph1()
        elif text == 'Graph2':
            self.doGraph2()
        elif text == 'Graph3':
            self.doGraph3()

    def doGraph1(self):

        self.fig.clear()
        ax = self.fig.add_subplot(111)
        ax.xaxis.set_major_formatter(dt.DateFormatter('%H:%M'))
        ax.xaxis.set_minor_locator(dt.DayLocator())

        candleData = list(map(
            lambda item:
            [dt.date2num(datetime.strptime(item[4], '%Y%m%d%H%M%S')),
             get_integer_price(item[0]),
             get_integer_price(item[2]),
             get_integer_price(item[3]),
             get_integer_price(item[1])], data))
        print(candleData)
        candlestick_ohlc(ax, candleData, width=0.0018, colorup="r", colordown="b")
        ax.autoscale_view()
        self.canvas.draw()

    def doGraph2(self):
        x = np.arange(0, 10, 0.5)
        y1 = np.sin(x)
        y2 = np.cos(x)

        self.fig.clear()
        ax = self.fig.add_subplot(111)
        ax.plot(x, y1, label="sin(x)")
        ax.plot(x, y2, label="cos(x)", linestyle="--")

        ax.set_xlabel("x")
        ax.set_xlabel("y")
        ax.set_title("sin & cos")
        ax.legend()

        self.canvas.draw()

    def doGraph3(self):
        X = np.arange(-5, 5, 0.25)
        Y = np.arange(-5, 5, 0.25)
        X, Y = np.meshgrid(X, Y)
        Z = X ** 2 + Y ** 2

        self.fig.clear()

        ax = self.fig.gca(projection='3d')
        ax.plot_wireframe(X, Y, Z, color='black')
        self.canvas.draw()


def get_integer_price(str_price):
    return int(str_price.strip()[1:])


data = [['+6810', '+6810', '+6810', '+6810', '20200929153000'],
        ['+6870', '+6880', '+6940', '+6830', '20200929151500'],
        ['+6890', '+6910', '+6950', '+6810', '20200929151000'],
        ['+6910', '+6890', '+6970', '+6830', '20200929150500'],
        ['+6890', '+7000', '+7000', '+6800', '20200929150000'],
        ['+6990', '+7000', '+7020', '+6970', '20200929145500'],
        ['+7000', '+7000', '+7070', '+6980', '20200929145000'],
        ['+6990', '+6980', '+7020', '+6950', '20200929144500'],
        ['+6980', '+7020', '+7080', '+6940', '20200929144000'],
        ['+7020', '+7030', '+7080', '+6990', '20200929143500'],
        ['+7030', '+6930', '+7060', '+6920', '20200929143000'],
        ['+6930', '+6920', '+7000', '+6870', '20200929142500'],
        ['+6920', '+7040', '+7040', '+6870', '20200929142000'],
        ['+7040', '+7080', '+7090', '+6950', '20200929141500'],
        ['+7080', '+7210', '+7240', '+6980', '20200929141000'],
        ['+7200', '+7230', '+7270', '+7130', '20200929140500'],
        ['+7220', '+7480', '+7520', '+7170', '20200929140000'],
        ['+7480', '+7400', '+7500', '+7310', '20200929135500'],
        ['+7400', '+7220', '+7400', '+7190', '20200929135000'],
        ['+7210', '+7160', '+7240', '+7150', '20200929134500'],
        ['+7160', '+7220', '+7250', '+7150', '20200929134000'],
        ['+7230', '+7200', '+7270', '+7190', '20200929133500'],
        ['+7200', '+7120', '+7210', '+7100', '20200929133000'],
        ['+7120', '+7070', '+7120', '+7010', '20200929132500'],
        ['+7070', '+7140', '+7150', '+7040', '20200929132000'],
        ['+7140', '+7130', '+7190', '+7090', '20200929131500'],
        ['+7130', '+7060', '+7160', '+7040', '20200929131000'],
        ['+7060', '+6990', '+7090', '+6980', '20200929130500'],
        ['+6980', '+6990', '+7020', '+6970', '20200929130000'],
        ['+6990', '+6970', '+7000', '+6960', '20200929125500'],
        ['+6970', '+7000', '+7030', '+6960', '20200929125000'],
        ['+7000', '+6950', '+7050', '+6940', '20200929124500'],
        ['+6950', '+6970', '+6980', '+6930', '20200929124000'],
        ['+6970', '+6950', '+7010', '+6940', '20200929123500'],
        ['+6940', '+7010', '+7010', '+6940', '20200929123000'],
        ['+7000', '+7070', '+7070', '+6990', '20200929122500'],
        ['+7070', '+7050', '+7110', '+7020', '20200929122000'],
        ['+7040', '+6990', '+7060', '+6980', '20200929121500'],
        ['+6990', '+6980', '+7040', '+6980', '20200929121000'],
        ['+6970', '+6880', '+7000', '+6870', '20200929120500'],
        ['+6890', '+7030', '+7030', '+6880', '20200929120000'],
        ['+7020', '+7050', '+7050', '+6970', '20200929115500'],
        ['+7050', '+7110', '+7120', '+6980', '20200929115000'],
        ['+7100', '+7100', '+7130', '+7090', '20200929114500'],
        ['+7100', '+7100', '+7130', '+7060', '20200929114000'],
        ['+7100', '+7110', '+7170', '+7100', '20200929113500'],
        ['+7100', '+7150', '+7160', '+7070', '20200929113000'],
        ['+7140', '+7170', '+7180', '+7120', '20200929112500'],
        ['+7170', '+7180', '+7240', '+7150', '20200929112000'],
        ['+7170', '+7150', '+7220', '+7140', '20200929111500'],
        ['+7150', '+7240', '+7270', '+7120', '20200929111000'],
        ['+7230', '+7200', '+7250', '+7160', '20200929110500'],
        ['+7200', '+7110', '+7200', '+7110', '20200929110000'],
        ['+7120', '+7090', '+7170', '+7090', '20200929105500'],
        ['+7100', '+7160', '+7190', '+7060', '20200929105000'],
        ['+7160', '+7170', '+7230', '+7100', '20200929104500'],
        ['+7170', '+7100', '+7180', '+7070', '20200929104000'],
        ['+7100', '+7160', '+7190', '+7060', '20200929103500'],
        ['+7160', '+7250', '+7260', '+7150', '20200929103000'],
        ['+7250', '+7280', '+7340', '+7190', '20200929102500'],
        ['+7280', '+7120', '+7300', '+7100', '20200929102000'],
        ['+7110', '+7060', '+7160', '+7030', '20200929101500'],
        ['+7050', '+7130', '+7140', '+7010', '20200929101000'],
        ['+7120', '+7240', '+7350', '+7010', '20200929100500'],
        ['+7240', '+7320', '+7400', '+7220', '20200929100000'],
        ['+7340', '+7200', '+7370', '+7160', '20200929095500'],
        ['+7210', '+7120', '+7280', '+7050', '20200929095000'],
        ['+7120', '+7070', '+7120', '+7000', '20200929094500'],
        ['+7070', '+7030', '+7120', '+6980', '20200929094000'],
        ['+7030', '+6920', '+7070', '+6860', '20200929093500'],
        ['+6920', '+7070', '+7140', '+6900', '20200929093000'],
        ['+7070', '+7100', '+7120', '+6960', '20200929092500'],
        ['+7110', '+7180', '+7320', '+7100', '20200929092000'],
        ['+7190', '+7100', '+7200', '+6950', '20200929091500'],
        ['+7060', '+6750', '+7060', '+6740', '20200929091000'],
        ['+6750', '+6440', '+6750', '+6440', '20200929090500'],
        ['+6450', '+6420', '+6580', '-6330', '20200929090000']]
