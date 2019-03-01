# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainmenu.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QLineEdit, QMessageBox

import BookApp as app

class Ui_Dialog(QDialog):

    def init_ui(self, dialog):
        self.closeFromAction = False
        self.setupUi(dialog)
                
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(612, 421)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btnBookInfo = QtWidgets.QPushButton(Dialog)
        self.btnBookInfo.setMinimumSize(QtCore.QSize(100, 100))
        self.btnBookInfo.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.btnBookInfo.setAutoDefault(False)
        self.btnBookInfo.setObjectName("btnBookInfo")
        self.horizontalLayout_4.addWidget(self.btnBookInfo)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.btnBookAdd = QtWidgets.QPushButton(Dialog)
        self.btnBookAdd.setMinimumSize(QtCore.QSize(100, 100))
        self.btnBookAdd.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.btnBookAdd.setAutoDefault(False)
        self.btnBookAdd.setObjectName("btnBookAdd")
        self.horizontalLayout_4.addWidget(self.btnBookAdd)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.btnBookSale = QtWidgets.QPushButton(Dialog)
        self.btnBookSale.setMinimumSize(QtCore.QSize(100, 100))
        self.btnBookSale.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.btnBookSale.setAutoDefault(False)
        self.btnBookSale.setObjectName("btnBookSale")
        self.horizontalLayout_4.addWidget(self.btnBookSale)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.btnSysConf = QtWidgets.QPushButton(Dialog)
        self.btnSysConf.setMinimumSize(QtCore.QSize(100, 100))
        self.btnSysConf.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.btnSysConf.setAutoDefault(False)
        self.btnSysConf.setObjectName("btnSysConf")
        self.horizontalLayout_4.addWidget(self.btnSysConf)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.btnSysExit = QtWidgets.QPushButton(Dialog)
        self.btnSysExit.setMinimumSize(QtCore.QSize(100, 100))
        self.btnSysExit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.btnSysExit.setAutoDefault(False)
        self.btnSysExit.setObjectName("btnSysExit")
        self.horizontalLayout_4.addWidget(self.btnSysExit)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(50)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        #Dialog.setWindowTitle(_translate("Dialog", self.username + ", 欢迎登陆图书管理系统"))
        self.btnBookInfo.setText(_translate("Dialog", "图书信息"))
        self.btnBookAdd.setText(_translate("Dialog", "图书入库"))
        self.btnBookSale.setText(_translate("Dialog", "销售查询"))
        self.btnSysConf.setText(_translate("Dialog", "系统配置"))
        self.btnSysExit.setText(_translate("Dialog", "系统退出"))
        self.label.setText(_translate("Dialog", "图书管理系统"))

    def init_ui_data(self, params):
        username = params['username']
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", username + ", 欢迎登陆图书管理系统"))

    def init_ui_action(self):
        self.btnBookInfo.clicked.connect(self.show_book_info_window)
        self.btnBookAdd.clicked.connect(self.show_book_add_window)
        self.btnBookSale.clicked.connect(self.show_book_sale_window)
        self.btnSysConf.clicked.connect(self.show_book_sys_conf_window)
        self.btnSysExit.clicked.connect(self.show_book_exit_window)

    def show_book_info_window(self): 
        print("show_book_info_window")
        dialog = app.get_window('bookinfo')
        dialog.init_ui_action()

        app.show_window('bookinfo')
        app.hide_window('mainmenu')


    def show_book_add_window(self):
        print("show_book_add_window")

    def show_book_sale_window(self):
        print("show_book_sale_window")

    def show_book_sys_conf_window(self):
        dialog = app.get_window('changeadminpwd')
        dialog.setModal(True)
        dialog.init_ui_action()

        app.show_window('changeadminpwd')
        app.hide_window('mainmenu')

    def show_book_exit_window(self):
        print("show_book_exit_window")
        quitDialog = Ui_Quit_Dialog()
        quitDialog.show_quit_dialog(self)


    """对QDialog类重写，实现一些功能"""""
    def closeEvent(self, event):
        if self.closeFromAction:
            self.closeFromAction = False
            return

        reply = QtWidgets.QMessageBox.question(self, '提示',"是否退出系统?!",QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,QtWidgets.QMessageBox.No)
            
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
            app.hide_window('mainmenu')
            app.show_window('login')
        else:
            event.ignore()


"""
新增一个关闭窗口类
"""
class Ui_Quit_Dialog(QDialog):

    def show_quit_dialog(self, dialog):
        box = QMessageBox(QMessageBox.Question, self.tr("提示"), self.tr("是否退出系统?!"), QMessageBox.NoButton, self)
        yr_btn = box.addButton(self.tr("是"), QMessageBox.YesRole)
        nr_btn = box.addButton(self.tr("否"), QMessageBox.YesRole)


        box.move(dialog.pos().x()+dialog.size().width()/2-box.size().width(),
                dialog.pos().y() + dialog.size().height()/2-box.size().height())

        box.exec_()
        if box.clickedButton() == yr_btn:
            self.closeFromAction = True
            #self.closeFromAction = True
            app.hide_window('mainmenu')
            app.show_window('login')
            return
        else:
            self.closeFromAction = True


