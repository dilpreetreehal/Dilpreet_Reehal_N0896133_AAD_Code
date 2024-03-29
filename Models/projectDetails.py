from PyQt5 import QtCore, QtWidgets
import os
from Models.cameraClass import Camera
global Form
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from Models.cameraSetup import Ui_cameraSetup

class Ui_projectDetails(object):

    def chooseFolder(self):
        home = os.getenv("HOME")
        my_dir = QFileDialog.getExistingDirectory(None,"Open a folder", home,QFileDialog.ShowDirsOnly)
        # add in filter here to only open folders with right file types
        self.projectPathEdit.setText(my_dir)
    def openProject(self):
        breakpoint()

    def openCamera(self):

        if self.projectNameEdit.text() != "" and (self.projectPathEdit.text() != "Choose Folder") and (self.projectPathEdit.text() != ""):
                QtWidgets.QApplication.closeAllWindows()
                camera = Camera(self.projectPathEdit.text(),self.projectNameEdit.text())
                self.window = QtWidgets.QMainWindow()
                self.ui = Ui_cameraSetup()
                self.ui.setupUi(self.window,camera)
                self.window.show()
                camera.openCamera()
        else:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setText("Fill out Project Name and Folder Location")
            msgBox.setWindowTitle("Invalid Information ")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec()


    def setupUi(self, projectDetails):
        projectDetails.setObjectName("projectDetails")
        projectDetails.resize(782, 457)
        projectDetails.setStyleSheet("background-color:white")
        self.centralwidget = QtWidgets.QWidget(projectDetails)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(260, 170, 311, 111))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.projectTitle = QtWidgets.QLabel(self.formLayoutWidget)
        self.projectTitle.setStyleSheet("background-color:black\n"
"")
        self.projectTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.projectTitle.setObjectName("projectTitle")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.projectTitle)
        self.projectNameEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.projectNameEdit.setStyleSheet("background-color:grey")
        self.projectNameEdit.setObjectName("projectNameEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.projectNameEdit)
        self.fileTitle = QtWidgets.QLabel(self.formLayoutWidget)
        self.fileTitle.setStyleSheet("background-color:black\n"
"")
        self.fileTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.fileTitle.setObjectName("fileTitle")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.fileTitle)

        self.projectPathEdit = QtWidgets.QPushButton(self.formLayoutWidget)
        self.projectPathEdit.setGeometry(QtCore.QRect(30, 20, 100, 32))
        self.projectPathEdit.setStyleSheet("background-color:black")
        self.projectPathEdit.setObjectName("filePathButton")
        self.projectPathEdit.setText("Choose Folder")

        self.projectPathEdit.clicked.connect(self.chooseFolder)


        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.projectPathEdit)
        self.dateEdit = QtWidgets.QDateEdit(self.formLayoutWidget)
        self.dateEdit.setStyleSheet("background-color:grey")
        self.dateEdit.setObjectName("dateEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.dateEdit)
        self.dateTitle = QtWidgets.QLabel(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateTitle.sizePolicy().hasHeightForWidth())
        self.dateTitle.setSizePolicy(sizePolicy)
        self.dateTitle.setStyleSheet("background-color:black\n"
"")
        self.dateTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.dateTitle.setObjectName("dateTitle")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.dateTitle)
        self.nextBtn = QtWidgets.QPushButton(self.centralwidget)
        self.nextBtn.setGeometry(QtCore.QRect(630, 360, 100, 32))
        self.nextBtn.setStyleSheet("background-color:black")

        self.nextBtn.setObjectName("nextBtn")

        self.nextBtn.clicked.connect(self.openCamera)


        projectDetails.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(projectDetails)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 782, 24))
        self.menubar.setObjectName("menubar")
        projectDetails.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(projectDetails)
        self.statusbar.setObjectName("statusbar")
        projectDetails.setStatusBar(self.statusbar)

        self.retranslateUi(projectDetails)
        QtCore.QMetaObject.connectSlotsByName(projectDetails)

    def retranslateUi(self, projectDetails):
        _translate = QtCore.QCoreApplication.translate
        projectDetails.setWindowTitle(_translate("projectDetails", "Project Details"))
        self.projectTitle.setText(_translate("projectDetails", "Project Name"))
        self.fileTitle.setText(_translate("projectDetails", "File Location "))
        self.dateTitle.setText(_translate("projectDetails", "Date               "))
        self.nextBtn.setText(_translate("projectDetails", "Next "))