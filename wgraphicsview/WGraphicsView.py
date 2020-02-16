from PyQt5 import QtWidgets, QtGui
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QWheelEvent, QPaintEvent
from wgraphicsview.WGraphicsScene import WGraphicsScene
from wtoolobj.WToolObj import WToolLine, WToolCircle, WToolRulerLength
from Ui.WCadUiFrame import Ui_MainWindow


class WGraphicsView(QtWidgets.QGraphicsView):
    def __init__(self, parent: QtWidgets.QWidget, ui: Ui_MainWindow):
        super().__init__()
        self.setParent(parent)
        self.ui = ui
        self.scene = WGraphicsScene()
        self.setScene(self.scene)
#        ''' When added first item, the scene rect changed and the content will scroll away, so set it first '''
#        self.scene.setSceneRect(QtCore.QRectF(-self.width(), -self.height(),
#                                              self.width(), self.height()))
        self.__init_attr()
        self.current_tool = None

    def __init_attr(self):
        self.setMouseTracking(True)
        self.setAttribute(QtCore.Qt.WA_AcceptTouchEvents)
        self.setDragMode(QtWidgets.QGraphicsView.ScrollHandDrag)
        self.setViewportMargins(0, 0, 0, 0)
        self.setStatusTip('绘图区域')

    def create_w_line(self):
        if self.current_tool is not None:
            self.current_tool.drop()
        self.current_tool = WToolLine(self, self.scene, self.ui.line_para_length.value(), self.ui.line_para_angle.value())
        self.scene.current_tool = self.current_tool

    def create_w_circle(self):
        if self.current_tool is not None:
            self.current_tool.drop()
        self.current_tool = WToolCircle(self, self.scene)
        self.scene.current_tool = self.current_tool

    def create_w_ruler_length(self):
        if self.current_tool is not None:
            self.current_tool.drop()
        self.current_tool = WToolRulerLength(self, self.scene)
        self.scene.current_tool = self.current_tool

    def create_w_ruler_angle(self):
        pass

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        ret = super(WGraphicsView, self).mousePressEvent(event)
        if self.current_tool is not None:
            self.current_tool.mouse_press_event_handler(event)
            self.check_done()
#        pos = self.mapToScene(event.pos())
#        scene_rect = self.sceneRect()
#        if abs(pos.x() - scene_rect.left()) <= 10 \
#                or abs(pos.x() - scene_rect.right()) <= 10 \
#                or abs(pos.y() - scene_rect.top()) <= 10 \
#                or abs(pos.y() - scene_rect.bottom()) <= 10:
#            top_left = QtCore.QPointF(scene_rect.topLeft().x() - 10, scene_rect.topLeft().y() - 10)
#            bottom_right = QtCore.QPointF(scene_rect.bottomRight().x() + 10, scene_rect.bottomRight().y() + 10)
#            self.setSceneRect(QtCore.QRectF(top_left, bottom_right))
#        self.adjust_scene_rect(scene_rect)
        return ret

    def mouseMoveEvent(self, event: QtGui.QMouseEvent) -> None:
        ret = super(WGraphicsView, self).mouseMoveEvent(event)
        if self.current_tool is not None:
            self.current_tool.mouse_move_event_handler(event)
            self.check_done()
        pos = self.mapToScene(event.pos())
        pos_str = "%d, %d" % (pos.x(), pos.y())
        self.ui.label_info_pos.setText(pos_str)
#        scene_rect = self.sceneRect()
#        if abs(pos.x() - scene_rect.left()) <= 10 \
#                or abs(pos.x() - scene_rect.right()) <= 10 \
#                or abs(pos.y() - scene_rect.top()) <= 10 \
#                or abs(pos.y() - scene_rect.bottom()) <= 10:
#            top_left = QtCore.QPointF(scene_rect.topLeft().x() - 10, scene_rect.topLeft().y() - 10)
#            bottom_right = QtCore.QPointF(scene_rect.bottomRight().x() + 10, scene_rect.bottomRight().y() + 10)
#            self.setSceneRect(QtCore.QRectF(top_left, bottom_right))
#        self.adjust_scene_rect(scene_rect)
        return ret

    def check_done(self):
        if self.current_tool is not None and self.current_tool.is_done() is True:
            self.current_tool = None
            self.scene.current_tool = None

    def drawBackground(self, painter: QtGui.QPainter, rect: QtCore.QRectF) -> None:
        ret = super(WGraphicsView, self).drawBackground(painter, rect)
        painter.setOpacity(0.2)
        axis = [QtCore.QLineF(-self.maximumWidth() / 2, 0, self.maximumWidth(), 0),
                QtCore.QLineF(0, -self.maximumHeight(), 0, self.maximumHeight())]
        painter.drawLines(axis)
        return ret

    def adjust_scene_rect(self, rect: QtCore.QRectF):
        """ Always make scene rect in center """
        top_left = rect.topLeft()
        bottom_right = rect.bottomRight()
        max_x_set_to = max(abs(top_left.x()), abs(bottom_right.x()))
        max_y_set_to = max(abs(top_left.y()), abs(bottom_right.y()))
        top_left_set_to = QtCore.QPointF(-max_x_set_to, -max_y_set_to)
        bottom_right_set_to = QtCore.QPointF(max_x_set_to, max_y_set_to)
        self.setSceneRect(QtCore.QRectF(top_left_set_to, bottom_right_set_to))
