import typing
from PyQt5 import QtGui
from PyQt5.QtCore import QPointF, QRectF
from PyQt5.QtWidgets import QGraphicsTextItem, QWidget, QStyleOptionGraphicsItem
from wmath import geometry
from math import degrees
from PyQt5.QtGui import QFontMetricsF, QFont
from wtypes import WToolTypes


class WGraphicsTextItem(QGraphicsTextItem):
    def __init__(self, text: str, pos: QPointF, angle: float):
        super(WGraphicsTextItem, self).__init__()
        self._item_type = WToolTypes.WItemTypes.PROMPT_TEXT
        self.angle = angle
        self.pos = pos
        self.text = text
        self.setPlainText(text)
        self.setPos(self.pos)
        self.setRotation(degrees(self.angle))
