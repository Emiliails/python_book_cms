# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../BookCMS_QT/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys

from LYUtils import DBManager as DBM

from mainwindow import Ui_Form as MainDialog


class Ui_MainWindow(object):

    def __init__(self):
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

    def init_ui_action(self):
        self.btnLogin.clicked.connect(self.do_login)
        self.ui_main_window = MainDialog()

    def do_login(self):
        username = self.teUsername.toPlainText()
        password = self.tePassword.toPlainText()
        print("do login")
        print('username:' + username)
        print('password:' + password)

        dbManager = DBM()
        ret = dbManager.check_user(username, password)
        if ret:
            Form = Qt
            mw = MainDialog()
            


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)  # 创建一个QApplication，也就是你要开发的软件app
    MainWindow = QtWidgets.QMainWindow()    # 创建一个QMainWindow，用来装载你需要的各种组件、控件
    ui = Ui_MainWindow()                    # ui是Ui_MainWindow()类的实例化对象
    ui.init_ui_action()
    MainWindow.show()                       # 执行QMainWindow的show()方法，显示这个QMainWindow
    sys.exit(app.exec_())                   # 使用exit()或者点击关闭按钮退出QApplication

