# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog1.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QDialog, QLabel

import BookApp as app

class Ui_Dialog(QDialog):

    def init_ui(self, params):
        self.username = params['username']

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(544, 408)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(10, 40, 511, 51))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 40))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_3.setMaximumSize(QtCore.QSize(16777215, 40))
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_2.setMaximumSize(QtCore.QSize(16777215, 40))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_4.setMaximumSize(QtCore.QSize(16777215, 40))
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(15, 101, 501, 291))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Welcome "+self.username))
        self.pushButton.setText(_translate("Dialog", "Search"))
        self.pushButton_3.setText(_translate("Dialog", "Sale"))
        self.pushButton_2.setText(_translate("Dialog", "Add"))
        self.pushButton_4.setText(_translate("Dialog", "Setting"))
        
    def init_ui_action(self):
        self.pushButton_2.clicked.connect(self.do_exit)

    def do_exit(self):
        app.show_window('login')

