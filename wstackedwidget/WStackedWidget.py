from PyQt5.QtWidgets import QStackedWidget, QWidget
from PyQt5.QtCore import pyqtSlot
from wtypes.WToolTypes import WToolTypes


class WStackedWidget(QStackedWidget):
    def __init__(self, parent: QWidget):
        super(WStackedWidget, self).__init__()
        self.setParent(parent)

    def set_index_to_line(self):
        self.setCurrentIndex(WToolTypes.LINE)

    def set_index_to_circle(self):
        self.setCurrentIndex(WToolTypes.CIRCLE)