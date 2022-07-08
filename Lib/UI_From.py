# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_From.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1099, 863)
        self.main_widget = QtWidgets.QWidget(MainWindow)
        self.main_widget.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.253731 rgba(232, 2, 6, 255), stop:0.915423 rgba(0, 219, 255, 255));\n"
"border-radius:50px;")
        self.main_widget.setObjectName("main_widget")
        self.Btn_Cerama = QtWidgets.QPushButton(self.main_widget)
        self.Btn_Cerama.setGeometry(QtCore.QRect(10, 140, 151, 101))
        self.Btn_Cerama.setStyleSheet("QPushButton{border-radius: 20px; \n"
"border: 5px groove gray;\n"
"border-style: outset;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 219, 255, 255), stop:0.820896 rgba(232, 2, 6, 255));\n"
"font: 20pt \"Agency FB\";}\n"
"QPushButton:hover{\n"
"border-radius: 20px; \n"
"border: 5px groove gray;\n"
"border-style: outset;\n"
"    background-color: qlineargradient(spread:reflect, x1:1, y1:0.0116364, x2:0.985075, y2:1, stop:0.223881 rgba(255, 96, 93, 255), stop:0.696517 rgba(56, 255, 240, 255));\n"
"font: 20pt \"Agency FB\"\n"
"}\n"
"QPushButton:pressed{border-radius: 20px; \n"
"border: 5px groove gray;\n"
"border-style: outset;\n"
"    background-color: qlineargradient(spread:reflect, x1:1, y1:0.0116364, x2:0.985075, y2:1, stop:0.109453 rgba(176, 65, 65, 255), stop:0.696517 rgba(60, 199, 227, 255));\n"
"font: 20pt \"Agency FB\"}")
        self.Btn_Cerama.setCheckable(False)
        self.Btn_Cerama.setChecked(False)
        self.Btn_Cerama.setObjectName("Btn_Cerama")
        self.label_MP4 = QtWidgets.QLabel(self.main_widget)
        self.label_MP4.setGeometry(QtCore.QRect(300, 70, 781, 491))
        self.label_MP4.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(39, 213, 241, 255), stop:1 rgba(255, 87, 255, 201));")
        self.label_MP4.setText("")
        self.label_MP4.setObjectName("label_MP4")
        self.Btn_Video = QtWidgets.QPushButton(self.main_widget)
        self.Btn_Video.setGeometry(QtCore.QRect(10, 30, 151, 101))
        self.Btn_Video.setStyleSheet("QPushButton{border-radius: 20px; \n"
"border: 5px groove gray;\n"
"border-style: outset;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 219, 255, 255), stop:0.820896 rgba(232, 2, 6, 255));\n"
"font: 20pt \"Agency FB\";}\n"
"QPushButton:hover{\n"
"border-radius: 20px; \n"
"border: 5px groove gray;\n"
"border-style: outset;\n"
"    background-color: qlineargradient(spread:reflect, x1:1, y1:0.0116364, x2:0.985075, y2:1, stop:0.223881 rgba(255, 96, 93, 255), stop:0.696517 rgba(56, 255, 240, 255));\n"
"font: 20pt \"Agency FB\"\n"
"}\n"
"QPushButton:pressed{border-radius: 20px; \n"
"border: 5px groove gray;\n"
"border-style: outset;\n"
"    background-color: qlineargradient(spread:reflect, x1:1, y1:0.0116364, x2:0.985075, y2:1, stop:0.109453 rgba(176, 65, 65, 255), stop:0.696517 rgba(60, 199, 227, 255));\n"
"font: 20pt \"Agency FB\"}")
        self.Btn_Video.setCheckable(False)
        self.Btn_Video.setChecked(False)
        self.Btn_Video.setObjectName("Btn_Video")
        self.label_Information = QtWidgets.QLabel(self.main_widget)
        self.label_Information.setGeometry(QtCore.QRect(250, 590, 871, 211))
        self.label_Information.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(45, 213, 241, 255), stop:1 rgba(0, 11, 255, 201));\n"
"font: 75 48pt \"Agency FB\";")
        self.label_Information.setText("")
        self.label_Information.setObjectName("label_Information")
        self.label_Message_Information = QtWidgets.QLabel(self.main_widget)
        self.label_Message_Information.setGeometry(QtCore.QRect(30, 590, 201, 211))
        self.label_Message_Information.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(45, 213, 241, 255), stop:1 rgba(0, 11, 255, 201));\n"
