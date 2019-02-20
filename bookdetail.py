# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bookdetail2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QLineEdit, QMessageBox

import BookApp as app
import LYUtils as utils

class Ui_Dialog(QDialog):

    def init_ui(self, bookDetail):
        QDialog.__init__(self)
        print("bookdetail init ui")
        self.setupUi(bookDetail)
        self.bookInfoUpdate = {}

    def init_ui_action(self):
        self.btnQuit.clicked.connect(self.quit_book_detail)
        self.btnUpdate.clicked.connect(self.update_book_detail_alert)
        self.btnDel.clicked.connect(self.del_book_detail)
        pass

    def init_ui_data(self, bookDetailInfo):
        self.bookInfoUpdate = bookDetailInfo

        self.txBookName.setText(bookDetailInfo['name'])
        self.txBookJZCode.setText(bookDetailInfo['jzc'])
        self.txBookBarCode.setText(bookDetailInfo['ISBN'])
        self.txBookAuthor.setText(bookDetailInfo['author'])
        self.txBookPress.setText(bookDetailInfo['press'])
        self.txBookPrice.setText(str(bookDetailInfo['price']))
        self.txBookNote.setText(bookDetailInfo['notes'])

        # 查询数据中图书种类category信息
        categories = list(utils.DBManager().get_category())
    
        bookInfoCategory = bookDetailInfo['category']
        categories.insert(0, {'name':''})
        self.txBookCategory.clear() # 清空所有items
        for category in categories:
            self.txBookCategory.addItem(category['name'])
            # 判断图书的默认种类category值
            if category['name'] == bookInfoCategory:
                self.txBookCategory.setCurrentText(category['name'])

        self.txBookCategory.activated.connect(self.selection_book_category)
        self.txBookCategory.currentTextChanged.connect(self.selection_book_category_txt)
    
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(518, 300)
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
        self.txBookName = QtWidgets.QLineEdit(Dialog)
        self.txBookName.setMinimumSize(QtCore.QSize(0, 40))
        self.txBookName.setMaximumSize(QtCore.QSize(16777215, 40))
        self.txBookName.setObjectName("txBookName")
        self.verticalLayout_3.addWidget(self.txBookName)
        self.txBookJZCode = QtWidgets.QTextEdit(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txBookJZCode.sizePolicy().hasHeightForWidth())
        self.txBookJZCode.setSizePolicy(sizePolicy)
        self.txBookJZCode.setMaximumSize(QtCore.QSize(16777215, 40))
        self.txBookJZCode.setObjectName("txBookJZCode")
        self.verticalLayout_3.addWidget(self.txBookJZCode)
        self.txBookBarCode = QtWidgets.QTextEdit(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txBookBarCode.sizePolicy().hasHeightForWidth())
        self.txBookBarCode.setSizePolicy(sizePolicy)
        self.txBookBarCode.setMaximumSize(QtCore.QSize(16777215, 40))
        self.txBookBarCode.setObjectName("txBookBarCode")
        self.verticalLayout_3.addWidget(self.txBookBarCode)
        self.txBookAuthor = QtWidgets.QTextEdit(Dialog)
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
        self.txBookPress = QtWidgets.QTextEdit(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txBookPress.sizePolicy().hasHeightForWidth())
        self.txBookPress.setSizePolicy(sizePolicy)
        self.txBookPress.setMinimumSize(QtCore.QSize(0, 40))
        self.txBookPress.setMaximumSize(QtCore.QSize(16777215, 40))
        self.txBookPress.setObjectName("txBookPress")
        self.verticalLayout_6.addWidget(self.txBookPress)
        self.txBookPrice = QtWidgets.QTextEdit(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txBookPrice.sizePolicy().hasHeightForWidth())
        self.txBookPrice.setSizePolicy(sizePolicy)
        self.txBookPrice.setMinimumSize(QtCore.QSize(0, 40))
        self.txBookPrice.setMaximumSize(QtCore.QSize(16777215, 40))
        self.txBookPrice.setObjectName("txBookPrice")
        self.verticalLayout_6.addWidget(self.txBookPrice)
        self.txBookNote = QtWidgets.QTextEdit(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txBookNote.sizePolicy().hasHeightForWidth())
        self.txBookNote.setSizePolicy(sizePolicy)
        self.txBookNote.setMinimumSize(QtCore.QSize(0, 40))
        self.txBookNote.setMaximumSize(QtCore.QSize(16777215, 40))
        self.txBookNote.setObjectName("txBookNote")
        self.verticalLayout_6.addWidget(self.txBookNote)
        self.txBookCategory = QtWidgets.QComboBox(Dialog)
        self.txBookCategory.setMinimumSize(QtCore.QSize(0, 40))
        self.txBookCategory.setMaximumSize(QtCore.QSize(16777215, 40))
        self.txBookCategory.setObjectName("txBookCategory")
        self.verticalLayout_6.addWidget(self.txBookCategory)
        self.horizontalLayout_2.addLayout(self.verticalLayout_6)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        spacerItem = QtWidgets.QSpacerItem(20, 38, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnUpdate = QtWidgets.QPushButton(Dialog)
        self.btnUpdate.setObjectName("btnUpdate")
        self.horizontalLayout.addWidget(self.btnUpdate)
        self.btnDel = QtWidgets.QPushButton(Dialog)
        self.btnDel.setObjectName("btnDel")
        self.horizontalLayout.addWidget(self.btnDel)
        self.horizontalLayout_5.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.btnQuit = QtWidgets.QPushButton(Dialog)
        self.btnQuit.setObjectName("btnQuit")
        self.horizontalLayout_5.addWidget(self.btnQuit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "图书信息"))
        self.label.setText(_translate("Dialog", "书籍名称"))
        self.label_3.setText(_translate("Dialog", "助记码"))
        self.label_4.setText(_translate("Dialog", "条形码"))
        self.label_5.setText(_translate("Dialog", "作者"))
        self.label_10.setText(_translate("Dialog", "出版社"))
        self.label_11.setText(_translate("Dialog", "价格"))
        self.label_12.setText(_translate("Dialog", "备注"))
        self.label_13.setText(_translate("Dialog", "种类"))
        self.btnUpdate.setText(_translate("Dialog", "修改"))
        self.btnDel.setText(_translate("Dialog", "删除"))
        self.btnQuit.setText(_translate("Dialog", "退出"))

    def quit_book_detail(self):
        app.hide_window('bookdetail')
        app.show_window('bookinfo')

    def update_book_detail_alert(self):

        box = QMessageBox(QMessageBox.Question, self.tr("提示"), self.tr("是否更新图书信息?!"), QMessageBox.NoButton, self)
        yr_btn = box.addButton(self.tr("是"), QMessageBox.YesRole)
        box.addButton(self.tr("否"), QMessageBox.NoRole)
        box.exec_()
        if box.clickedButton() == yr_btn:
            print ('Bye bye...')
            self.update_book_detail()
            return
        else:
            print ('继续...')
        return

    def update_book_detail(self):
        # update book info
        name = self.txBookName.text()
        jzc  = self.txBookJZCode.toPlainText()
        isbn = self.txBookBarCode.toPlainText()
        author = self.txBookAuthor.toPlainText()
        press = self.txBookPress.toPlainText()
        price = self.txBookPrice.toPlainText()
        notes = self.txBookNote.toPlainText()

        self.bookInfoUpdate['name'] = name
        self.bookInfoUpdate['jzc']  = jzc
        self.bookInfoUpdate['ISBN'] = isbn
        self.bookInfoUpdate['author'] = author
        self.bookInfoUpdate['press'] = press
        self.bookInfoUpdate['price'] = price
        self.bookInfoUpdate['notes'] = notes

        utils.DBManager().update_book_detail(self.bookInfoUpdate)

    def del_book_detail(self):
        pass

    def selection_book_category(self, index):
        print(index)

    def selection_book_category_txt(self, txt):
        self.txBookCategory.setCurrentText(txt)
        self.bookInfoUpdate['category'] = txt


    """对QDialog类重写，实现一些功能"""""
    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(self, '提示',"是否退出?!",QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,QtWidgets.QMessageBox.No)
            
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
            app.uis['bookinfo'].search_book_info()
            app.show_window('bookinfo')
        else:
            event.ignore()
