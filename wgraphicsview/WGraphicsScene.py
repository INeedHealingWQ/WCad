from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtWidgets import QGraphicsSceneDragDropEvent, QGraphicsSceneMouseEvent

from wgraphicsitem import WGraphicsItem


class WGraphicsScene(QtWidgets.QGraphicsScene):
    def __init__(self):
        super(WGraphicsScene, self).__init__()
#        line = WGraphicsItem.WGLine(QtCore.QLineF(0, 0, 100, 100))
        line_path = QtGui.QPainterPath()
        line_path.addRect(20, 20, 50, 50)
        line = QtWidgets.QGraphicsPathItem(line_path)
        self.addItem(line)

#    def mousePressEvent(self, event: 'QGraphicsSceneMouseEvent') -> None:
#        print('mouse pressed in scene')
#    def drawBackground(self, painter: QtGui.QPainter, rect: QtCore.QRectF) -> None:
#        painter.setBrush(QtCore.Qt.blue)
#        gradient = QtGui.QRadialGradient(0, 0, 10)
#        gradient.setSpread(QtGui.QGradient.RepeatSpread)
#        painter.setBackground(gradient)
