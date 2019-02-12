from PyQt5 import QtCore, QtGui, QtWidgets
import sys

from login import Ui_MainWindow as wLogin
from mw import Ui_MainWindow as wMain
from mainDialog import Ui_Dialog as mDialog

import BookApp 

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)  # 创建一个QApplication，也就是你要开发的软件app
    d1 = mDialog()
    mainWindow = QtWidgets.QMainWindow()    # 创建一个QMainWindow，用来装载你需要的各种组件、控件
    uiLogin = wLogin(mainWindow)  # ui是Ui_MainWindow()类的实例化对象
    uiLogin.init_ui_action(mainWindow)
    mainWindow.show()                       # 执行QMainWindow的show()方法，显示这个QMainWindow
    
    BookApp.uis['d1'] = d1
    BookApp.uis['login'] = mainWindow

    sys.exit(app.exec_())                   # 使用exit()或者点击关闭按钮退出QApplication

