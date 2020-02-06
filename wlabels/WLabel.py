from PyQt5.QtWidgets import QLabel, QWidget


class WLabel(QLabel):
    def __init__(self, parent: QWidget):
        super(WLabel, self).__init__()
        self.setParent(parent)
