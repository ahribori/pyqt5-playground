from PyQt5.QtWidgets import QWidget, QLabel, QBoxLayout


class ListTab(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.layout = QBoxLayout(QBoxLayout.TopToBottom)
        text = QLabel('list')
        self.layout.addWidget(text)
        self.setVisible(True)
