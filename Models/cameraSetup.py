# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cameraSetup.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from functools import partial

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_cameraSetup(object):

    def updateListWidget(self, message):
        self.imageList.addItem(message)


    def setupUi(self, cameraSetup,camera):
        cameraSetup.setObjectName("cameraSetup")
        cameraSetup.resize(900, 458)
        self.centralwidget = QtWidgets.QWidget(cameraSetup)
        self.centralwidget.setObjectName("centralwidget")
        self.captureBtn = QtWidgets.QPushButton(self.centralwidget)
        self.captureBtn.setGeometry(QtCore.QRect(30, 290, 151, 61))
        self.captureBtn.setObjectName("captureBtn")

        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(380, 60, 61, 41))
        self.spinBox.setObjectName("spinBox")



        self.captureBtn.clicked.connect(lambda: camera.setRow(self.spinBox.value()))

        self.spinBox.valueChanged.connect(lambda: self.updateListWidget("Row updated: "+str(self.spinBox.value())))

        self.captureBtn.clicked.connect(camera.takePic)

        self.captureBtn.clicked.connect(lambda: self.updateListWidget("Picture Taken: " + camera.fileName))

        self.captureBtn.clicked.connect(camera.datFile)



        self.imageList = QtWidgets.QListWidget(self.centralwidget)
        self.imageList.setGeometry(QtCore.QRect(490, 50, 300, 361))
        self.imageList.setObjectName("imageList")
        self.upBtn = QtWidgets.QPushButton(self.centralwidget)
        self.upBtn.setGeometry(QtCore.QRect(70, 110, 61, 61))
        self.upBtn.setObjectName("upBtn")
        self.downBtn = QtWidgets.QPushButton(self.centralwidget)
        self.downBtn.setGeometry(QtCore.QRect(70, 200, 61, 61))
        self.downBtn.setObjectName("downBtn")


        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(330, 70, 41, 21))
        self.label.setObjectName("label")
        cameraSetup.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(cameraSetup)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 654, 24))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        cameraSetup.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(cameraSetup)
        self.statusbar.setObjectName("statusbar")
        cameraSetup.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(cameraSetup)
        QtCore.QMetaObject.connectSlotsByName(cameraSetup)

    def retranslateUi(self, cameraSetup):
        _translate = QtCore.QCoreApplication.translate
        cameraSetup.setWindowTitle(_translate("cameraSetup", "MainWindow"))
        self.captureBtn.setText(_translate("cameraSetup", "Capture"))
        self.upBtn.setText(_translate("cameraSetup", "Up"))
        self.downBtn.setText(_translate("cameraSetup", "Down"))
        self.label.setText(_translate("cameraSetup", "Row"))
        self.menu.setTitle(_translate("cameraSetup", "  "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    cameraSetup = QtWidgets.QMainWindow()
    ui = Ui_cameraSetup()
    ui.setupUi(cameraSetup)
    cameraSetup.show()
    sys.exit(app.exec_())
    # sys.exit(QtWidgets.QApplication.closeAllWindows())
