# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../BookCMS_QT/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QLabel
import sys

from mw import Ui_MainWindow as wMain
from mainDialog import Ui_Dialog as mDialog
from LYUtils import DBManager as DBM

class Ui_MainWindow(object):

    def __init__(self, MainWindow):
        self.setupUi(MainWindow)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(414, 312)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 10)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.teUsername = QtWidgets.QTextEdit(self.centralWidget)
        self.teUsername.setMinimumSize(QtCore.QSize(0, 40))
        self.teUsername.setMaximumSize(QtCore.QSize(16777215, 40))
        self.teUsername.setObjectName("tePassword_2")
        self.verticalLayout_4.addWidget(self.teUsername)
        self.tePassword = QtWidgets.QTextEdit(self.centralWidget)
        self.tePassword.setMinimumSize(QtCore.QSize(0, 40))
        self.tePassword.setMaximumSize(QtCore.QSize(16777215, 40))
        self.tePassword.setObjectName("textEdit")
        self.verticalLayout_4.addWidget(self.tePassword)
        self.verticalLayout.addLayout(self.verticalLayout_4)
        self.btnLogin = QtWidgets.QPushButton(self.centralWidget)
        self.btnLogin.setMinimumSize(QtCore.QSize(0, 40))
        self.btnLogin.setMaximumSize(QtCore.QSize(16777215, 40))
        self.btnLogin.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.btnLogin)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnLogin.setText(_translate("MainWindow", "Login"))

    def init_ui_action(self, dialog):
        self.btnLogin.clicked.connect(self.do_login)
        self.dialog = dialog

    def do_login(self):
        username = self.teUsername.toPlainText()
        password = self.tePassword.toPlainText()
        print("do login")
        print('username:' + username)
        print('password:' + password)

        dbManager = DBM()
        ret = dbManager.check_user(username, password)


        self.dialog.init_ui({'username':username})
        self.dialog.setModal(True)        
        self.dialog.setupUi(self.dialog)
        self.dialog.show()
        
        #if ret:
        #MainDialog = QDialog()
        #dia = Ui_Dialog()
        #dia.setupUi(MainDialog)
        #MainDialog.show()

