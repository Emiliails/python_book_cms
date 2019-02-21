from PyQt5 import QtCore, QtGui, QtWidgets
import sys

# 登陆界面
from login import Ui_MainWindow as wLogin
# 主功能界面
from mainmenu import Ui_Dialog as mainMenuDialog
# 图书搜索界面
from bookinfo import Ui_Dialog as bookInfoDialog 
# 图书详情界面，可以修改删除
from bookdetail import Ui_Dialog as bookDetailDialog

from addbookdetail import Ui_Dialog as bookAddDialog

import BookApp

"""
from ctypes import *
adder = CDLL('./clib/adder.so')
res_int = adder.add_int(4,5)
print('ret:{0}'.format(res_int))
a = c_float(5.5)
b = c_float(4.1)
add_float = adder.add_float
add_float.restype = c_float
print(add_float(a, b))
"""

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)  # 创建一个QApplication，也就是你要开发的软件app
    mainMenu = mainMenuDialog()
    mainWindow = QtWidgets.QMainWindow()    # 创建一个QMainWindow，用来装载你需要的各种组件、控件
    uiLogin = wLogin(mainWindow)  # ui是Ui_MainWindow()类的实例化对象
    uiLogin.init_ui_action(mainWindow)
    mainWindow.show()                       # 执行QMainWindow的show()方法，显示这个QMainWindow

    
    # 初始化图书信息界面
    bookInfo = bookInfoDialog()
    bookInfo.init_ui(bookInfo)

    bookDetail = bookDetailDialog()
    bookDetail.init_ui(bookDetail)

    bookAdd = bookAddDialog()
    bookAdd.init_ui(bookAdd)

    # 添加所有界面容器uis中
    BookApp.uis['mainmenu'] = mainMenu
    BookApp.uis['login'] = mainWindow
    BookApp.uis['bookinfo'] = bookInfo
    BookApp.uis['bookdetail'] = bookDetail
    BookApp.uis['bookadd'] = bookAdd

    sys.exit(app.exec_())                   # 使用exit()或者点击关闭按钮退出QApplication

