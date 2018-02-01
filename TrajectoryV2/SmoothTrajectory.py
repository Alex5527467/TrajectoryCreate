# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Alex\TrajectoryCreate\TrajectoryV2\SmoothTrajectory.ui'
#
# Created: Thu Feb 01 14:23:59 2018
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

import sys
import os
import math
import numpy as np
from math import pi
from PyQt4 import QtCore, QtGui
from scipy.interpolate import interp1d
from trajectory import SmoothTrajectory

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
        MainWindow.resize(1164, 899)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.widget = SmoothTrajectory(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 600, 600))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.tableView = QtGui.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(600, 0, 561, 361))
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.Angle_lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.Angle_lineEdit.setGeometry(QtCore.QRect(750, 450, 81, 21))
        self.Angle_lineEdit.setObjectName(_fromUtf8("Angle_lineEdit"))
        self.TranX_lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.TranX_lineEdit.setGeometry(QtCore.QRect(750, 480, 81, 20))
        self.TranX_lineEdit.setObjectName(_fromUtf8("TranX_lineEdit"))
        self.TranY_lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.TranY_lineEdit.setGeometry(QtCore.QRect(870, 480, 81, 20))
        self.TranY_lineEdit.setObjectName(_fromUtf8("TranY_lineEdit"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(720, 480, 16, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(850, 480, 16, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(710, 450, 41, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(620, 370, 82, 228))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.intialButton = QtGui.QPushButton(self.layoutWidget)
        self.intialButton.setObjectName(_fromUtf8("intialButton"))
        self.verticalLayout.addWidget(self.intialButton)
        self.smoothButton = QtGui.QPushButton(self.layoutWidget)
        self.smoothButton.setObjectName(_fromUtf8("smoothButton"))
        self.verticalLayout.addWidget(self.smoothButton)
        self.rotateButton = QtGui.QPushButton(self.layoutWidget)
        self.rotateButton.setObjectName(_fromUtf8("rotateButton"))
        self.verticalLayout.addWidget(self.rotateButton)
        self.translateButton = QtGui.QPushButton(self.layoutWidget)
        self.translateButton.setObjectName(_fromUtf8("translateButton"))
        self.verticalLayout.addWidget(self.translateButton)
        self.adjustButton = QtGui.QPushButton(self.layoutWidget)
        self.adjustButton.setObjectName(_fromUtf8("adjustButton"))
        self.verticalLayout.addWidget(self.adjustButton)
        self.createAButton = QtGui.QPushButton(self.layoutWidget)
        self.createAButton.setObjectName(_fromUtf8("createAButton"))
        self.verticalLayout.addWidget(self.createAButton)
        self.modifyAButton = QtGui.QPushButton(self.layoutWidget)
        self.modifyAButton.setObjectName(_fromUtf8("modifyAButton"))
        self.verticalLayout.addWidget(self.modifyAButton)
        self.saveButton = QtGui.QPushButton(self.layoutWidget)
        self.saveButton.setObjectName(_fromUtf8("saveButton"))
        self.verticalLayout.addWidget(self.saveButton)
        self.tableView_ShowPoint = QtGui.QTableView(self.centralwidget)
        self.tableView_ShowPoint.setGeometry(QtCore.QRect(0, 600, 601, 251))
        self.tableView_ShowPoint.setObjectName(_fromUtf8("tableView_ShowPoint"))
        self.tableView_ModifyA = QtGui.QTableView(self.centralwidget)
        self.tableView_ModifyA.setGeometry(QtCore.QRect(600, 600, 561, 251))
        self.tableView_ModifyA.setObjectName(_fromUtf8("tableView_ModifyA"))
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

        self.intialButton.clicked.connect(self.intial)
        self.smoothButton.clicked.connect(self.smooth)
        self.rotateButton.clicked.connect(self.rotate)
        self.translateButton.clicked.connect(self.translate)
        self.adjustButton.clicked.connect(self.adjust)
        self.createAButton.clicked.connect(self.createA)
        self.modifyAButton.clicked.connect(self.modifyA)
        self.saveButton.clicked.connect(self.save)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "初始轨迹", None))
        self.label.setText(_translate("MainWindow", "X:", None))
        self.label_2.setText(_translate("MainWindow", "Y:", None))
        self.label_3.setText(_translate("MainWindow", "Angle:", None))
        self.intialButton.setText(_translate("MainWindow", "Intial", None))
        self.smoothButton.setText(_translate("MainWindow", "Smooth", None))
        self.rotateButton.setText(_translate("MainWindow", "Rotate", None))
        self.translateButton.setText(_translate("MainWindow", "Translate", None))
        self.adjustButton.setText(_translate("MainWindow", "DelIterant", None))
        self.createAButton.setText(_translate("MainWindow", "CreateA", None))
        self.modifyAButton.setText(_translate("MainWindow", "ModifyA", None))
        self.saveButton.setText(_translate("MainWindow", "SavePra", None))

        self.Angle_lineEdit.setText(_translate("MainWindow", "-0.25*pi", None))
        self.TranX_lineEdit.setText(_translate("MainWindow", "1859", None))
        self.TranY_lineEdit.setText(_translate("MainWindow", "-383.665", None))
        self.tableView_set()#初始化表格
        self.tableView1_set()
        self.tableView2_set()



    def tableView1_set(self):  
          
        #添加表头：  
        self.model1 = QtGui.QStandardItemModel(self.tableView_ShowPoint)  
  
        #设置表格属性：  
        self.model1.setRowCount(17)    
        self.model1.setColumnCount(4)   
          
        #设置表头  
        self.model1.setHeaderData(0,QtCore.Qt.Horizontal,_fromUtf8(u"Num"))  
        self.model1.setHeaderData(1,QtCore.Qt.Horizontal,_fromUtf8(u"XHeight"))  
        self.model1.setHeaderData(2,QtCore.Qt.Horizontal,_fromUtf8(u"YHeight"))
        self.model1.setHeaderData(3,QtCore.Qt.Horizontal,_fromUtf8(u"Angle"))
        
        
        self.tableView_ShowPoint.setModel(self.model1)  
        #设置列宽  
        self.tableView_ShowPoint.setColumnWidth(0,50)  
        self.tableView_ShowPoint.setColumnWidth(1,100)  
        self.tableView_ShowPoint.setColumnWidth(2,100)
        self.tableView_ShowPoint.setColumnWidth(3,100)


        #表头信息显示居中  
        self.tableView_ShowPoint.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignCenter)



    def tableView2_set(self):  
          
        #添加表头：  
        self.model2 = QtGui.QStandardItemModel(self.tableView_ModifyA)  
  
        #设置表格属性：  
        self.model2.setRowCount(17)    
        self.model2.setColumnCount(3)   
          
        #设置表头  
        self.model2.setHeaderData(0,QtCore.Qt.Horizontal,_fromUtf8(u"BeginNum"))  
        self.model2.setHeaderData(1,QtCore.Qt.Horizontal,_fromUtf8(u"EndNum"))  
        self.model2.setHeaderData(2,QtCore.Qt.Horizontal,_fromUtf8(u"ModifyFuc"))

        lineNum=0
        with open('modifyApra.txt', 'r') as file_to_read:
            while True:
                lines = file_to_read.readline() # 整行读取数据
                if not lines:
                    break
                    pass
                a_tmp,b_tmp,c_tmp = [str(i) for i in lines.split()]
                self.model2.setItem(lineNum, 0,QtGui.QStandardItem(_fromUtf8(a_tmp)))
                self.model2.setItem(lineNum, 1,QtGui.QStandardItem(_fromUtf8(b_tmp)))
                self.model2.setItem(lineNum, 2,QtGui.QStandardItem(_fromUtf8(c_tmp)))
                lineNum=lineNum+1
                pass           
            pass
        
        self.tableView_ModifyA.setModel(self.model2)  
        #设置列宽  
        self.tableView_ModifyA.setColumnWidth(0,100)  
        self.tableView_ModifyA.setColumnWidth(1,100)  
        self.tableView_ModifyA.setColumnWidth(2,100)



        #表头信息显示居中  
        self.tableView_ModifyA.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignCenter)


    def tableView_set(self):  
          
        #添加表头：  
        self.model = QtGui.QStandardItemModel(self.tableView)  
  
        #设置表格属性：  
        self.model.setRowCount(17)    
        self.model.setColumnCount(4)   
          
        #设置表头  
        self.model.setHeaderData(0,QtCore.Qt.Horizontal,_fromUtf8(u"BeginNum"))  
        self.model.setHeaderData(1,QtCore.Qt.Horizontal,_fromUtf8(u"EndNum"))  
        self.model.setHeaderData(2,QtCore.Qt.Horizontal,_fromUtf8(u"InsertNum"))  
        self.model.setHeaderData(3,QtCore.Qt.Horizontal,_fromUtf8(u"SmoothorNot"))


        lineNum=0
        with open('smoothpar.txt', 'r') as file_to_read:
            while True:
                lines = file_to_read.readline() # 整行读取数据
                if not lines:
                    break
                    pass
                a_tmp,b_tmp,c_tmp,d_tmp = [str(i) for i in lines.split()]
                self.model.setItem(lineNum, 0,QtGui.QStandardItem(_fromUtf8(a_tmp)))
                self.model.setItem(lineNum, 1,QtGui.QStandardItem(_fromUtf8(b_tmp)))
                self.model.setItem(lineNum, 2,QtGui.QStandardItem(_fromUtf8(c_tmp)))
                self.model.setItem(lineNum, 3,QtGui.QStandardItem(_fromUtf8(d_tmp)))
                lineNum=lineNum+1
                pass           
            pass

        
      
        
        self.tableView.setModel(self.model)  
        #设置列宽  
        self.tableView.setColumnWidth(0,100)  
        self.tableView.setColumnWidth(1,100)  
        self.tableView.setColumnWidth(2,100)
        self.tableView.setColumnWidth(3,100)

        #表头信息显示居中  
        self.tableView.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignCenter)


        #定义槽  
    def intial(self):
        X=[]
        Y=[]
        XMark=[]
        YMark=[]
        CutPoint=[]
        with open('IntialPoint.txt', 'r') as file_to_read:
            while True:
                lines = file_to_read.readline() # 整行读取数据
                if not lines:
                    break
                    pass
                a_tmp,b_tmp,c_tmp,d_tmp = [str(i) for i in lines.split()]
                if d_tmp=='1':
                    X.append(eval(b_tmp))
                    Y.append(eval(c_tmp))
                    XMark.append(eval(b_tmp))
                    YMark.append(eval(c_tmp))
                    CutPoint.append(int(a_tmp))
                else:
                    X.append(eval(b_tmp))
                    Y.append(eval(c_tmp))
                
                pass           
            pass
        self.startPlot1(X,Y,XMark,YMark,CutPoint)
        fileObject = open('SmoothPoint.txt', 'w')
        for i in range(0,len(X)):
            fileObject.write(str(i)+' '+str(X[i])+' '+str(Y[i])+' 0')
            fileObject.write('\n')   
        fileObject.close()

        lineNum=0
        with open('SmoothPoint.txt', 'r') as file_to_read:
            while True:
                lines = file_to_read.readline() # 整行读取数据
                if not lines:
                    break
                    pass
                a_tmp,b_tmp,c_tmp,d_tmp = [str(i) for i in lines.split()]
                self.model1.setItem(lineNum, 0,QtGui.QStandardItem(_fromUtf8(a_tmp)))
                self.model1.setItem(lineNum, 1,QtGui.QStandardItem(_fromUtf8(b_tmp)))
                self.model1.setItem(lineNum, 2,QtGui.QStandardItem(_fromUtf8(c_tmp)))
                self.model1.setItem(lineNum, 3,QtGui.QStandardItem(_fromUtf8(d_tmp)))
                lineNum=lineNum+1
                pass           
            pass


    def smooth(self):
        X=[]
        Y=[]
        XNew=[]
        YNew=[]
        with open('SmoothPoint.txt', 'r') as file_to_read:
            while True:
                lines = file_to_read.readline() # 整行读取数据
                if not lines:
                    break
                    pass
                a_tmp,b_tmp,c_tmp,d_tmp = [str(i) for i in lines.split()]
                X.append(eval(b_tmp))
                Y.append(eval(c_tmp))
                pass           
            pass
        
        for im in range(0,17):
            a=self.model.data(self.model.index(im,0)).toPyObject()
            b=self.model.data(self.model.index(im,1)).toPyObject()
            c=self.model.data(self.model.index(im,2)).toPyObject()
            d=self.model.data(self.model.index(im,3)).toPyObject()
            if(a<>None and b<>None and c<>None and d<>None):
                if str(d)=='False':
                    XNew.extend(X[int(a):int(b)])
                    YNew.extend(Y[int(a):int(b)])
                if str(d)=='True':
                    xx = X[int(a):int(b)]        #为统一表格beginnum与finalnum规则待修改！！！！
                    yy = Y[int(a):int(b)]
                    xnew1 = xx
                    f = interp1d(xx, yy, kind='cubic')
                    for inew in range(0,int(c)):
                        dnew =X[int(a)]+(X[int(b)-1]-X[int(a)])*inew/int(c)
                        xnew1.append(dnew)
                    xnew1.sort()
                    ynew1 = f(xnew1)
                    XNew.extend(xnew1)
                    YNew.extend(ynew1)
            else:
                break
        self.startPlot2(XNew,YNew)
        
        fileObject = open('SmoothPoint.txt', 'w')
        for i in range(0,len(XNew)):
            fileObject.write(str(i)+' '+str(XNew[i])+' '+str(YNew[i])+' 0')
            fileObject.write('\n')            
        fileObject.close()

        lineNum=0
        with open('SmoothPoint.txt', 'r') as file_to_read:
            while True:
                lines = file_to_read.readline() # 整行读取数据
                if not lines:
                    break
                    pass
                a_tmp,b_tmp,c_tmp,d_tmp = [str(i) for i in lines.split()]
                self.model1.setItem(lineNum, 0,QtGui.QStandardItem(_fromUtf8(a_tmp)))
                self.model1.setItem(lineNum, 1,QtGui.QStandardItem(_fromUtf8(b_tmp)))
                self.model1.setItem(lineNum, 2,QtGui.QStandardItem(_fromUtf8(c_tmp)))
                self.model1.setItem(lineNum, 3,QtGui.QStandardItem(_fromUtf8(d_tmp)))
                lineNum=lineNum+1
                pass           
            pass

    def rotate(self):
        X=[]
        Y=[]
        A=[]
        XRotate=[]
        YRotate=[]
        angle=str(self.Angle_lineEdit.text())
        with open('SmoothPoint.txt', 'r') as file_to_read:
            while True:
                lines = file_to_read.readline() # 整行读取数据
                if not lines:
                    break
                    pass
                a_tmp,b_tmp,c_tmp,d_tmp = [str(i) for i in lines.split()]
                X.append(eval(b_tmp))
                Y.append(eval(c_tmp))
                A.append(eval(d_tmp))
                pass           
            pass
        
        for i in range(0,len(X)):
            xk1=X[i]
            yk1=Y[i]
            a1=math.cos(eval(angle))
            a2=math.sin(eval(angle)) 
            xk2=xk1*a1-yk1*a2
            yk2=xk1*a2+yk1*a1
            XRotate.append(xk2)
            YRotate.append(yk2)
        
        self.startPlot2(XRotate,YRotate)
        
        fileObject = open('SmoothPoint.txt', 'w')
        for i in range(0,len(XRotate)):
            fileObject.write(str(i)+' '+str(XRotate[i])+' '+str(YRotate[i])+' 0')
            fileObject.write('\n')
               
        fileObject.close()

        lineNum=0
        with open('SmoothPoint.txt', 'r') as file_to_read:
            while True:
                lines = file_to_read.readline() # 整行读取数据
                if not lines:
                    break
                    pass
                a_tmp,b_tmp,c_tmp,d_tmp = [str(i) for i in lines.split()]
                self.model1.setItem(lineNum, 0,QtGui.QStandardItem(_fromUtf8(a_tmp)))
                self.model1.setItem(lineNum, 1,QtGui.QStandardItem(_fromUtf8(b_tmp)))
                self.model1.setItem(lineNum, 2,QtGui.QStandardItem(_fromUtf8(c_tmp)))
                self.model1.setItem(lineNum, 3,QtGui.QStandardItem(_fromUtf8(d_tmp)))
                lineNum=lineNum+1
                pass           
            pass

        
    def translate(self):
        X=[]
        Y=[]
        XTranslate=[]
        YTranslate=[]
        xoffset=str(self.TranX_lineEdit.text())
        yoffset=str(self.TranY_lineEdit.text())
        with open('SmoothPoint.txt', 'r') as file_to_read:
            while True:
                lines = file_to_read.readline() # 整行读取数据
                if not lines:
                    break
                    pass
                a_tmp,b_tmp,c_tmp,d_tmp = [str(i) for i in lines.split()]
                X.append(eval(b_tmp))
                Y.append(eval(c_tmp))
                pass           
            pass
        
        for i in range(0,len(X)):
            xk1=X[i]+eval(xoffset)
            yk1=Y[i]+eval(yoffset)
            XTranslate.append(xk1)
            YTranslate.append(yk1)
        self.startPlot2(XTranslate,YTranslate)
        
        fileObject = open('SmoothPoint.txt', 'w')
        for i in range(0,len(XTranslate)):
            fileObject.write(str(i)+' '+str(XTranslate[i])+' '+str(YTranslate[i])+' 0')
            fileObject.write('\n')               
        fileObject.close()

        lineNum=0
        with open('SmoothPoint.txt', 'r') as file_to_read:
            while True:
                lines = file_to_read.readline() # 整行读取数据
                if not lines:
                    break
                    pass
                a_tmp,b_tmp,c_tmp,d_tmp = [str(i) for i in lines.split()]
                self.model1.setItem(lineNum, 0,QtGui.QStandardItem(_fromUtf8(a_tmp)))
                self.model1.setItem(lineNum, 1,QtGui.QStandardItem(_fromUtf8(b_tmp)))
                self.model1.setItem(lineNum, 2,QtGui.QStandardItem(_fromUtf8(c_tmp)))
                self.model1.setItem(lineNum, 3,QtGui.QStandardItem(_fromUtf8(d_tmp)))
                lineNum=lineNum+1
                pass           
            pass

    def adjust(self):
        xoffset=str(self.TranX_lineEdit.text())
        yoffset=str(self.TranY_lineEdit.text())
        X=[]
        Y=[]
        XAdjust=[]
        YAdjust=[]
        XMark=[]
        YMark=[]
        #偏移量
        Length1=313
        #主轴中心偏移坐标
        CircleOffset=1800
        with open('SmoothPoint.txt', 'r') as file_to_read:
            while True:
                lines = file_to_read.readline() # 整行读取数据
                if not lines:
                    break
                    pass
                a_tmp,b_tmp,c_tmp,d_tmp = [str(i) for i in lines.split()]
                X.append(eval(b_tmp))
                Y.append(eval(c_tmp))
                pass           
            pass
        
        for i in range(0,len(X)):
            xk1=X[i]
            yk1=Y[i]
            #yk11=yk1+CircleOffset
            #xk2=xk1*xk1
            #yk2=yk11*yk11
            #xyk1=math.sqrt(xk2+yk2)
            #ak1=math.acos(Length1/xyk1)
            #ak2=math.asin(yk11/xyk1)
            #ak3=ak1-ak2
            #xk3=xk1-Length1*math.cos(ak3)
            #yk3=yk1+Length1*math.sin(ak3)

            XAdjust.append(xk1)
            YAdjust.append(yk1)
        

       #删除重复点     
        DelCount=[]
        delnum=0
        for idel in range(0,len(X)-1):
            if(XAdjust[idel]==XAdjust[idel+1]):
                if(YAdjust[idel]==YAdjust[idel+1]):
                    DelCount.append(idel)
        for idel1 in DelCount:
            del XAdjust[idel1-delnum]
            del YAdjust[idel1-delnum]
            delnum=delnum+1

        

        
        self.startPlot2(XAdjust,YAdjust)
        
        fileObject = open('SmoothPoint.txt', 'w')
        for i in range(0,len(XAdjust)):
            fileObject.write(str(i)+' '+str(XAdjust[i])+' '+str(YAdjust[i])+' 0')
            fileObject.write('\n')

        fileObject.close()

        lineNum=0
        with open('SmoothPoint.txt', 'r') as file_to_read:
            while True:
                lines = file_to_read.readline() # 整行读取数据
                if not lines:
                    break
                    pass
                a_tmp,b_tmp,c_tmp,d_tmp = [str(i) for i in lines.split()]
                self.model1.setItem(lineNum, 0,QtGui.QStandardItem(_fromUtf8(a_tmp)))
                self.model1.setItem(lineNum, 1,QtGui.QStandardItem(_fromUtf8(b_tmp)))
                self.model1.setItem(lineNum, 2,QtGui.QStandardItem(_fromUtf8(c_tmp)))
                self.model1.setItem(lineNum, 3,QtGui.QStandardItem(_fromUtf8(d_tmp)))
                lineNum=lineNum+1
                pass           
            pass


    def createA(self):


        X=[]
        Y=[]
        XMark=[]
        YMark=[]
        #主轴中心偏移坐标
        CircleOffset=1800
        with open('SmoothPoint.txt', 'r') as file_to_read:
            while True:
                lines = file_to_read.readline() # 整行读取数据
                if not lines:
                    break
                    pass
                a_tmp,b_tmp,c_tmp,d_tmp = [str(i) for i in lines.split()]
                X.append(eval(b_tmp))
                Y.append(eval(c_tmp))
                pass           
            pass      

        Angle=[]

        xoffset=str(self.TranX_lineEdit.text())
        yoffset=str(self.TranY_lineEdit.text())

        for i in range(0,len(X)):
            xk1=X[i]
            yk1=Y[i]
            vector1X=0-xk1
            vector1Y=-1800-yk1
            vector2X=xk1-eval(xoffset)
            vector2Y=yk1-eval(yoffset)
            product=vector1X*vector2X+vector1Y*vector2Y
            normvector1=math.sqrt(vector1X*vector1X+vector1Y*vector1Y)
            normvector2=math.sqrt(vector2X*vector2X+vector2Y*vector2Y)
            innerproduct=product/normvector1/normvector2
            Angle.append(math.acos(innerproduct))

            
        
        fileObject = open('SmoothPoint.txt', 'w')
        for i in range(0,len(Angle)):
            fileObject.write(str(i)+' '+str(X[i])+' '+str(Y[i])+' '+str(Angle[i]))
            fileObject.write('\n')
        fileObject.close()


        lineNum=0
        with open('SmoothPoint.txt', 'r') as file_to_read:
            while True:
                lines = file_to_read.readline() # 整行读取数据
                if not lines:
                    break
                    pass
                a_tmp,b_tmp,c_tmp,d_tmp = [str(i) for i in lines.split()]
                self.model1.setItem(lineNum, 0,QtGui.QStandardItem(_fromUtf8(a_tmp)))
                self.model1.setItem(lineNum, 1,QtGui.QStandardItem(_fromUtf8(b_tmp)))
                self.model1.setItem(lineNum, 2,QtGui.QStandardItem(_fromUtf8(c_tmp)))
                self.model1.setItem(lineNum, 3,QtGui.QStandardItem(_fromUtf8(d_tmp)))
                lineNum=lineNum+1
                pass           
            pass


    def modifyA(self):
        X=[]
        Y=[]
        Angle=[]
        with open('SmoothPoint.txt', 'r') as file_to_read:
            while True:
                lines = file_to_read.readline() # 整行读取数据
                if not lines:
                    break
                    pass
                a_tmp,b_tmp,c_tmp,d_tmp = [str(i) for i in lines.split()]
                X.append(eval(b_tmp))
                Y.append(eval(c_tmp))
                Angle.append(eval(d_tmp))
                pass           
            pass
        XNew=[]
        YNew=[]
        ANew=[]
        for im in range(0,17):
            a=self.model2.data(self.model2.index(im,0)).toPyObject()
            b=self.model2.data(self.model2.index(im,1)).toPyObject()
            c=self.model2.data(self.model2.index(im,2)).toPyObject()
            if(a<>None and b<>None and c<>None  and a<>'' and b<>'' and c<>''):
                for i in range(int(a),int(b)):
                    a=Angle[int(i)]
                    ANew.append(eval(str(c)))
                    XNew.append(X[i])
                    YNew.append(Y[i])               
            else:
                break


        fileObject = open('SmoothPoint.txt', 'w')
        for i in range(0,len(ANew)):
            fileObject.write(str(i)+' '+str(XNew[i])+' '+str(YNew[i])+' '+str(ANew[i]))
            fileObject.write('\n')
        fileObject.close()


        lineNum=0
        with open('SmoothPoint.txt', 'r') as file_to_read:
            while True:
                lines = file_to_read.readline() # 整行读取数据
                if not lines:
                    break
                    pass
                a_tmp,b_tmp,c_tmp,d_tmp = [str(i) for i in lines.split()]
                self.model1.setItem(lineNum, 0,QtGui.QStandardItem(_fromUtf8(a_tmp)))
                self.model1.setItem(lineNum, 1,QtGui.QStandardItem(_fromUtf8(b_tmp)))
                self.model1.setItem(lineNum, 2,QtGui.QStandardItem(_fromUtf8(c_tmp)))
                self.model1.setItem(lineNum, 3,QtGui.QStandardItem(_fromUtf8(d_tmp)))
                lineNum=lineNum+1
                pass           
            pass

        
    
    
    def save(self):
        fileObject = open('smoothpar.txt', 'w')
        for im in range(0,17):
            a=self.model.data(self.model.index(im,0)).toPyObject()
            b=self.model.data(self.model.index(im,1)).toPyObject()
            c=self.model.data(self.model.index(im,2)).toPyObject()
            d=self.model.data(self.model.index(im,3)).toPyObject()
            if(a<>None and b<>None and c<>None and d<>None and
               a<>'' and b<>'' and c<>'' and d<>''):
                fileObject.write(str(a)+' '+str(b)+' '+str(c)+' '+str(d))
                fileObject.write('\n')
            else:
                break
        fileObject.close()
        
        fileObject = open('modifyApra.txt', 'w')
        for im in range(0,17):
            a=self.model2.data(self.model2.index(im,0)).toPyObject()
            b=self.model2.data(self.model2.index(im,1)).toPyObject()
            c=self.model2.data(self.model2.index(im,2)).toPyObject()
            if(a<>None and b<>None and c<>None and a<>'' and b<>'' and c<>''):
                fileObject.write(str(a)+' '+str(b)+' '+str(c))
                fileObject.write('\n')
            else:
                break
        fileObject.close()

class Code_MainWindow(Ui_MainWindow):
    def __init__(self, parent = None):
        super(Code_MainWindow, self).__init__(parent)
        self.setupUi(self)


    def startPlot1(self,x,y,xmark,ymark,cutpoint):
        ''' begin to plot'''
        self.widget.startPlot1(x,y,xmark,ymark,cutpoint)
        pass
    def startPlot2(self,x,y):
        ''' begin to plot'''
        self.widget.startPlot2(x,y)
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






