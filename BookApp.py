uis = {} 

# 定义全局变量
#class G:
searchs = {}
gSearch_book_infos = None 

def show_window(name):
    w = uis[name]
    if w:
        w.show()

def hide_window(name):
    w = uis[name]
    if w:
        w.hide()

def get_window(name):
    w = uis[name]
    if w:
        return w
    return NULL

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QLineEdit
from PyQt5.Qt import * # 包含了Qt.Key_Return

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
            gSearch_book_infos()
            


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
