# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\酿酒线\test\test.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

import sys
import os
import datetime
from PyQt4 import QtCore, QtGui
from mplCanvasWrapper import mplCanvasWrapper1

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(QtGui.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1900, 1000)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.mplCanvas1 = mplCanvasWrapper1(self.centralwidget)
        self.mplCanvas1.setGeometry(QtCore.QRect(0, 0, 1900, 950))
        self.mplCanvas1.setObjectName(_fromUtf8("mplCanvas1"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1900, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "即时曲线", None))

class Code_MainWindow(Ui_MainWindow):
    def __init__(self, parent = None):
        super(Code_MainWindow, self).__init__(parent)
        self.setupUi(self)

    
    def initdata(self):
        self.mplCanvas1.initDataGenerator()
        pass
       
    def releasePlot(self):
        ''' stop and release thread'''
        self.mplCanvas1.releasePlot()
 
    def closeEvent(self,event):
        result = QtGui.QMessageBox.question(self,
                      "Confirm Exit...",
                      "Are you sure you want to exit ?",
                      QtGui.QMessageBox.Yes| QtGui.QMessageBox.No)
        event.ignore()
 
        if result == QtGui.QMessageBox.Yes:
            self.releasePlot()#release thread's resouce
            event.accept()
 
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ui = Code_MainWindow()
    ui.show()
sys.exit(app.exec_())

