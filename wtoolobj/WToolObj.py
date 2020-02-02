from PyQt5.QtGui import QPainterPath, QMouseEvent, QInputEvent
from PyQt5.QtCore import Qt


class WToolObj:
    def __init__(self):
        self.tmp_path = QPainterPath()
        self.final_path = None


class WToolLine(WToolObj):
    def __init__(self):
        super(WToolLine, self).__init__()

    def mouse_press_event_handler(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            if self.tmp_path.isEmpty() is True:
                self.tmp_path.moveTo(event.pos())
            else:
                self.final_path = self.tmp_path
                self.tmp_path = None
        elif event.button() == Qt.RightButton:
            self.tmp_path = QPainterPath()

    def mouse_move_event_handler(self, event: QMouseEvent):
        if self.tmp_path.isEmpty() is False:
            self.tmp_path.lineTo(event.pos())
