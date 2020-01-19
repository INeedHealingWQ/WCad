from PyQt5.QtGui import QPainterPath
from PyQt5.QtCore import QPointF, QLineF


class QCadLineF(QPainterPath):
    def __init__(self, line_f):
        super().__init__()
        self.delta = 5.0
        self.line = QLineF(line_f)
        self.moveTo(self.line.p1())
        self.lineTo(self.line.p2())

        # self.prompt_path = QPainterPath()
        # self.prompt_path.addEllipse(self.line.p1(), self.delta, self.delta)
        # self.prompt_path.addEllipse(self.line.p2(), self.delta, self.delta)
        # self.prompt_path.addEllipse(self.line.center(), self.delta, self.delta)
