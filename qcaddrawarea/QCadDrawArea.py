from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import math
import sympy


class QCadDrawArea(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.setParent(parent)
        self.path = QPainterPath()
        self.setAttribute(Qt.WA_AcceptTouchEvents)
        self.setMouseTracking(True)
        self.points = []
        self.lines = []
        ''' lines = [[startpoint(QPoint), endpoint(QPoint)], line, ang] '''
        self.current_start = QPoint(0, 0)
        self.current_end = QPoint(0, 0)
        self.is_linked = False
        self.prompt_circle = [0, QPoint(0, 0), 0]
        self.prompt_line = [0, QPoint(0, 0), 0]
        self.baseline = sympy.Line((0, 0), (1, 0))

    def initAxies(self, pen):
        pen.setPen(Qt.gray)
        pen.save()
        pen.translate(self.parent().width() / 2, self.parent().height() / 2)
        pen.drawLine(int(-self.parent().width() / 2), 0, int(self.parent().width() / 2), 0)
        pen.drawLine(0, int(self.parent().height() / 2), 0, int(-self.parent().height() / 2))
        pen.restore()

    def paintEvent(self, event):
        p = QPainter(self)
        self.initAxies(p)
        p.setPen(Qt.white)

        if self.get_prompt_circle_flag() == 1:
            p.save()
            p.setPen(Qt.red)
            p.drawEllipse(self.get_prompt_circle_point(),
                          self.get_prompt_circle_r(), self.get_prompt_circle_r())
            p.restore()
        elif self.get_prompt_line_flag() == 1:
            p.save()
            p.setPen(Qt.red)
            p.drawEllipse(self.get_prompt_line_point(),
                          self.get_prompt_line_r(), self.get_prompt_line_r())
            p.restore()

        for point_pair in self.points:
            p.drawLine(*point_pair)

        if self.is_linked is True:
            p.drawLine(self.current_start, self.current_end)

    def mouseMoveEvent(self, event):
        need_prompt = False
        need_line_prompt = False
        for point_pair in self.points:
            distance_0 = math.sqrt((event.x() - point_pair[0].x()) ** 2
                                   + (event.y() - point_pair[0].y()) ** 2)
            distance_1 = math.sqrt((event.x() - point_pair[1].x()) ** 2
                                   + (event.y() - point_pair[1].y()) ** 2)
            ''' here need optimization '''
            if distance_0 <= 10:
                self.set_prompt_circle(1, point_pair[0], 10)
                need_prompt = True
            elif distance_1 <= 10:
                self.set_prompt_circle(1, point_pair[1], 10)
                need_prompt = True
        if need_prompt is False:
            self.reset_prompt_circle()
            for line in self.lines:
                sym_point = sympy.Point(event.x(), event.y())
                dist = sym_point.distance(line[1])
                if dist < 5:
                    perpendicular_line = line[1].perpendicular_line(sym_point)
                    intersection_point = sympy.intersection(perpendicular_line, line[1])
                    Qpt = QPoint(int(intersection_point[0].args[0]), int(intersection_point[0].args[1]))
                    self.set_prompt_line(1, Qpt, 5)
                    need_line_prompt = True

        if need_line_prompt is False:
            self.reset_prompt_line()

        if self.is_linked is True:
            self.current_end = event.pos()
            print(event.globalPos())
            if event.x() > self.width():
                self.setGeometry(QRect(0, 0, 800, 800))

        self.update()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            if self.is_linked is False:
                self.is_linked = True
                self.current_start = self.current_end = event.pos()
            else:
                if self.get_prompt_circle_flag() == 1:
                    self.current_end = self.get_prompt_circle_point()
                elif self.get_prompt_line_flag() == 1:
                    self.current_end = self.get_prompt_line_point()
                if self.current_start != self.current_end:
                    self.points.append([self.current_start, self.current_end])
                    points = [self.current_start, self.current_end]
                    p1 = sympy.Point(self.current_start.x(), self.current_start.y())
                    p2 = sympy.Point(self.current_end.x(), self.current_end.y())
                    line = sympy.Line(p1, p2)
                    ang = line.angle_between(self.baseline)
                    ltmp = [points, line, ang]
                    self.lines.append(ltmp)
                    self.current_start = self.current_end = event.pos()

            if self.get_prompt_circle_flag() == 1:
                self.current_end = self.current_start = self.get_prompt_circle_point()
            elif self.get_prompt_line_flag() == 1:
                self.current_end = self.current_start = self.get_prompt_line_point()

        elif event.button() == Qt.RightButton:
            if self.is_linked is True:
                self.is_linked = False
        self.update()

    def mouseReleaseEvent(self, event):
        pass

    def reset_prompt_line(self):
        self.prompt_line[0] = 0
        self.prompt_line[1] = QPoint(0, 0)
        self.prompt_line[2] = 0

    def set_prompt_line(self, flag, point, r):
        self.prompt_line[0] = flag
        self.prompt_line[1] = point
        self.prompt_line[2] = r

    def get_prompt_line_flag(self):
        return self.prompt_line[0]

    def get_prompt_line_point(self):
        return self.prompt_line[1]

    def get_prompt_line_r(self):
        return self.prompt_line[2]

    def reset_prompt_circle(self):
        self.prompt_circle[0] = 0
        self.prompt_circle[1] = QPoint(0, 0)
        self.prompt_circle[2] = 0

    def set_prompt_circle(self, flag, point, r):
        self.prompt_circle[0] = flag
        self.prompt_circle[1] = point
        self.prompt_circle[2] = r

    def get_prompt_circle_flag(self):
        return self.prompt_circle[0]

    def get_prompt_circle_point(self):
        return self.prompt_circle[1]

    def get_prompt_circle_r(self):
        return self.prompt_circle[2]