"font: 30pt \"Bahnschrift SemiLight Condensed\";\n"
)
        self.label_Message_Information.setObjectName("label_Message_Information")
        self.label_Message_Mp4 = QtWidgets.QLabel(self.main_widget)
        self.label_Message_Mp4.setGeometry(QtCore.QRect(170, 70, 111, 491))
        self.label_Message_Mp4.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(39, 213, 241, 255), stop:1 rgba(255, 87, 255, 201));\n"
"font: 75 48pt \"Agency FB\";\n"
"")
        self.label_Message_Mp4.setObjectName("label_Message_Mp4")
        self.Btn_Exit = QtWidgets.QPushButton(self.main_widget)
        self.Btn_Exit.setGeometry(QtCore.QRect(10, 470, 151, 101))
        self.Btn_Exit.setStyleSheet("QPushButton{border-radius: 20px; \n"
"border: 5px groove gray;\n"
"border-style: outset;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 219, 255, 255), stop:0.820896 rgba(232, 2, 6, 255));\n"
"font: 20pt \"Agency FB\";}\n"
"QPushButton:hover{\n"
"border-radius: 20px; \n"
"border: 5px groove gray;\n"
"border-style: outset;\n"
"    background-color: qlineargradient(spread:reflect, x1:1, y1:0.0116364, x2:0.985075, y2:1, stop:0.223881 rgba(255, 96, 93, 255), stop:0.696517 rgba(56, 255, 240, 255));\n"
"font: 20pt \"Agency FB\"\n"
"}\n"
"QPushButton:pressed{border-radius: 20px; \n"
"border: 5px groove gray;\n"
"border-style: outset;\n"
"    background-color: qlineargradient(spread:reflect, x1:1, y1:0.0116364, x2:0.985075, y2:1, stop:0.109453 rgba(176, 65, 65, 255), stop:0.696517 rgba(60, 199, 227, 255));\n"
"font: 20pt \"Agency FB\"}")
        self.Btn_Exit.setCheckable(False)
        self.Btn_Exit.setChecked(False)
        self.Btn_Exit.setObjectName("Btn_Exit")
        self.label_Message_QNum = QtWidgets.QLabel(self.main_widget)
        self.label_Message_QNum.setGeometry(QtCore.QRect(460, 10, 431, 51))
        self.label_Message_QNum.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(45, 213, 241, 255), stop:1 rgba(0, 11, 255, 201));\n"
