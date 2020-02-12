from PyQt5.QtCore import Qt, QLineF, QPointF
from PyQt5.QtGui import QMouseEvent, QTransform
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene
from wgraphicsitem.WGraphicsItem import WGLine
from wtypes import WToolTypes
from PyQt5.QtGui import QPainterPath
from sympy import tan, pi
from wmath import geometry


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
    def __init__(self, view: QGraphicsView, scene: QGraphicsScene, len: float, ang: float):
        super(WToolLine, self).__init__(view, scene)
        self.start_point = None
        self.tool_type = WToolTypes.WToolTypes.LINE

        self.length = len
        self.angle = (-ang / 180) * pi


    def mouse_press_event_handler(self, event: QMouseEvent):
        if self.prompt_point is not None:
            pos = self.prompt_point
            self.prompt_point = None
        else:
            pos = self.view.mapToScene(event.pos())
        if event.button() == Qt.LeftButton:
            if self.length != 0:
                end = geometry.calc_end(pos, self.angle, self.length)
                self._final_item = WGLine(QLineF(pos, end), tmp=False)
                self.scene.addItem(self._final_item)
                self.__done()
                return
            if self._init_flag is False:
                self.start_point = pos
                self._init_flag = True
            else:
                self._final_item = WGLine(QLineF(self.start_point, pos), tmp=False)
                self.scene.addItem(self._final_item)
                self.__done()

        elif event.button() == Qt.RightButton:
            if self.length != 0:
                self.__done()
            if self._init_flag is True:
                self.__destroy_tmp()
                self._init_flag = False
                self.start_point = None

    def mouse_move_event_handler(self, event: QMouseEvent):
        pos = self.view.mapToScene(event.pos())
        if self.length != 0:
            self.__destroy_tmp()
            end = geometry.calc_end(pos, self.angle, self.length)
            self._tmp_item = WGLine(QLineF(pos, end), tmp=True)
            self.scene.addItem(self._tmp_item)
            self.scene.update()
            return
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


class WToolRulerLength(WToolObj):
    def __init__(self, view: QGraphicsView, scene: QGraphicsScene):
        super(WToolRulerLength, self).__init__(view, scene)
        self.tool_type = WToolTypes.WToolTypes.RULER_LENGTH

        self.init_flag = False
        self.done_flag = False
        self.start_point = None
        self.end_point = None
        self._tmp_item = []

    def mouse_press_event_handler(self, event: QMouseEvent):
        pos = self.view.mapToScene(event.pos())
        if event.button() ==  Qt.LeftButton:
            if self.done_flag is True:
                p1, p2 = geometry.calc_baseline(self.start_point, self.end_point, pos)
                self.scene.addLine(QLineF(p1, p2))
            elif self.init_flag is False:
                if self.prompt_point is not None:
                    self.start_point = self.prompt_point
                else:
                    self.start_point = pos
                self.init_flag = True
            else:
                if self.prompt_point is not None:
                    self.end_point = self.prompt_point
                else:
                    self.end_point = pos
                self.done_flag = True

    def mouse_move_event_handler(self, event: QMouseEvent):
        pos = self.view.mapToScene(event.pos())
        if self.done_flag is True:
            self.__destroy_tmp()
            p1, p2 = geometry.calc_baseline(self.start_point, self.end_point, pos)
            tmp1 = WGLine(QLineF(p1, p2), tmp=True)
            a1, a2 = geometry.calc_line_side_arrow_points(self.start_point, self.end_point, pos)
            tmp2 = WGLine(QLineF(self.start_point, a1), tmp=True)
            tmp3 = WGLine(QLineF(self.end_point, a2), tmp=True)
            prompt1, prompt2 = geometry.calc_prompt_perpendicular_line(self.start_point, self.end_point, pos)
            if prompt1 is not None:
                tmp4 = WGLine(QLineF(self.start_point, prompt1), tmp=True)
                tmp5 = WGLine(QLineF(self.end_point, prompt2), tmp=True)
                self._tmp_item.append(tmp4)
                self._tmp_item.append(tmp5)
                self.scene.addItem(tmp4)
                self.scene.addItem(tmp5)
            self._tmp_item.append(tmp1)
            self._tmp_item.append(tmp2)
            self._tmp_item.append(tmp3)
            self.scene.addItem(tmp1)
            self.scene.addItem(tmp2)
            self.scene.addItem(tmp3)


    def __destroy_tmp(self):
        if self._tmp_item != []:
            for i in self._tmp_item:
                self.scene.removeItem(i)
            self._tmp_item = []
