import sys
import time

import PyQt5
import cv2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QPropertyAnimation, QRect

from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QMouseEvent, QFont
from PyQt5.QtWidgets import QMainWindow

from Detect import Detect
from Lib.UI_From import Ui_MainWindow
global Temp_Sign_Change
Temp_Sign_Change = 0
class Designer(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setAttribute(Qt.WA_TranslucentBackground) #窗口部件透明化
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint | Qt.Tool)
        self.timer_video = QtCore.QTimer()  # 创建定时器
        self.cap = cv2.VideoCapture() # 打开摄像头
        self.TimeConnet()
        self.setupUi(self)
        self.num_stop = 1
    def TimeConnet(self):
        self.timer_video.timeout.connect(self.Show_Video_Frame)
    def Show_Video_Frame(self): # 显示检测的信息
        global Temp_Sign_Change
        if Temp_Sign_Change == 0:
            flag, img = self.cap.read()
            if img is not None:
                self.label_Information.setText('No Detection')
                show = cv2.resize(img, (640, 480))  # 直接将原始img上的检测结果进行显示
                self.result = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)
                showImage = QtGui.QImage(self.result.data, self.result.shape[1], self.result.shape[0],
                                         QtGui.QImage.Format_RGB888)
                self.label_MP4.setPixmap(QtGui.QPixmap.fromImage(showImage))
                self.label_MP4.setScaledContents(True)  # 设置图像自适应界面大小
        else:
            flag, img = self.cap.read()
            img, List = Detect.Detcetion(None, img)
            Len_List = len(List)
            print('检测到',List)
            if img is not None:
                self.label.setFont(QFont("Roman times", 50, QFont.Bold))  # 字体大小
                strT = '<span style=\" color: #ff4500;\">%s</span>' % ("检测到"+str(Len_List)+"个对象\n")
                self.label_Information.setText("%s" % (strT))
                show = cv2.resize(img, (640, 480))  # 直接将原始img上的检测结果进行显示
                self.result = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)
                showImage = QtGui.QImage(self.result.data, self.result.shape[1], self.result.shape[0],
                                         QtGui.QImage.Format_RGB888)
                self.label_MP4.setPixmap(QtGui.QPixmap.fromImage(showImage))
                self.label_MP4.setScaledContents(True)  # 设置图像自适应界面大小
    def Exit(self): #退出程序
        sys.exit(app.exec_())

    def Pause(self): #暂停
        self.timer_video.blockSignals(False)
        if self.timer_video.isActive() == True and self.num_stop % 2 == 1:
            self.Btn_Video_2.setText(u'暂停检测')  # 当前状态为暂停状态
            self.num_stop = self.num_stop + 1  # 调整标记信号为偶数
            self.timer_video.blockSignals(True)
        else:
            self.num_stop = self.num_stop + 1
            self.Btn_Video_2.setText(u'继续检测')
    def Finish(self): #结束检测
        self.cap.release()  # 释放video_capture资源
        self.label_MP4.clear()
        if self.num_stop % 2 == 0:
            self.Btn_Video_2.setText(u'暂停检测')
            self.num_stop = self.num_stop + 1
            self.timer_video.blockSignals(False)
    def OpenCerama(self): #打开摄像头
        camera_num = 0
        self.cap = cv2.VideoCapture(camera_num)
        # 判断摄像头是否处于打开状态
        bool_open = self.cap.isOpened()
        if not bool_open:
            QtWidgets.QMessageBox.warning(self, u"Warning", u"打开摄像头失败", buttons=QtWidgets.QMessageBox.Ok,
                                          defaultButton=QtWidgets.QMessageBox.Ok)
        else:
            self.timer_video.start(30)
    def OpenMp4(self): #打开视频
        video_name, _ = QtWidgets.QFileDialog.getOpenFileName(self, "打开视频", "data/", "*.mp4;;*.avi;;All Files(*)")
        flag = self.cap.open(video_name)
        if not flag:
            QtWidgets.QMessageBox.warning(self, u"Warning", u"打开视频失败", buttons=QtWidgets.QMessageBox.Ok,
                                          defaultButton=QtWidgets.QMessageBox.Ok)
            return
        else:
            self.timer_video.start(30)
    def SignChange(self): #Btn.png的移动
        global Temp_Sign_Change
        if Temp_Sign_Change == 0:
            Temp_Sign_Change = 1
            animation = QPropertyAnimation(self.label)
            animation.setTargetObject(self.label)  # 设置动画对象
            animation.setPropertyName(b"geometry")
            animation.setStartValue(QRect(self.label.geometry().x(), self.label.geometry().y(), 42, 38))  # 设置起始点;初始尺寸
            animation.setEndValue((QRect(self.label.geometry().x() + 90, self.label.geometry().y(), 42, 38)))  # 设置终点；终止尺寸
            animation.setDuration(100)  # 时长单位毫秒
            animation.start()
        else:
            Temp_Sign_Change = 0
            animation = QPropertyAnimation(self.label)
            animation.setTargetObject(self.label)  # 设置动画对象
            animation.setPropertyName(b"geometry")
            animation.setStartValue(QRect(self.label.geometry().x(), self.label.geometry().y(), 42, 38))  # 设置起始点;初始尺寸
            animation.setEndValue((QRect(self.label.geometry().x() - 90, self.label.geometry().y(), 42, 38)))  # 设置终点；终止尺寸
            animation.setDuration(100)  # 时长单位毫秒
            animation.start()

if __name__ == '__main__':
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    ui = Designer()
    ui.show()
    sys.exit(app.exec_())