"font: 20pt \"Bahnschrift SemiLight Condensed\";\n"
"border-radius:20px"
)
        self.label_Message_QNum.setAlignment(Qt.AlignCenter)
        self.label_Message_QNum.setObjectName("label_Message_QNum")
        self.Btn_Video_2 = QtWidgets.QPushButton(self.main_widget)
        self.Btn_Video_2.setGeometry(QtCore.QRect(10, 250, 151, 101))
        self.Btn_Video_2.setStyleSheet("QPushButton{border-radius: 20px; \n"
"border: 5px groove gray;\n"
"border-style: outset;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 219, 255, 255), stop:0.820896 rgba(232, 2, 6, 255));\n"
"font: 20pt \"Agency FB\";}\n"
"QPushButton:hover{\n"
"border-radius: 20px; \n"
"border: 5px groove gray;\n"
"border-style: outset;\n"
"    background-color: qlineargradient(spread:reflect, x1:1, y1:0.0116364, x2:0.985075, y2:1, stop:0.223881 rgba(255, 96, 93, 255), stop:0.696517 rgba(56, 255, 240, 255));\n"
"font: 20pt \"Agency FB\"\n"
"}\n"
"QPushButton:pressed{border-radius: 20px; \n"
"border: 5px groove gray;\n"
"border-style: outset;\n"
"    background-color: qlineargradient(spread:reflect, x1:1, y1:0.0116364, x2:0.985075, y2:1, stop:0.109453 rgba(176, 65, 65, 255), stop:0.696517 rgba(60, 199, 227, 255));\n"
"font: 20pt \"Agency FB\"}")
        self.Btn_Video_2.setCheckable(False)
        self.Btn_Video_2.setChecked(False)
        self.Btn_Video_2.setObjectName("Btn_Video_2")
        self.Btn_Video_Finish = QtWidgets.QPushButton(self.main_widget)
        self.Btn_Video_Finish.setGeometry(QtCore.QRect(10, 360, 151, 101))
        self.Btn_Video_Finish.setStyleSheet("QPushButton{border-radius: 20px; \n"
"border: 5px groove gray;\n"
"border-style: outset;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 219, 255, 255), stop:0.820896 rgba(232, 2, 6, 255));\n"
"font: 20pt \"Agency FB\";}\n"
"QPushButton:hover{\n"
"border-radius: 20px; \n"
"border: 5px groove gray;\n"
"border-style: outset;\n"
"    background-color: qlineargradient(spread:reflect, x1:1, y1:0.0116364, x2:0.985075, y2:1, stop:0.223881 rgba(255, 96, 93, 255), stop:0.696517 rgba(56, 255, 240, 255));\n"
"font: 20pt \"Agency FB\"\n"
"}\n"
"QPushButton:pressed{border-radius: 20px; \n"
"border: 5px groove gray;\n"
"border-style: outset;\n"
"    background-color: qlineargradient(spread:reflect, x1:1, y1:0.0116364, x2:0.985075, y2:1, stop:0.109453 rgba(176, 65, 65, 255), stop:0.696517 rgba(60, 199, 227, 255));\n"
"font: 20pt \"Agency FB\"}")
        self.Btn_Video_Finish.setCheckable(False)
        self.Btn_Video_Finish.setChecked(False)
        self.Btn_Video_Finish.setObjectName("Btn_Video_Finish")
        self.Btn_Detect = QtWidgets.QPushButton(self.main_widget)
        self.Btn_Detect.setGeometry(QtCore.QRect(180, 20, 141, 41))
        self.Btn_Detect.setStyleSheet("QPushButton{\n"
"    background:transparent;\n"
"    color:white;\n"
"    border-radius: 20px;\n"
"    font-family: 微软雅黑;\n"
"    border: 3px solid black;\n"
"}\n"
"QPushButton:hover{                    \n"
"    background:transparent;\n"
"    border:3px solid black;\n"
"}\n"
"QPushButton:pressed{\n"
"    border: 3px solid black;\n"
"    background: transparent;\n"
"}<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
"<ui version=\"4.0\">\n"
" <widget name=\"__qt_fake_top_level\">\n"
"  <widget class=\"QLabel\" name=\"label_8\">\n"
"   <property name=\"geometry\">\n"
"    <rect>\n"
"     <x>392</x>\n"
"     <y>362</y>\n"
"     <width>331</width>\n"
"     <height>321</height>\n"
"    </rect>\n"
"   </property>\n"
"   <property name=\"text\">\n"
"    <string/>\n"
"   </property>\n"
"   <property name=\"pixmap\">\n"
"    <pixmap>G:/桌面文件/Qt控件案例/Custom/凹.png</pixmap>\n"
"   </property>\n"
"   <property name=\"scaledContents\">\n"
"    <bool>true</bool>\n"
"   </property>\n"
"  </widget>\n"
" </widget>\n"
" <resources/>\n"
"</ui>\n"
"")
        self.Btn_Detect.setText("")
        self.Btn_Detect.setObjectName("Btn_Detect")
        self.label = QtWidgets.QLabel(self.main_widget)
        self.label.setGeometry(QtCore.QRect(185, 20, 42, 39))
        self.label.setStyleSheet("border-image: url(:/IMG/IMG/Btn.png);\n"
"background-color: None;")
        self.label.setText("")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.main_widget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1099, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)


        self.retranslateUi(MainWindow)
        self.Btn_Video.clicked.connect(MainWindow.OpenCerama)
        self.Btn_Cerama.clicked.connect(MainWindow.OpenMp4)
        self.Btn_Video_2.clicked.connect(MainWindow.Pause)
        self.Btn_Video_Finish.clicked.connect(MainWindow.Finish)
        self.Btn_Exit.clicked.connect(MainWindow.Exit)
        self.Btn_Detect.clicked.connect(MainWindow.SignChange)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Btn_Cerama.setText(_translate("MainWindow", "打开视频"))
        self.Btn_Video.setText(_translate("MainWindow", "打开摄像"))
        self.label_Message_Information.setText(_translate("MainWindow", "\n"
"检测信息\n"
""))
        self.label_Message_Mp4.setText(_translate("MainWindow","\n"
"视\n"
"\n"
"频\n"))
        self.Btn_Exit.setText(_translate("MainWindow", "退出程序"))
        self.label_Message_QNum.setText(_translate("MainWindow", "獜洛橙"))
        self.Btn_Video_2.setText(_translate("MainWindow", "暂停检测"))
        self.Btn_Video_Finish.setText(_translate("MainWindow", "结束检测"))
from Lib import QRC_rc
