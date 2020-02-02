import typing
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QStyleOptionGraphicsItem, QGraphicsItem
from wpath import WPath


class WGLine(QtWidgets.QGraphicsPathItem):
    def __init__(self, line: QtCore.QLineF):
        super(WGLine, self).__init__()
        self.wline = WPath.WLineF(line)
        self.bound = self.wline.w_bounding_rect()
        self.setFlag(QtWidgets.QGraphicsPathItem.ItemIsMovable)
        self.setPath(self.wline)

#    def mousePressEvent(self, event: 'QGraphicsSceneMouseEvent') -> None:
#        print('mouse pressed on item')

