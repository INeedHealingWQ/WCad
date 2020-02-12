# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WCadUiFrame.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(924, 656)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("  QMainWindow::separator {\n"
"      background: yellow;\n"
"      width: 10px; /* when vertical */\n"
"      height: 10px; /* when horizontal */\n"
"  }\n"
"\n"
"  QMainWindow::separator:hover {\n"
"      background: red;\n"
"  }\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.stackedWidget = WStackedWidget(self.centralwidget)
        self.stackedWidget.setMinimumSize(QtCore.QSize(160, 250))
        self.stackedWidget.setMaximumSize(QtCore.QSize(160, 250))
        self.stackedWidget.setObjectName("stackedWidget")
        self.line_page = QtWidgets.QWidget()
        self.line_page.setObjectName("line_page")
        self.groupBox_3 = QtWidgets.QGroupBox(self.line_page)
        self.groupBox_3.setGeometry(QtCore.QRect(0, 20, 161, 231))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox_3.setStyleSheet("  QGroupBox {\n"
"      background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                        stop: 0 #E0E0E0, stop: 1 #FFFFFF);\n"
"      border: 2px solid gray;\n"
"      border-radius: 5px;\n"
"      margin-top: 1ex; /* leave space at the top for the title */\n"
"  }\n"
"\n"
"  QGroupBox::title {\n"
"      subcontrol-origin: margin;\n"
"      subcontrol-position: top center; /* position at the top center */\n"
"      padding: 0 3px;\n"
"      background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                        stop: 0 #FF0ECE, stop: 1 #FFFFFF);\n"
"  }")
        self.groupBox_3.setObjectName("groupBox_3")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox_3)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 30, 153, 70))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout_2 = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setStyleSheet("  QFrame, QLabel, QToolTip {\n"
"      border: 2px solid green;\n"
"      border-radius: 4px;\n"
"      padding: 2px;\n"
"  }")
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.line_para_length = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.line_para_length.setStyleSheet("")
        self.line_para_length.setMinimum(-10000.0)
        self.line_para_length.setMaximum(10000.0)
        self.line_para_length.setSingleStep(0.01)
        self.line_para_length.setObjectName("line_para_length")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.line_para_length)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setStyleSheet("  QFrame, QLabel, QToolTip {\n"
"      border: 2px solid green;\n"
"      border-radius: 4px;\n"
"      padding: 2px;\n"
"  }")
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.line_para_angle = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.line_para_angle.setStyleSheet("")
        self.line_para_angle.setMinimum(-360.0)
        self.line_para_angle.setMaximum(360.0)
        self.line_para_angle.setSingleStep(0.01)
        self.line_para_angle.setObjectName("line_para_angle")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.line_para_angle)
        self.stackedWidget.addWidget(self.line_page)
        self.circle_page = QtWidgets.QWidget()
        self.circle_page.setObjectName("circle_page")
        self.groupBox_2 = QtWidgets.QGroupBox(self.circle_page)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 20, 151, 231))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox_2.setObjectName("groupBox_2")
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget1.setGeometry(QtCore.QRect(0, 30, 147, 31))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget1)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.layoutWidget1)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBox)
        self.stackedWidget.addWidget(self.circle_page)
        self.gridLayout.addWidget(self.stackedWidget, 1, 0, 1, 1)
        self.graphicsView = WGraphicsView(self.centralwidget, self)
        self.graphicsView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.graphicsView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.graphicsView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.graphicsView.setBackgroundBrush(brush)
        self.graphicsView.setDragMode(QtWidgets.QGraphicsView.NoDrag)
        self.graphicsView.setResizeAnchor(QtWidgets.QGraphicsView.NoAnchor)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 0, 1, 3, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setMinimumSize(QtCore.QSize(160, 80))
        self.groupBox_4.setStyleSheet("  QGroupBox {\n"
"      background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                        stop: 0 #E0E0E0, stop: 1 #FFFFFF);\n"
"      border: 2px solid gray;\n"
"      border-radius: 5px;\n"
"      margin-top: 1ex; /* leave space at the top for the title */\n"
"  }\n"
"\n"
"  QGroupBox::title {\n"
"      subcontrol-origin: margin;\n"
"      subcontrol-position: top center; /* position at the top center */\n"
"      padding: 0 3px;\n"
"      background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                        stop: 0 #FF0ECE, stop: 1 #FFFFFF);\n"
"  }")
        self.groupBox_4.setObjectName("groupBox_4")
        self.layoutWidget2 = QtWidgets.QWidget(self.groupBox_4)
        self.layoutWidget2.setGeometry(QtCore.QRect(0, 30, 153, 33))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.formLayout_3 = QtWidgets.QFormLayout(self.layoutWidget2)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_info_pos_prompt = QtWidgets.QLabel(self.layoutWidget2)
        self.label_info_pos_prompt.setStyleSheet("  QFrame, QLabel, QToolTip {\n"
"      border: 2px solid green;\n"
"      border-radius: 4px;\n"
"      padding: 2px;\n"
"  }")
        self.label_info_pos_prompt.setObjectName("label_info_pos_prompt")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_info_pos_prompt)
        self.label_info_pos = QtWidgets.QLabel(self.layoutWidget2)
        self.label_info_pos.setStyleSheet("  QFrame, QLabel, QToolTip {\n"
"      border: 2px solid green;\n"
"      border-radius: 4px;\n"
"      padding: 2px;\n"
"  }")
        self.label_info_pos.setObjectName("label_info_pos")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_info_pos)
        self.gridLayout.addWidget(self.groupBox_4, 2, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setMinimumSize(QtCore.QSize(160, 250))
        self.groupBox.setMaximumSize(QtCore.QSize(160, 250))
        self.groupBox.setStyleSheet("  QGroupBox {\n"
"      background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                        stop: 0 #E0E0E0, stop: 1 #FFFFFF);\n"
"      border: 2px solid gray;\n"
"      border-radius: 5px;\n"
"      margin-top: 1ex; /* leave space at the top for the title */\n"
"  }\n"
"\n"
"  QGroupBox::title {\n"
"      subcontrol-origin: margin;\n"
"      subcontrol-position: top center; /* position at the top center */\n"
"      padding: 0 3px;\n"
"      background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                        stop: 0 #FF0ECE, stop: 1 #FFFFFF);\n"
"  }")
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.line_btn = QtWidgets.QPushButton(self.groupBox)
        self.line_btn.setEnabled(True)
        self.line_btn.setGeometry(QtCore.QRect(10, 30, 84, 28))
        self.line_btn.setAutoFillBackground(False)
        self.line_btn.setStyleSheet("QPushButton {\n"
"    border: 2px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                        stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                        stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgba(100,255,100,100);\n"
"border-color:rgba(255,255,255,200);\n"
"color:rgba(0,0,0,200);\n"
"};")
        self.line_btn.setCheckable(False)
        self.line_btn.setAutoRepeat(False)
        self.line_btn.setAutoDefault(False)
        self.line_btn.setDefault(False)
        self.line_btn.setFlat(False)
        self.line_btn.setObjectName("line_btn")
        self.circle_btn = QtWidgets.QPushButton(self.groupBox)
        self.circle_btn.setGeometry(QtCore.QRect(10, 70, 84, 28))
        self.circle_btn.setStyleSheet("QPushButton {\n"
"    border: 2px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                        stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                        stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgba(100,255,100,100);\n"
"border-color:rgba(255,255,255,200);\n"
"color:rgba(0,0,0,200);\n"
"};")
        self.circle_btn.setObjectName("circle_btn")
        self.ruler_length = QtWidgets.QPushButton(self.groupBox)
        self.ruler_length.setGeometry(QtCore.QRect(10, 170, 84, 31))
        self.ruler_length.setStyleSheet("QPushButton {\n"
"    border: 2px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                        stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                        stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgba(100,255,100,100);\n"
"border-color:rgba(255,255,255,200);\n"
"color:rgba(0,0,0,200);\n"
"};")
        self.ruler_length.setObjectName("ruler_length")
        self.ruler_angle = QtWidgets.QPushButton(self.groupBox)
        self.ruler_angle.setGeometry(QtCore.QRect(10, 210, 84, 31))
        self.ruler_angle.setStyleSheet("QPushButton {\n"
"    border: 2px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                        stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                        stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgba(100,255,100,100);\n"
"border-color:rgba(255,255,255,200);\n"
"color:rgba(0,0,0,200);\n"
"};")
        self.ruler_angle.setObjectName("ruler_angle")
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 924, 22))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menubar.sizePolicy().hasHeightForWidth())
        self.menubar.setSizePolicy(sizePolicy)
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.label_3.setBuddy(self.doubleSpinBox)
        self.label.setBuddy(self.doubleSpinBox)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.line_btn.clicked.connect(self.graphicsView.create_w_line)
        self.line_btn.clicked.connect(self.stackedWidget.set_index_to_line)
        self.circle_btn.clicked.connect(self.stackedWidget.set_index_to_circle)
        self.circle_btn.clicked.connect(self.graphicsView.create_w_circle)
        self.ruler_length.clicked.connect(self.graphicsView.create_w_ruler_length)
        self.ruler_angle.clicked.connect(self.graphicsView.create_w_ruler_angle)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_3.setTitle(_translate("MainWindow", "直线参数"))
        self.label_3.setText(_translate("MainWindow", "长度"))
        self.label_4.setText(_translate("MainWindow", "角度"))
        self.groupBox_2.setTitle(_translate("MainWindow", "圆参数"))
        self.label.setText(_translate("MainWindow", "半径"))
        self.groupBox_4.setTitle(_translate("MainWindow", "信息"))
        self.label_info_pos_prompt.setText(_translate("MainWindow", "位置："))
        self.label_info_pos.setText(_translate("MainWindow", "0， 0"))
        self.groupBox.setTitle(_translate("MainWindow", "工具"))
        self.line_btn.setText(_translate("MainWindow", "直线"))
        self.circle_btn.setText(_translate("MainWindow", "圆"))
        self.ruler_length.setText(_translate("MainWindow", "刻度尺"))
        self.ruler_angle.setText(_translate("MainWindow", "量角器"))


from wgraphicsview.WGraphicsView import WGraphicsView
from wstackedwidget.WStackedWidget import WStackedWidget
