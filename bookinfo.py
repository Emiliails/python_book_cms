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
import LYUtils as utils

class Ui_Dialog(QDialog):

    def init_ui(self, bookInfo):
        print("bookinfo init ui")
        self.books = []
        self.bookSort = [0,0,0,0,0,0,0,0]
        self.rowCnt = 0

        self.setupUi(bookInfo)
        self.init_ui_data()

        self.tableWidget.setColumnCount(8)
        self.tableWidget.setHorizontalHeaderLabels(
                ['书籍名称', '作者', '出版社', '价格', 'ISBN', '助记码', '种类', '备注'])
        self.tableWidget.setRowCount(0)
        
        # 设置水平方向表格为自适应的伸缩模式
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # 禁止修改
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 整行选中的方式
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        # 绑定signal信号事件， 根据类提供的信号事件进行绑定
        # self.tableWidget.itemClicked.connect(self.selection_item)
        self.tableWidget.itemDoubleClicked.connect(self.selection_item_double)
        # 表头的排序功能，默认是升序
        self.tableWidget.horizontalHeader().setSortIndicator(0, Qt.AscendingOrder)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget.horizontalHeader().sectionClicked.connect(self.hor_sort_clicked)

    def init_ui_action(self):
        self.btnQuit.clicked.connect(self.exit_book_info)
        self.btnAdd.clicked.connect(self.go_to_book_add)

    def init_ui_data(self):
        # 查询数据中图书种类category信息
        categories = list(utils.DBManager().get_category())
    
        categories.insert(0, {'name':''})
        for category in categories:
            print("{0}".format(category))
            self.txBookCategory.addItem(category['name'])

        self.txBookCategory.activated.connect(self.selection_book_category)
        self.txBookCategory.currentTextChanged.connect(self.selection_book_category_txt)


    def setupUi(self, Dialog):
        funcs = {'search_book_info': self.search_book_info}
        app.gSearch_book_infos = self.search_book_info

        Dialog.setObjectName("Dialog")
        Dialog.resize(649, 536)
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
        self.txBookName = app.MyTextEdit(Dialog, 'name')
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
       
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setObjectName("tableWidget")

        self.verticalLayout_2.addWidget(self.tableWidget)
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
        Dialog.setWindowTitle(_translate("Dialog", "图书信息"))
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

    def exit_book_info(self):
        app.hide_window('bookinfo')
        app.show_window('mainmenu')

    def go_to_book_add(self):
        '''
        进入添加图书信息界面
        '''
        dialog = app.get_window('bookadd')
        dialog.init_ui_action()
        dialog.init_ui_data()
        dialog.show()

        app.show_window('bookadd')
        app.hide_window('bookinfo')


    def get_books_list(self):
        bookInfo = {}
        for (k, v) in app.searchs.items():
            if app.searchs[k] != '':
                # 模糊查找
                bookInfo[k] = {"$regex":v, "$options":'$i'}

        print('total search conditions:' + str(bookInfo))
        books = list(utils.DBManager().search(bookInfo))
        print("{0}".format(books))
        return books


    def search_book_info(self):
        """
        #print('total search conditions:' + str(G.searchs))
        bookInfo = {}
        for (k, v) in app.searchs.items():
            if app.searchs[k] != '':
                # 模糊查找
                bookInfo[k] = {"$regex":v, "$options":'$i'}

        self.books = list(utils.DBManager().search(bookInfo))
        """
        self.books = self.get_books_list()
        """
        self.tableWidget.setRowCount(self.rowCnt+1)
        itemName = QtWidgets.QTableWidgetItem(books[0]['name'])
        itemName.setBackground(QColor(100,100,200))
        self.tableWidget.setItem(self.rowCnt, 0, itemName)
        """
        
        self.refresh_book_list()

    def selection_item_double(self):
        '''
        双击表单的数据项
        '''
        print(self.tableWidget.currentRow())
        index = self.tableWidget.currentRow()
        print((self.books[index]))

        dialog = app.get_window('bookdetail')
        dialog.setModal(True)        
        #dialog.setupUi(dialog)
        #dialog.init_ui_action()
        dialog.init_ui_data(self.books[index])
        dialog.init_ui_action()

        dialog.show()
        app.hide_window('bookinfo')

    def selection_book_category(self, index):
        print(index)


    def selection_book_category_txt(self, txt):
        app.searchs['category'] = txt
        self.books = self.get_books_list()
        self.refresh_book_list()
            

    def hor_sort_clicked(self, index):
        print("index{0}:".format(index))
        print("len:{0}".format(len(self.bookSort)))

        keyName = ''
        if index == 0:
            keyName = 'name'
        elif index == 3:
            keyName = 'price'
   
        if self.bookSort[index] == utils.Sort.DESC: 
            self.bookSort[index] = utils.Sort.ASC 
        else: 
            self.bookSort[index] = utils.Sort.DESC

        utils.quick_sort(self.books, key=keyName, sort=self.bookSort[index])
        self.refresh_book_list()


    def refresh_book_list(self):
        self.tableWidget.clear()
        self.rowCnt = 0
        self.tableWidget.setRowCount(self.rowCnt)
        self.tableWidget.setHorizontalHeaderLabels(
                ['书籍名称', '作者', '出版社', '价格', 'ISBN', '助记码', '种类', '备注'])

        for abook in self.books: 
            self.tableWidget.setRowCount(self.rowCnt+1)
            itemName = QtWidgets.QTableWidgetItem(abook['name'])
            self.tableWidget.setItem(self.rowCnt, 0, itemName)
        
            itemAuthor = QtWidgets.QTableWidgetItem(abook['author'])
            self.tableWidget.setItem(self.rowCnt, 1, itemAuthor)
        
            newItem = QtWidgets.QTableWidgetItem(abook['press'])
            self.tableWidget.setItem(self.rowCnt, 2, newItem)

            newItem = QtWidgets.QTableWidgetItem(str(abook['price']))
            self.tableWidget.setItem(self.rowCnt, 3, newItem)
        
            newItem = QtWidgets.QTableWidgetItem(abook['ISBN'])
            self.tableWidget.setItem(self.rowCnt, 4, newItem)
        
            newItem = QtWidgets.QTableWidgetItem(abook['jzc'])
            self.tableWidget.setItem(self.rowCnt, 5, newItem)
                
            newItem = QtWidgets.QTableWidgetItem(abook['category'])
            self.tableWidget.setItem(self.rowCnt, 6, newItem)
        
            newItem = QtWidgets.QTableWidgetItem(abook['notes'])
            self.tableWidget.setItem(self.rowCnt, 7, newItem)
            
            # 设置任务操作 添加多个按钮
            """
            checkBtn = QtWidgets.QPushButton('修改')
            checkBtn.clicked.connect(lambda:self.update_book_info(abook, name, checkBtn))
            delBtn  = QtWidgets.QPushButton('删除')
            delBtn.clicked.connect(lambda:self.delete_book_info(abook, name))
        
            hLayout = QtWidgets.QHBoxLayout()
            hLayout.addWidget(checkBtn)
            hLayout.addWidget(delBtn)
            hLayout.setContentsMargins(0,0,0,0)
            hLayout.setAlignment(Qt.AlignCenter)
            widget = QtWidgets.QWidget()
            widget.setLayout(hLayout)
            self.tableWidget.setCellWidget(self.rowCnt, 0, checkBtn)
            """
            self.rowCnt+=1 

