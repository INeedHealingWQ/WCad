from PyQt5.QtCore import Qt, QLineF
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene
from wgraphicsitem.WGraphicsItem import WGLine
from wgraphicsitem.WGraphicsTextItem import WGraphicsTextItem
from wtypes import WToolTypes
from math import pi
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
    def __init__(self, view: QGraphicsView, scene: QGraphicsScene, l: float, ang: float):
        super(WToolLine, self).__init__(view, scene)
        self.start_point = None
        self.tool_type = WToolTypes.WToolTypes.LINE

        self.length = l
        self.angle = (-ang / 180) * pi

    def mouse_press_event_handler(self, event: QMouseEvent):
        if self.prompt_point is not None:
            pos = self.prompt_point
            self.prompt_point = None
        else:
            pos = self.view.mapToScene(event.pos())
        if event.button() == Qt.LeftButton:
            if self.length != 0:
                end = geometry.calc_p2_from_p1(pos, self.angle, self.length)
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
            end = geometry.calc_p2_from_p1(pos, self.angle, self.length)
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
        self.per_prompt_done_flag = False
        self.baseline_prompt_done_flag = False
        self.text_done = False
        self.start_point = None
        self.end_point = None
        ''' in degrees '''
        self.angle = None
        self.prompt_baseline = None
        self.prompt_baseline_p1 = None
        self.prompt_baseline_p2 = None
        self.measure_line = None
        self._tmp_item = []

    def mouse_press_event_handler(self, event: QMouseEvent):
        pos = self.view.mapToScene(event.pos())
        if event.button() == Qt.LeftButton:
            if self.baseline_prompt_done_flag is True:
                arrow1, arrow2 = geometry.calc_line_side_arrow_points(
                    self.prompt_baseline_p1, self.prompt_baseline_p2, pos)
                arrow_1 = WGLine(QLineF(self.prompt_baseline_p1, arrow1), tmp=True)
                arrow_2 = WGLine(QLineF(self.prompt_baseline_p2, arrow2), tmp=True)
                self.scene.addItem(arrow_1)
                self.scene.addItem(arrow_2)
                length = '%.3f' % self.measure_line.length()
                text = length.__str__()
                length_item = WGraphicsTextItem(text, pos, self.angle)
                self.scene.addItem(length_item)
                self.text_done = True
                self.__done()
            elif self.per_prompt_done_flag is True:
                p1, p2 = geometry.calc_baseline(self.start_point, self.end_point, pos)
                self.prompt_baseline = WGLine(QLineF(p1, p2), tmp=False)
                self.prompt_baseline_p1 = p1
                self.prompt_baseline_p2 = p2
                self.scene.addItem(self.prompt_baseline)
                self.baseline_prompt_done_flag = True
            elif self.done_flag is True:
                prompt1, prompt2 = geometry.calc_prompt_perpendicular_line(self.start_point, self.end_point, pos)
                if prompt1 is not None:
                    per1 = WGLine(QLineF(self.start_point, prompt1), tmp=False)
                    per2 = WGLine(QLineF(self.end_point, prompt2), tmp=False)
                    self.scene.addItem(per1)
                    self.scene.addItem(per2)
                    self.per_prompt_done_flag = True
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
                self.measure_line = QLineF(self.start_point, self.end_point)
                self.angle = geometry.calc_angle_from_p1_to_p2(self.start_point, self.end_point, False)

    def mouse_move_event_handler(self, event: QMouseEvent):
        pos = self.view.mapToScene(event.pos())
        if self.text_done is True:
            self.__destroy_tmp()
        elif self.baseline_prompt_done_flag is True:
            self.__destroy_tmp()
            arrow1, arrow2 = geometry.calc_line_side_arrow_points(self.prompt_baseline_p1, self.prompt_baseline_p2, pos)
            tmp6 = WGLine(QLineF(self.prompt_baseline_p1, arrow1), tmp=True)
            tmp7 = WGLine(QLineF(self.prompt_baseline_p2, arrow2), tmp=True)
            self._tmp_item.append(tmp6)
            self._tmp_item.append(tmp7)
            self.scene.addItem(tmp6)
            self.scene.addItem(tmp7)
            text = '%.03f' % self.measure_line.length()
            length_item = WGraphicsTextItem(text, pos, self.angle)
            self._tmp_item.append(length_item)
            self.scene.addItem(length_item)
        elif self.per_prompt_done_flag is True:
            self.__destroy_tmp()
            p1, p2 = geometry.calc_baseline(self.start_point, self.end_point, pos)
            tmp1 = WGLine(QLineF(p1, p2), tmp=True)
            self._tmp_item.append(tmp1)
            self.scene.addItem(tmp1)
        elif self.done_flag is True:
            self.__destroy_tmp()
            prompt1, prompt2 = geometry.calc_prompt_perpendicular_line(self.start_point, self.end_point, pos)
            if prompt1 is not None:
                tmp4 = WGLine(QLineF(self.start_point, prompt1), tmp=True)
                tmp5 = WGLine(QLineF(self.end_point, prompt2), tmp=True)
                self._tmp_item.append(tmp4)
                self._tmp_item.append(tmp5)
                self.scene.addItem(tmp4)
                self.scene.addItem(tmp5)

    def __destroy_tmp(self):
        if self._tmp_item:
            for i in self._tmp_item:
                self.scene.removeItem(i)
            self._tmp_item = []

    def __done(self):
        if self._tmp_item is not None:
            for i in self._tmp_item:
                self.scene.removeItem(i)
        self._tmp_item = self._final_item = None
        self._done_flag = True
