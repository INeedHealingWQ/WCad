from PyQt5 import QtWidgets, QtGui
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication
from wgraphicsview.WGraphicsScene import WGraphicsScene
from wtoolobj.WToolObj import WToolLine, WToolCircle


class WGraphicsView(QtWidgets.QGraphicsView):
    def __init__(self, parent: QtWidgets.QWidget, ui: QtCore.QObject):
        super().__init__()
        self.setParent(parent)
        self.ui = ui
        self.scene = WGraphicsScene()
        self.setScene(self.scene)
        ''' When added first item, the scene rect changed and the content will scroll away, so set it first '''
        self.scene.setSceneRect(QtCore.QRectF(-self.width(), -self.height(),
                                              self.width(), self.height()))
        self.__init_attr()
        self.current_tool = None

    def __init_attr(self):
        self.setMouseTracking(True)
        self.setAttribute(QtCore.Qt.WA_AcceptTouchEvents)
        self.setDragMode(QtWidgets.QGraphicsView.ScrollHandDrag)
        self.setViewportMargins(20, 20, 20, 20)
        self.setStatusTip('绘图区域')

    def create_w_line(self):
        if self.current_tool is not None:
            self.current_tool.drop()
        self.current_tool = WToolLine(self, self.scene)
        self.scene.current_tool = self.current_tool

    def create_w_circle(self):
        if self.current_tool is not None:
            self.current_tool.drop()
        self.current_tool = WToolCircle(self, self.scene)
        self.scene.current_tool = self.current_tool

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        ret = super(WGraphicsView, self).mousePressEvent(event)
        if self.current_tool is not None:
            self.current_tool.mouse_press_event_handler(event)
            self.check_done()
        return ret

    def mouseMoveEvent(self, event: QtGui.QMouseEvent) -> None:
        ret = super(WGraphicsView, self).mouseMoveEvent(event)
        if self.current_tool is not None:
            print(self.scene.sceneRect())
            self.current_tool.mouse_move_event_handler(event)
            self.check_done()
        pos = self.mapToScene(event.pos())
        pos_str = "%d, %d" % (pos.x(), pos.y())
        self.ui.label_info_pos.setText(pos_str)
        return ret

    def check_done(self):
        if self.current_tool is not None and self.current_tool.is_done() is True:
            self.current_tool = None
            self.scene.current_tool = None

    def drawBackground(self, painter: QtGui.QPainter, rect: QtCore.QRectF) -> None:
        ret = super(WGraphicsView, self).drawBackground(painter, rect)
#        painter.setOpacity(0.2)
#        axis = [QtCore.QLineF(-self.maximumWidth() / 2, 0, self.maximumWidth(), 0),
#                QtCore.QLineF(0, -self.maximumHeight(), 0, self.maximumHeight())]
#        painter.drawLines(axis)
        return ret
