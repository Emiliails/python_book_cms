# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QLabel
import sys

from LYUtils import DBManager as DBM

import BookApp as app

class Ui_MainWindow(object):   

    def __init__(self, MainWindow):
        self.window = MainWindow
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
        self.verticalLayout_4.setContentsMargins(100, 0, 100, 10)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.title = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.verticalLayout_4.addWidget(self.title)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.teUsername = QtWidgets.QTextEdit(self.centralWidget)
        self.teUsername.setMinimumSize(QtCore.QSize(0, 30))
        self.teUsername.setMaximumSize(QtCore.QSize(16777215, 40))
        self.teUsername.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.teUsername.setUndoRedoEnabled(True)
        self.teUsername.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.teUsername.setObjectName("teUsername")
        self.verticalLayout_4.addWidget(self.teUsername)
        self.tePassword = QtWidgets.QTextEdit(self.centralWidget)
        self.tePassword.setMinimumSize(QtCore.QSize(0, 30))
        self.tePassword.setMaximumSize(QtCore.QSize(16777215, 40))
        self.tePassword.setObjectName("tePassword")
        self.verticalLayout_4.addWidget(self.tePassword)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem2)
        self.btnLogin = QtWidgets.QPushButton(self.centralWidget)
        self.btnLogin.setMinimumSize(QtCore.QSize(0, 40))
        self.btnLogin.setMaximumSize(QtCore.QSize(16777215, 40))
        self.btnLogin.setObjectName("btnLogin")
        self.verticalLayout_4.addWidget(self.btnLogin)
        self.verticalLayout.addLayout(self.verticalLayout_4)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "欢迎登陆"))
        self.title.setText(_translate("MainWindow", "图书查询系统"))
        self.teUsername.setPlaceholderText(_translate("MainWindow", "用户名"))
        self.tePassword.setPlaceholderText(_translate("MainWindow", "密码"))
        self.btnLogin.setText(_translate("MainWindow", "登陆"))
        
    def init_ui_action(self, dialog):
        self.btnLogin.clicked.connect(self.do_login)

    def do_login(self):
        username = self.teUsername.toPlainText()
        password = self.tePassword.toPlainText()
        print('username:' + username)
        print('password:' + password)

        dbManager = DBM()
        ret = dbManager.check_user(username, password)

        dialog = app.get_window('mainmenu')
        dialog.init_ui_data({'username': username})
        dialog.init_ui_action()

        app.show_window('mainmenu')
        app.hide_window('login')

