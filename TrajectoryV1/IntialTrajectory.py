# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Alex\Desktop\Robot\PathGeneration20171101\Trajectory\IntialTrajectory.ui'
#
# Created: Wed Jan 31 08:37:04 2018
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

import sys
import os
import numpy as np
from math import pi
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from trajectory import IntialTrajectory

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
        MainWindow.resize(1164, 644)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.widget = IntialTrajectory(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 600, 600))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.createButton = QtGui.QPushButton(self.centralwidget)
        self.createButton.setGeometry(QtCore.QRect(639, 450, 75, 23))
        self.createButton.setObjectName(_fromUtf8("createButton"))
        self.tableView = QtGui.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(600, 0, 561, 371))
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.saveButton = QtGui.QPushButton(self.centralwidget)
        self.saveButton.setGeometry(QtCore.QRect(640, 410, 75, 23))
        self.saveButton.setObjectName(_fromUtf8("saveButton"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1164, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.createButton.clicked.connect(self.create)   
        self.saveButton.clicked.connect(self.save) 

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "初始轨迹", None))
        self.createButton.setText(_translate("MainWindow", "Create", None))
        self.saveButton.setText(_translate("MainWindow", "SavePra", None))

        self.tableView_set()#初始化表格


    def tableView_set(self):  
          
        #添加表头：  
        self.model = QtGui.QStandardItemModel(self.tableView)  
  
        #设置表格属性：  
        self.model.setRowCount(17)    
        self.model.setColumnCount(5)   
          
        #设置表头  
        self.model.setHeaderData(0,QtCore.Qt.Horizontal,_fromUtf8(u"X Formula"))  
        self.model.setHeaderData(1,QtCore.Qt.Horizontal,_fromUtf8(u"Y Formula"))  
        self.model.setHeaderData(2,QtCore.Qt.Horizontal,_fromUtf8(u"PointNum"))  
        self.model.setHeaderData(3,QtCore.Qt.Horizontal,_fromUtf8(u"BeginNum"))
        self.model.setHeaderData(4,QtCore.Qt.Horizontal,_fromUtf8(u"EndNum"))



        lineNum=0
        with open('function.txt', 'r') as file_to_read:
            while True:
                lines = file_to_read.readline() # 整行读取数据
                if not lines:
                    break
                    pass
                a_tmp,b_tmp,c_tmp,d_tmp,e_tmp = [str(i) for i in lines.split()]
                self.model.setItem(lineNum, 0,QtGui.QStandardItem(_fromUtf8(a_tmp)))
                self.model.setItem(lineNum, 1,QtGui.QStandardItem(_fromUtf8(b_tmp)))
                self.model.setItem(lineNum, 2,QtGui.QStandardItem(_fromUtf8(c_tmp)))
                self.model.setItem(lineNum, 3,QtGui.QStandardItem(_fromUtf8(d_tmp)))
                self.model.setItem(lineNum, 4,QtGui.QStandardItem(_fromUtf8(e_tmp)))
                lineNum=lineNum+1
                pass           
            pass

        
        #self.model.setItem(0, 0,QtGui.QStandardItem(_fromUtf8(u'720*np.sin(i*1.9*pi/n-0.5*pi)')))
        #self.model.setItem(0, 1,QtGui.QStandardItem(_fromUtf8(u'720*np.cos(i*1.9*pi/n-0.5*pi)')))
        #self.model.setItem(0, 2,QtGui.QStandardItem(_fromUtf8(u'500')))
        #self.model.setItem(0, 3,QtGui.QStandardItem(_fromUtf8(u'0')))
        #self.model.setItem(0, 4,QtGui.QStandardItem(_fromUtf8(u'490')))
        
        self.tableView.setModel(self.model)  
        #设置列宽  
        self.tableView.setColumnWidth(0,200)  
        self.tableView.setColumnWidth(1,200)  
        self.tableView.setColumnWidth(2,70)
        self.tableView.setColumnWidth(3,70)
        self.tableView.setColumnWidth(4,70)
        #表头信息显示居中  
        self.tableView.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignCenter)




        #定义槽  
    def create(self):
        x=[]
        y=[]
        xMark=[]
        yMark=[]
        CutNum=-1
        CutPoint=[]
        for im in range(0,17):
            a=self.model.data(self.model.index(im,0)).toPyObject()
            b=self.model.data(self.model.index(im,1)).toPyObject()
            c=self.model.data(self.model.index(im,2)).toPyObject()
            d=self.model.data(self.model.index(im,3)).toPyObject()
            e=self.model.data(self.model.index(im,4)).toPyObject()
            if(a<>None and b<>None and c<>None and d<>None and e<>None):
                n=int(c)
                for i in range(int(d),int(e)):
                    x.append(eval(str(a)))
                    y.append(eval(str(b)))
                CutNum=CutNum+1
                CutPoint.append(CutNum)
                CutNum=CutNum+int(e)-int(d)-1
                CutPoint.append(CutNum)
            else:
                break

        for ik in CutPoint:
            xMark.append(x[ik])
            yMark.append(y[ik])

        self.startPlot1(x,y,xMark,yMark)


        fileObject = open('IntialPoint.txt', 'w')
        for i in range(0,len(x)):
            if i in CutPoint:
                fileObject.write(str(i)+' '+str(x[i])+' '+str(y[i])+' 1')
                fileObject.write('\n')
            else:
                fileObject.write(str(i)+' '+str(x[i])+' '+str(y[i])+' 0')
                fileObject.write('\n')
            
        fileObject.close() 




    def save(self):
        fileObject = open('function.txt', 'w')
        for im in range(0,17):
            a=self.model.data(self.model.index(im,0)).toPyObject()
            b=self.model.data(self.model.index(im,1)).toPyObject()
            c=self.model.data(self.model.index(im,2)).toPyObject()
            d=self.model.data(self.model.index(im,3)).toPyObject()
            e=self.model.data(self.model.index(im,4)).toPyObject()
            if(a<>None and b<>None and c<>None and d<>None and e<>None):
                fileObject.write(str(a)+' '+str(b)+' '+str(c)+' '+str(d)+' '+str(e))
                fileObject.write('\n')
            else:
                break
        fileObject.close() 


class Code_MainWindow(Ui_MainWindow):
    def __init__(self, parent = None):
        super(Code_MainWindow, self).__init__(parent)
        self.setupUi(self)


    def startPlot1(self,x,y,xmark,ymark):
        ''' begin to plot'''
        self.widget.startPlot1(x,y,xmark,ymark)
        pass
        
    
    
    def closeEvent(self,event):
        result = QtGui.QMessageBox.question(self,
                      "Confirm Exit...",
                      "Are you sure you want to exit ?",
                          QtGui.QMessageBox.Yes| QtGui.QMessageBox.No)
        event.ignore()
 
        if result == QtGui.QMessageBox.Yes:
            event.accept()


        
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ui = Code_MainWindow()
    ui.show()
sys.exit(app.exec_())



