# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'changeadminpwd.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QDialog, QLabel

import BookApp as app

class Ui_Dialog(QDialog):
    
    def init_ui(self, dialog):
        self.setupUi(dialog)

    def init_ui_action(self):
        self.btnCancle.clicked.connect(self.go_back)
        pass

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(529, 316)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setMinimumSize(QtCore.QSize(0, 45))
        self.label.setMaximumSize(QtCore.QSize(16777215, 45))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setMinimumSize(QtCore.QSize(0, 40))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_4 = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(0, 40))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.txNewPwd = QtWidgets.QLineEdit(Dialog)
        self.txNewPwd.setMinimumSize(QtCore.QSize(220, 40))
        self.txNewPwd.setMaximumSize(QtCore.QSize(220, 40))
        self.txNewPwd.setObjectName("txNewPwd")
        self.verticalLayout.addWidget(self.txNewPwd)
        self.txConfirmPwd = QtWidgets.QLineEdit(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txConfirmPwd.sizePolicy().hasHeightForWidth())
        self.txConfirmPwd.setSizePolicy(sizePolicy)
        self.txConfirmPwd.setMinimumSize(QtCore.QSize(220, 40))
        self.txConfirmPwd.setMaximumSize(QtCore.QSize(220, 40))
        self.txConfirmPwd.setObjectName("txConfirmPwd")
        self.verticalLayout.addWidget(self.txConfirmPwd)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnOK = QtWidgets.QPushButton(Dialog)
        self.btnOK.setObjectName("btnOK")
        self.horizontalLayout_2.addWidget(self.btnOK)
        self.btnCancle = QtWidgets.QPushButton(Dialog)
        self.btnCancle.setObjectName("btnCancle")
        self.horizontalLayout_2.addWidget(self.btnCancle)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout_3, 1, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 2, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 41, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 0, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 1, 4, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "修改管理员密码"))
        self.label_2.setText(_translate("Dialog", "新密码"))
        self.label_4.setText(_translate("Dialog", "确认密码"))
        self.btnOK.setText(_translate("Dialog", "确定"))
        self.btnCancle.setText(_translate("Dialog", "返回"))


    def go_back(self):
        app.hide_window('changeadminpwd')
        app.show_window('mainmenu')

    """对QDialog类重写，实现一些功能"""""
    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(self, '提示',"是否退出?!",QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,QtWidgets.QMessageBox.No)
            
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
            self.go_back()
        else:
            event.ignore()
