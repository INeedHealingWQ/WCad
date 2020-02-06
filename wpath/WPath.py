from PyQt5.QtGui import QPainterPath
from PyQt5.QtCore import QPointF, QLineF


class WCircle(QPainterPath):
    def __init__(self, pos: QPointF, r: float):
        super(WCircle, self).__init__()
        self.pos = pos
        self.r = r
        self.draw_path()

    def draw_path(self):
        self.addEllipse(self.pos, self.r, self.r)


class WLineF(QPainterPath):
    def __init__(self, line_f: QLineF):
        super().__init__()
        self.start_point = line_f.p1()
        self.end_point = line_f.p2()
        self.mid_point = line_f.center()
        self.draw_path()

    def draw_path(self):
        self.moveTo(self.start_point)
        self.lineTo(self.end_point)

#    def w_bounding_rect(self):
#        return self.boundingRect()
