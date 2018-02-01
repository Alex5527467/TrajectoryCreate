# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Alex\Desktop\test\test1.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

import sys
import os
import datetime
from PyQt4 import QtCore, QtGui
from mplCanvasWrapper1 import mplCanvasWrapper1
from mplCanvasWrapper1 import mplCanvasWrapper2
from mplCanvasWrapper1 import mplCanvasWrapper3
from mplCanvasWrapper1 import mplCanvasWrapper4

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
        MainWindow.resize(1620, 1000)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.mplCanvas1 = mplCanvasWrapper1(self.centralwidget)
        self.mplCanvas1.setGeometry(QtCore.QRect(10, 10, 761, 411))
        self.mplCanvas1.setObjectName(_fromUtf8("mplCanvas1"))
        self.mplCanvas2 = mplCanvasWrapper2(self.centralwidget)
        self.mplCanvas2.setGeometry(QtCore.QRect(10, 470, 761, 451))
        self.mplCanvas2.setObjectName(_fromUtf8("mplCanvas2"))
        self.mplCanvas3 = mplCanvasWrapper3(self.centralwidget)
        self.mplCanvas3.setGeometry(QtCore.QRect(830, 10, 761, 411))
        self.mplCanvas3.setObjectName(_fromUtf8("mplCanvas3"))
        self.mplCanvas4 = mplCanvasWrapper4(self.centralwidget)
        self.mplCanvas4.setGeometry(QtCore.QRect(830, 470, 761, 451))
        self.mplCanvas4.setObjectName(_fromUtf8("mplCanvas4"))
        self.slid_1 = QtGui.QScrollBar(self.centralwidget)
        self.slid_1.setGeometry(QtCore.QRect(10, 420, 751, 20))
        self.slid_1.setMaximum(500)
        self.slid_1.setSliderPosition(500)
        self.slid_1.setOrientation(QtCore.Qt.Horizontal)
        self.slid_1.setObjectName(_fromUtf8("slid_1"))
        self.slid_1.valueChanged[int].connect(self.changeValue1)
        self.slid_3 = QtGui.QScrollBar(self.centralwidget)
        self.slid_3.setGeometry(QtCore.QRect(830, 420, 751, 20))
        self.slid_3.setMaximum(500)
        self.slid_3.setSliderPosition(500)
        self.slid_3.setOrientation(QtCore.Qt.Horizontal)
        self.slid_3.setObjectName(_fromUtf8("slid_3"))
        self.slid_2 = QtGui.QScrollBar(self.centralwidget)
        self.slid_2.setGeometry(QtCore.QRect(10, 920, 751, 20))
        self.slid_2.setMaximum(500)
        self.slid_2.setSliderPosition(500)
        self.slid_2.setOrientation(QtCore.Qt.Horizontal)
        self.slid_2.setObjectName(_fromUtf8("slid_2"))
        self.slid_4 = QtGui.QScrollBar(self.centralwidget)
        self.slid_4.setGeometry(QtCore.QRect(830, 920, 751, 20))
        self.slid_4.setMaximum(500)
        self.slid_4.setSliderPosition(500)
        self.slid_4.setOrientation(QtCore.Qt.Horizontal)
        self.slid_4.setObjectName(_fromUtf8("slid_4"))
        self.slid_2.valueChanged[int].connect(self.changeValue2)
        self.slid_3.valueChanged[int].connect(self.changeValue3)
        self.slid_4.valueChanged[int].connect(self.changeValue4)
        self.mplCanvas1.raise_()
        self.mplCanvas2.raise_()
        self.mplCanvas3.raise_()
        self.mplCanvas4.raise_()
        self.slid_3.raise_()
        self.slid_1.raise_()
        self.slid_3.raise_()
        self.slid_2.raise_()
        self.slid_4.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1620, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "历史图表", None))

class Code_MainWindow(Ui_MainWindow):
    def __init__(self, parent = None):
        super(Code_MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.startPlot1()
        self.startPlot2()
        self.startPlot3()
        self.startPlot4()
    def startPlot1(self):
        ''' begin to plot'''
        now= datetime.datetime.now()
        delta = datetime.timedelta(days=1)
        n_days = now-delta
        self.begintime=n_days
        self.overtime= now 
        self.mplCanvas1.startPlot1(self.begintime,self.overtime)
        pass
    
    def startPlot2(self):
        ''' begin to plot'''
        now1= datetime.datetime.now()
        delta1 = datetime.timedelta(days=1)
        n_days1 = now1-delta1
        self.begintime=n_days1
        self.overtime= now1 
        self.mplCanvas2.startPlot1(self.begintime,self.overtime)
        pass
    def startPlot3(self):
        ''' begin to plot'''
        now1= datetime.datetime.now()
        delta1 = datetime.timedelta(days=1)
        n_days1 = now1-delta1
        self.begintime=n_days1
        self.overtime= now1 
        self.mplCanvas3.startPlot1(self.begintime,self.overtime)
        pass

    def startPlot4(self):
        ''' begin to plot'''
        now1= datetime.datetime.now()
        delta1 = datetime.timedelta(days=1)
        n_days1 = now1-delta1
        self.begintime=n_days1
        self.overtime= now1 
        self.mplCanvas4.startPlot1(self.begintime,self.overtime)
        pass
    
    
    
    def closeEvent(self,event):
        result = QtGui.QMessageBox.question(self,
                      "Confirm Exit...",
                      "Are you sure you want to exit ?",
                          QtGui.QMessageBox.Yes| QtGui.QMessageBox.No)
        event.ignore()
 
        if result == QtGui.QMessageBox.Yes:
            event.accept()

    def changeValue1(self, value):
        a=500-value
        now= datetime.datetime.now()
        delta1=datetime.timedelta(minutes=a)
        delta2=datetime.timedelta(hours=1)
        n_days1 = now-delta1
        n_days2 = n_days1-delta2
        self.begintime=n_days2
        self.overtime=n_days1 
        self.mplCanvas1.startPlot1(self.begintime,self.overtime)
        
    def changeValue2(self, value):
        a=500-value
        now= datetime.datetime.now()
        delta1=datetime.timedelta(minutes=a)
        delta2=datetime.timedelta(hours=1)
        n_days1 = now-delta1
        n_days2 = n_days1-delta2
        self.begintime=n_days2
        self.overtime=n_days1 
        self.mplCanvas2.startPlot1(self.begintime,self.overtime)

    def changeValue3(self, value):
        a=500-value
        now= datetime.datetime.now()
        delta1=datetime.timedelta(minutes=a)
        delta2=datetime.timedelta(hours=1)
        n_days1 = now-delta1
        n_days2 = n_days1-delta2
        self.begintime=n_days2
        self.overtime=n_days1 
        self.mplCanvas3.startPlot1(self.begintime,self.overtime)
        
    def changeValue4(self, value):
        a=500-value
        now= datetime.datetime.now()
        delta1=datetime.timedelta(minutes=a)
        delta2=datetime.timedelta(hours=1)
        n_days1 = now-delta1
        n_days2 = n_days1-delta2
        self.begintime=n_days2
        self.overtime=n_days1 
        self.mplCanvas4.startPlot1(self.begintime,self.overtime)
        

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ui = Code_MainWindow()
    ui.show()
sys.exit(app.exec_())

