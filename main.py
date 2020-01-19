import sys
from PyQt5 import QtWidgets
from Ui import QCadUiFrame


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_win = QtWidgets.QMainWindow()
    qcad_ui_frame = QCadUiFrame.Ui_MainWindow()
    qcad_ui_frame.setupUi(main_win)
    main_win.setMouseTracking(True)
    main_win.show()
    sys.exit(app.exec_())
