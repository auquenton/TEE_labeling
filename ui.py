# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\showvideo.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(832, 620)
        MainWindow.setStyleSheet("background-color:white;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.display_label = QtWidgets.QLabel(self.centralwidget)
        self.display_label.setGeometry(QtCore.QRect(40, 40, 368, 500))
        self.display_label.setStyleSheet("border-width: 1px;\n"
                                         "border-style: solid;\n"
                                         "border-color: rgb(0, 0, 0)")
        self.display_label.setText("")
        self.display_label.setObjectName("display_label")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(490, 60, 211, 438))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(
            QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.cls_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.cls_label.sizePolicy().hasHeightForWidth())
        self.cls_label.setSizePolicy(sizePolicy)
        self.cls_label.setObjectName("cls_label")
        self.verticalLayout.addWidget(self.cls_label)
        self.radioButton_0 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_0.setObjectName("radioButton_0")
        self.verticalLayout.addWidget(self.radioButton_0)
        self.radioButton_1 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_1.setObjectName("radioButton_1")
        self.verticalLayout.addWidget(self.radioButton_1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout.addWidget(self.radioButton_2)
        self.radioButton_3 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_3.setObjectName("radioButton_3")
        self.verticalLayout.addWidget(self.radioButton_3)
        self.radioButton_4 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_4.setObjectName("radioButton_4")
        self.verticalLayout.addWidget(self.radioButton_4)
        self.radioButton_5 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_5.setObjectName("radioButton_5")
        self.verticalLayout.addWidget(self.radioButton_5)
        self.radioButton_6 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_6.setObjectName("radioButton_6")
        self.verticalLayout.addWidget(self.radioButton_6)
        self.radioButton_7 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_7.setObjectName("radioButton_7")
        self.verticalLayout.addWidget(self.radioButton_7)
        self.radioButton_8 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_8.setObjectName("radioButton_8")
        self.verticalLayout.addWidget(self.radioButton_8)
        self.radioButton_9 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_9.setObjectName("radioButton_9")
        self.verticalLayout.addWidget(self.radioButton_9)
        self.radioButton_10 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_10.setObjectName("radioButton_10")
        self.verticalLayout.addWidget(self.radioButton_10)
        self.radioButton_11 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_11.setObjectName("radioButton_11")
        self.verticalLayout.addWidget(self.radioButton_11)
        self.radioButton_12 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_12.setObjectName("radioButton_12")
        self.verticalLayout.addWidget(self.radioButton_12)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(
            QtCore.QRect(590, 510, 161, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.prev_label = QtWidgets.QToolButton(self.horizontalLayoutWidget)
        self.prev_label.setStyleSheet(
            "border-width: 0px;border-width: 1px;border-style: solid")
        self.prev_label.setIconSize(QtCore.QSize(32, 32))
        self.prev_label.setArrowType(QtCore.Qt.LeftArrow)
        self.prev_label.setObjectName("prev_label")
        self.horizontalLayout.addWidget(self.prev_label)
        self.pos_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.pos_label.setScaledContents(True)
        self.pos_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pos_label.setObjectName("pos_label")
        self.horizontalLayout.addWidget(self.pos_label)
        self.next_label = QtWidgets.QToolButton(self.horizontalLayoutWidget)
        self.next_label.setStyleSheet(
            "border-width: 0px;border-width: 1px;border-style: solid")
        self.next_label.setIconSize(QtCore.QSize(32, 32))
        self.next_label.setArrowType(QtCore.Qt.RightArrow)
        self.next_label.setObjectName("next_label")
        self.horizontalLayout.addWidget(self.next_label)
        self.pred_info_label = QtWidgets.QLabel(self.centralwidget)
        self.pred_info_label.setGeometry(QtCore.QRect(80, 560, 251, 41))
        self.pred_info_label.setText("")
        self.pred_info_label.setScaledContents(True)
        self.pred_info_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pred_info_label.setObjectName("pred_info_label")
        self.filename_label = QtWidgets.QLabel(self.centralwidget)
        self.filename_label.setGeometry(QtCore.QRect(30, 10, 381, 16))
        self.filename_label.setText("")
        self.filename_label.setAlignment(QtCore.Qt.AlignCenter)
        self.filename_label.setObjectName("filename_label")
        self.radioButton_None = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_None.setGeometry(QtCore.QRect(490, 480, 51, 16))
        self.radioButton_None.setObjectName("radioButton_None")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(720, 60, 91, 431))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.quality_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.quality_label.sizePolicy().hasHeightForWidth())
        self.quality_label.setSizePolicy(sizePolicy)
        self.quality_label.setObjectName("quality_label")
        self.verticalLayout_2.addWidget(self.quality_label)
        self.radioButton_good = QtWidgets.QRadioButton(
            self.verticalLayoutWidget_2)
        self.radioButton_good.setObjectName("radioButton_good")
        self.verticalLayout_2.addWidget(self.radioButton_good)
        self.radioButton_bad = QtWidgets.QRadioButton(
            self.verticalLayoutWidget_2)
        self.radioButton_bad.setObjectName("radioButton_bad")
        self.verticalLayout_2.addWidget(self.radioButton_bad)
        spacerItem = QtWidgets.QSpacerItem(
            20, 342, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 832, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setStyleSheet("c")
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setEnabled(True)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionopen_folder = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        self.actionopen_folder.setFont(font)
        self.actionopen_folder.setObjectName("actionopen_folder")
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.cls_label.setText(_translate("MainWindow", "样本类别"))
        self.radioButton_0.setText(_translate("MainWindow", "0-食管中段四腔心切面"))
        self.radioButton_1.setText(_translate("MainWindow", "1-食管中段两腔心切面"))
        self.radioButton_2.setText(_translate("MainWindow", "2-食管中段左室长轴切面"))
        self.radioButton_3.setText(_translate("MainWindow", "3-食管中段主动脉瓣短轴切面"))
        self.radioButton_4.setText(_translate(
            "MainWindow", "4-食管中段右室流入-流出道切面"))
        self.radioButton_5.setText(_translate("MainWindow", "5-食管中段双腔静脉切面"))
        self.radioButton_6.setText(_translate("MainWindow", "6-食管上段升主动脉短轴切面"))
        self.radioButton_7.setText(_translate("MainWindow", "7-食管上段升主动脉长轴切面"))
        self.radioButton_8.setText(_translate("MainWindow", "8-经胃中段短轴切面"))
        self.radioButton_9.setText(_translate("MainWindow", "9-降主动脉短轴切面"))
        self.radioButton_10.setText(_translate("MainWindow", "10-降主动脉长轴切面"))
        self.radioButton_11.setText(_translate("MainWindow", "11-其他-标准切面"))
        self.radioButton_12.setText(_translate("MainWindow", "12-其他-非标准切面"))
        self.prev_label.setText(_translate("MainWindow", "..."))
        self.pos_label.setText(_translate("MainWindow", "0 / 0"))
        self.next_label.setText(_translate("MainWindow", "..."))
        self.radioButton_None.setText(_translate("MainWindow", "None"))
        self.quality_label.setText(_translate("MainWindow", "样本质量"))
        self.radioButton_good.setText(_translate("MainWindow", "正常"))
        self.radioButton_bad.setText(_translate("MainWindow", "差"))
        self.menu.setTitle(_translate("MainWindow", "打开"))
        self.actionopen_folder.setText(_translate("MainWindow", "open folder"))
