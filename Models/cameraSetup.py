

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_cameraSetup(object):


    def setupUi(self, cameraSetup,camera):
        cameraSetup.setObjectName("cameraSetup")
        cameraSetup.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(cameraSetup)
        self.centralwidget.setObjectName("centralwidget")
        self.captureBtn = QtWidgets.QPushButton(self.centralwidget)
        self.captureBtn.setGeometry(QtCore.QRect(400, 430, 100, 32))
        self.captureBtn.setObjectName("captureBtn")

        self.captureBtn.clicked.connect(camera.takePic)

        self.imageList = QtWidgets.QListWidget(self.centralwidget)
        self.imageList.setGeometry(QtCore.QRect(10, 60, 171, 411))
        self.imageList.setObjectName("imageList")

        self.imagePreview = QtWidgets.QLabel(cameraSetup)
        self.imagePreview.setGeometry(QtCore.QRect(230, 60, 451, 331))

        # self.imagePreview.setText("")

        self.image_label = QtWidgets.QLabel(cameraSetup)
        self.image_label.setObjectName("image_label")

        self.imagePreview.setObjectName("imagePreview")


        cameraSetup.setCentralWidget(self.centralwidget)


        self.menubar = QtWidgets.QMenuBar(cameraSetup)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        cameraSetup.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(cameraSetup)
        self.statusbar.setObjectName("statusbar")
        cameraSetup.setStatusBar(self.statusbar)

        self.retranslateUi(cameraSetup)
        QtCore.QMetaObject.connectSlotsByName(cameraSetup)

    def retranslateUi(self, cameraSetup):
        _translate = QtCore.QCoreApplication.translate
        cameraSetup.setWindowTitle(_translate("cameraSetup", "MainWindow"))
        self.captureBtn.setText(_translate("cameraSetup", "Capture"))
        self.image_label.setText(_translate("Form", "TextLabel"))



