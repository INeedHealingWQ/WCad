from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtWidgets import QGraphicsSceneDragDropEvent, QGraphicsSceneMouseEvent
from wgraphicsitem import WGraphicsItem
from wgraphicsitem.WGraphicsTextItem import WGraphicsTextItem


class WGraphicsScene(QtWidgets.QGraphicsScene):
    def __init__(self):
        super(WGraphicsScene, self).__init__()
        self.current_tool = None

    def mouseMoveEvent(self, event: 'QGraphicsSceneMouseEvent') -> None:
        super(WGraphicsScene, self).mouseMoveEvent(event)

    def mousePressEvent(self, event: 'QGraphicsSceneMouseEvent') -> None:
        super(WGraphicsScene, self).mousePressEvent(event)

    def drawBackground(self, painter: QtGui.QPainter, rect: QtCore.QRectF) -> None:
        ret = super(WGraphicsScene, self).drawBackground(painter, rect)
        painter.setOpacity(0.2)
#        axis = [QtCore.QLineF(self.sceneRect().x(), 0, self.sceneRect().width(), 0),
#                QtCore.QLineF(0, self.sceneRect().y(), 0, self.sceneRect().height())]
#        painter.drawLines(axis)
        return ret

