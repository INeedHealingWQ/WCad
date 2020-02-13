import typing
from PyQt5 import QtGui
from PyQt5.QtCore import QPointF
from PyQt5.QtWidgets import QGraphicsTextItem, QWidget, QStyleOptionGraphicsItem
from wmath import geometry
from math import degrees
from PyQt5.QtGui import QFontMetricsF, QFont


class WGraphicsTextItem(QGraphicsTextItem):
    def __init__(self, text: str, pos: QPointF, angle: float):
        super(WGraphicsTextItem, self).__init__()
        self.angle = angle
        self.pos = pos
        self.text = text
        self.setPlainText(text)
        self.setPos(self.pos)

    def paint(self, painter: QtGui.QPainter, option: 'QStyleOptionGraphicsItem',
              widget: typing.Optional[QWidget] = ...) -> None:
        painter.rotate(degrees(self.angle))
        return super(WGraphicsTextItem, self).paint(painter, option, widget)

    def boundingRect(self):
        rect = super(WGraphicsTextItem, self).boundingRect()

        return geometry.calc_bounding_rect_of_common_rect(*(
            geometry.rotate_points( rect.topLeft(), rect.topRight(),
                                   rect.bottomLeft(), rect.bottomRight(), angle_in_rad=self.angle)
        ))

