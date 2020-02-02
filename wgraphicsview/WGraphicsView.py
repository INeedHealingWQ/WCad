from PyQt5 import QtWidgets, QtGui
from PyQt5 import QtCore
from wgraphicsview.WGraphicsScene import WGraphicsScene


class WGraphicsView(QtWidgets.QGraphicsView):
    def __init__(self, parent):
        super().__init__()
        self.setParent(parent)
        self.scene = WGraphicsScene()
        self.setScene(self.scene)
        self.__init_attr()
        self.__init_signal()
        self.current_tool = 0

    def __init_signal(self):
        pass

    def __init_attr(self):
        self.setMouseTracking(True)
        self.setAttribute(QtCore.Qt.WA_AcceptTouchEvents)
        self.setViewportMargins(20, 20, 20, 20)

    def polyline(self):
        self.scene.polyline()
#    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
#        self.scene.mousePressEvent(event)
#        print('mouse pressed in view')
#
#    def mouseMoveEvent(self, event: QtGui.QMouseEvent) -> None:
#        pos = event.pos()
#        pos = self.mapToScene(pos)
