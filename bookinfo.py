# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bookinfo2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QLineEdit
from PyQt5.Qt import * # 包含了Qt.Key_Return


import BookApp as app

searchs = {}

class MyTextEdit(QtWidgets.QTextEdit):
    
    def __init__(self, parent, key):
        """
        QtWidgets.QTextEdit.__init__(self)
        self.parent = parent
        """
        super(MyTextEdit, self).__init__(parent)
        # 监听文本框是否被选择
        #self.selectionChanged.connect(self.text_selected)

        self.key = key
        if key not in searchs:
            print('add ' + key + '...')
            searchs[key] = ""

    def text_selected(self):
        if self.toPlainText() != '':
            print(self.toPlainText())

    def keyPressEvent(self, event):
        """
        监听文本内容变化，并且过滤回车和空内容
        """
        QtWidgets.QTextEdit.keyPressEvent(self, event)
        if event.key() == Qt.Key_Return:
            # 过滤回车并且防止空字符的发送
            cursor = self.textCursor()
            cursor.clearSelection()
            cursor.deletePreviousChar()
            if self.toPlainText() != '':
                print(self.key+": " + self.toPlainText())

            # update search condition
            searchs[self.key] = self.toPlainText()
            print('total search conditions:' + str(searchs))


'''
继承了QLineEdit类，监听文本框内容的变化
'''
class MyLineEdit(QtWidgets.QLineEdit):

    def __init__(self, parent):
        super(MyLineEdit, self).__init__(parent)
        self.textChanged.connect(self.text_changed)
        self.editingFinished.connect(self.text_finished)

    def text_changed(self):
        if self.text() != '':
            print(self.text())

    def text_finished(self):
        if self.text() != '':
            print(self.text())


class Ui_Dialog(QDialog):

    def init_ui(self):
        print("bookinfo init ui")

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(616, 454)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(18)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_3 = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.txBookName = MyTextEdit(Dialog, 'name')#MyLineEdit(Dialog)#QtWidgets.QLineEdit(Dialog)
        self.txBookName.setMinimumSize(QtCore.QSize(0, 40))
        self.txBookName.setMaximumSize(QtCore.QSize(16777215, 40))
        self.txBookName.setObjectName("txBookName")
        self.verticalLayout_3.addWidget(self.txBookName)
        self.txBookJZCode = MyTextEdit(Dialog, 'jzcode')#QtWidgets.QTextEdit(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txBookJZCode.sizePolicy().hasHeightForWidth())
        self.txBookJZCode.setSizePolicy(sizePolicy)
        self.txBookJZCode.setMaximumSize(QtCore.QSize(16777215, 40))
        self.txBookJZCode.setObjectName("txBookJZCode")
        self.verticalLayout_3.addWidget(self.txBookJZCode)
        self.txBookBarCode = MyTextEdit(Dialog, 'ISBN')#QtWidgets.QTextEdit(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txBookBarCode.sizePolicy().hasHeightForWidth())
        self.txBookBarCode.setSizePolicy(sizePolicy)
        self.txBookBarCode.setMaximumSize(QtCore.QSize(16777215, 40))
        self.txBookBarCode.setObjectName("txBookBarCode")
        self.verticalLayout_3.addWidget(self.txBookBarCode)
        self.txBookAuthor = MyTextEdit(Dialog, 'author')#QtWidgets.QTextEdit(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txBookAuthor.sizePolicy().hasHeightForWidth())
        self.txBookAuthor.setSizePolicy(sizePolicy)
        self.txBookAuthor.setMaximumSize(QtCore.QSize(16777215, 40))
        self.txBookAuthor.setObjectName("txBookAuthor")
        self.verticalLayout_3.addWidget(self.txBookAuthor)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(20)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_10 = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_4.addWidget(self.label_10)
        self.label_11 = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_4.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_4.addWidget(self.label_12)
        self.label_13 = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_4.addWidget(self.label_13)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.txBookPress = MyTextEdit(Dialog, 'press')#QtWidgets.QTextEdit(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txBookPress.sizePolicy().hasHeightForWidth())
        self.txBookPress.setSizePolicy(sizePolicy)
        self.txBookPress.setMinimumSize(QtCore.QSize(0, 40))
        self.txBookPress.setMaximumSize(QtCore.QSize(16777215, 40))
        self.txBookPress.setObjectName("txBookPress")
        self.verticalLayout_6.addWidget(self.txBookPress)
        self.txBookPrice = MyTextEdit(Dialog, 'price')#QtWidgets.QTextEdit(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txBookPrice.sizePolicy().hasHeightForWidth())
        self.txBookPrice.setSizePolicy(sizePolicy)
        self.txBookPrice.setMinimumSize(QtCore.QSize(0, 40))
        self.txBookPrice.setMaximumSize(QtCore.QSize(16777215, 40))
        self.txBookPrice.setObjectName("txBookPrice")
        self.verticalLayout_6.addWidget(self.txBookPrice)
        self.txBookNote = MyTextEdit(Dialog, 'note')#QtWidgets.QTextEdit(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txBookNote.sizePolicy().hasHeightForWidth())
        self.txBookNote.setSizePolicy(sizePolicy)
        self.txBookNote.setMinimumSize(QtCore.QSize(0, 40))
        self.txBookNote.setMaximumSize(QtCore.QSize(16777215, 40))
        self.txBookNote.setObjectName("txBookNote")
        self.verticalLayout_6.addWidget(self.txBookNote)
        self.txbookCategory = QtWidgets.QTextEdit(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txbookCategory.sizePolicy().hasHeightForWidth())
        self.txbookCategory.setSizePolicy(sizePolicy)
        self.txbookCategory.setMinimumSize(QtCore.QSize(0, 40))
        self.txbookCategory.setMaximumSize(QtCore.QSize(16777215, 40))
        self.txbookCategory.setObjectName("txbookCategory")
        self.verticalLayout_6.addWidget(self.txbookCategory)
        self.horizontalLayout_2.addLayout(self.verticalLayout_6)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.listWidget = QtWidgets.QListWidget(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(180)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setMinimumSize(QtCore.QSize(0, 180))
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_2.addWidget(self.listWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnAdd = QtWidgets.QPushButton(Dialog)
        self.btnAdd.setObjectName("btnAdd")
        self.horizontalLayout.addWidget(self.btnAdd)
        self.btnUpdate = QtWidgets.QPushButton(Dialog)
        self.btnUpdate.setObjectName("btnUpdate")
        self.horizontalLayout.addWidget(self.btnUpdate)
        self.btnDel = QtWidgets.QPushButton(Dialog)
        self.btnDel.setObjectName("btnDel")
        self.horizontalLayout.addWidget(self.btnDel)
        self.btnQuit = QtWidgets.QPushButton(Dialog)
        self.btnQuit.setObjectName("btnQuit")
        self.horizontalLayout.addWidget(self.btnQuit)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "书籍名称"))
        self.label_3.setText(_translate("Dialog", "助记码"))
        self.label_4.setText(_translate("Dialog", "条形码"))
        self.label_5.setText(_translate("Dialog", "作者"))
        self.label_10.setText(_translate("Dialog", "出版社"))
        self.label_11.setText(_translate("Dialog", "价格"))
        self.label_12.setText(_translate("Dialog", "备注"))
        self.label_13.setText(_translate("Dialog", "种类"))
        self.btnAdd.setText(_translate("Dialog", "增添"))
        self.btnUpdate.setText(_translate("Dialog", "修改"))
        self.btnDel.setText(_translate("Dialog", "删除"))
        self.btnQuit.setText(_translate("Dialog", "退出"))

