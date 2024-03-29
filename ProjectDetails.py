# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ProjectDetails.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_projectDetails(object):
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
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setStyleSheet("background-color:black\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit.setStyleSheet("background-color:grey")
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setStyleSheet("background-color:black\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_2.setStyleSheet("background-color:grey")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.dateEdit = QtWidgets.QDateEdit(self.formLayoutWidget)
        self.dateEdit.setStyleSheet("background-color:grey")
        self.dateEdit.setObjectName("dateEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.dateEdit)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setStyleSheet("background-color:black\n"
"")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 20, 100, 32))
        self.pushButton.setStyleSheet("background-color:black")
        self.pushButton.setObjectName("pushButton")
        self.nextBtn = QtWidgets.QPushButton(self.centralwidget)
        self.nextBtn.setGeometry(QtCore.QRect(630, 360, 100, 32))
        self.nextBtn.setStyleSheet("background-color:black;color:blue")
        self.nextBtn.setObjectName("nextBtn")
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
        projectDetails.setWindowTitle(_translate("projectDetails", "MainWindow"))
        self.label_2.setText(_translate("projectDetails", "Project Name"))
        self.label.setText(_translate("projectDetails", "File Location "))
        self.label_5.setText(_translate("projectDetails", "Date               "))
        self.pushButton.setText(_translate("projectDetails", "Open Project"))
        self.nextBtn.setText(_translate("projectDetails", "Next "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    projectDetails = QtWidgets.QMainWindow()
    ui = Ui_projectDetails()
    ui.setupUi(projectDetails)
    projectDetails.show()
    sys.exit(app.exec_())
