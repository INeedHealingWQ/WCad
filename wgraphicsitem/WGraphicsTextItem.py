import typing
from PyQt5 import QtGui
from PyQt5.QtWidgets import QGraphicsTextItem, QWidget, QStyleOptionGraphicsItem


class WGraphicsTextItem(QGraphicsTextItem):
    def __init__(self, text: str, ang_deg: float):
        super(WGraphicsTextItem, self).__init__(text)
        self.ang_deg = ang_deg

    def paint(self, painter: QtGui.QPainter, option: 'QStyleOptionGraphicsItem',
              widget: typing.Optional[QWidget] = ...) -> None:
        painter.rotate(self.ang_deg)
        super(WGraphicsTextItem, self).paint(painter, option, widget)
