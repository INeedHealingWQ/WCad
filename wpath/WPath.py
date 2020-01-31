from PyQt5 import QtCore
from PyQt5.QtGui import QPainterPath
from PyQt5.QtCore import QPointF, QLineF


class WLineF(QPainterPath):
    def __init__(self, linef:QLineF):
        super().__init__()
        self.moveTo(linef.p1())
        self.lineTo(linef.p2())

    def w_bounding_rect(self):
        print(self.boundingRect())
        return self.boundingRect()
