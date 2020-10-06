from PyQt5.QtWidgets import QWidget, QVBoxLayout, QComboBox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np

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
        cb.activated[str].connect(self.onComboBoxChanged)
        layout.addWidget(cb)
        self.layout = layout
        self.onComboBoxChanged(cb.currentText())
        self.setLayout(self.layout)
        self.canvas.mpl_connect('button_press_event', lambda e: print(e))
        self.canvas.mpl_connect('scroll_event', lambda e: print(e))

    def onComboBoxChanged(self, text):
        if text == 'Graph1':
            self.doGraph1()
        elif text == 'Graph2':
            self.doGraph2()

    def doGraph1(self):
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

    def doGraph2(self):
        X = np.arange(-5, 5, 0.25)
        Y = np.arange(-5, 5, 0.25)
        X, Y = np.meshgrid(X, Y)
        Z = X ** 2 + Y ** 2

        self.fig.clear()

        ax = self.fig.gca(projection='3d')
        ax.plot_wireframe(X, Y, Z, color='black')
        self.canvas.draw()
