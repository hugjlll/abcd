# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ifui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1012, 605)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(120, 480, 231, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(40, 160, 461, 281))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.video1 = QtWidgets.QLabel(self.frame)
        self.video1.setGeometry(QtCore.QRect(0, 0, 461, 281))
        self.video1.setObjectName("video1")
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setGeometry(QtCore.QRect(540, 160, 431, 281))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.video2 = QtWidgets.QLabel(self.frame_2)
        self.video2.setGeometry(QtCore.QRect(0, 0, 431, 281))
        self.video2.setObjectName("video2")
        self.frame_3 = QtWidgets.QFrame(Dialog)
        self.frame_3.setGeometry(QtCore.QRect(440, 480, 251, 71))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setGeometry(QtCore.QRect(10, 10, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.frame_4 = QtWidgets.QFrame(Dialog)
        self.frame_4.setGeometry(QtCore.QRect(720, 480, 231, 71))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_2 = QtWidgets.QLabel(self.frame_4)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.title = QtWidgets.QLabel(Dialog)
        self.title.setGeometry(QtCore.QRect(20, 40, 981, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "开始匹配"))
        self.video1.setText(_translate("Dialog", "TextLabel"))
        self.video2.setText(_translate("Dialog", "TextLabel"))
        self.label.setText(_translate("Dialog", "匹配结果："))
        self.label_2.setText(_translate("Dialog", ""))
        self.title.setText(_translate("Dialog", "手写签名与身份证姓名匹配系统"))
