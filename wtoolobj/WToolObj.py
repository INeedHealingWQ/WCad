from PyQt5.QtCore import Qt, QLineF, QPointF
from PyQt5.QtGui import QMouseEvent, QTransform
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene
from wgraphicsitem.WGraphicsItem import WGLine
from wtypes import WToolTypes
from PyQt5.QtGui import QPainterPath


class WToolObj:
    def __init__(self, view: QGraphicsView, scene: QGraphicsScene):
        self.view = view
        self.scene = scene
        self._tmp_item = None
        self._final_item = None
        self._init_flag = False
        self._done_flag = False
        self.tool_type = None
        self.prompt_point = None

    def is_done(self):
        return self._done_flag

    def mouse_press_event_handler(self, event: QMouseEvent):
        raise NotImplementedError

    def mouse_move_event_handler(self, event: QMouseEvent):
        raise NotImplementedError

    def drop(self):
        pass


class WToolCircle(WToolObj):
    def __init__(self, view: QGraphicsView, scene: QGraphicsScene):
        super(WToolCircle, self).__init__(view, scene)
        self.tool_type = WToolTypes.WToolTypes.CIRCLE

    def mouse_move_event_handler(self, event: QMouseEvent):
        pass

    def mouse_press_event_handler(self, event: QMouseEvent):
        pass


class WToolLine(WToolObj):
    def __init__(self, view: QGraphicsView, scene: QGraphicsScene):
        super(WToolLine, self).__init__(view, scene)
        self.start_point = None
        self.tool_type = WToolTypes.WToolTypes.LINE

    def mouse_press_event_handler(self, event: QMouseEvent):
        if self.prompt_point is not None:
            pos = self.prompt_point
            self.prompt_point = None
        else:
            pos = self.view.mapToScene(event.pos())
        if event.button() == Qt.LeftButton:
            if self._init_flag is False:
                self.start_point = pos
                self._init_flag = True
            else:
                self._final_item = WGLine(QLineF(self.start_point, pos), tmp=False)
                self.scene.addItem(self._final_item)
                self.__done()

        elif event.button() == Qt.RightButton:
            if self._init_flag is True:
                self.__destroy_tmp()
                self._init_flag = False
                self.start_point = None

    def mouse_move_event_handler(self, event: QMouseEvent):
        pos = self.view.mapToScene(event.pos())
        if self._init_flag is True:
            self.__destroy_tmp()
            self._tmp_item = WGLine(QLineF(self.start_point, pos), tmp=True)
            self.scene.addItem(self._tmp_item)
            ''' for unknown reason, sometimes part of the scene can not updata  '''
            self.scene.update()

    def drop(self):
        self.__destroy_tmp()

    def __destroy_tmp(self):
        if self._tmp_item is not None:
            self.scene.removeItem(self._tmp_item)
            self._tmp_item = None

    def __done(self):
        if self._tmp_item is not None:
            self.scene.removeItem(self._tmp_item)
        self._tmp_item = self._final_item = None
        self._done_flag = True
