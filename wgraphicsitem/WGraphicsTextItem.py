import typing
from PyQt5 import QtGui
from PyQt5.QtCore import QPointF
from PyQt5.QtWidgets import QGraphicsTextItem, QWidget, QStyleOptionGraphicsItem
from wmath import geometry
from math import radians
from PyQt5.QtGui import QFontMetricsF, QFont


class WGraphicsTextItem(QGraphicsTextItem):
    def __init__(self, text: str, pos: QPointF, ang_deg: float):
        super(WGraphicsTextItem, self).__init__()
        self.ang_deg = ang_deg
        self.pos = pos
        self.setPlainText(text)
        self.text = text
        self.setTextWidth(15 * len(text))

    def paint(self, painter: QtGui.QPainter, option: 'QStyleOptionGraphicsItem',
              widget: typing.Optional[QWidget] = ...) -> None:
        painter.rotate(self.ang_deg)
        self.setPos(self.pos)
        return super(WGraphicsTextItem, self).paint(painter, option, widget)

    def boundingRect(self):
        ret = super(WGraphicsTextItem, self).boundingRect()
        font_metrics = QFontMetricsF(self.font())
        rect = font_metrics.boundingRectChar(self.text)
        print('font rect: ', rect)
        print('super rect: ', ret)
        return rect
#        return super(WGraphicsTextItem, self).boundingRect()

