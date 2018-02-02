# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Alex\Desktop\Robot\PathGeneration20171101\Trajectory\SpeedTrajectory.ui'
#
# Created: Tue Jan 30 15:29:43 2018
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

import sys
import os
import math
import numpy as np
from math import pi
from PyQt4 import QtCore, QtGui
from trajectory3d import D3Trajectory
from trajectory import SpeedTrajectory
from trajectory import LinearSpeedTrajectory

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
        MainWindow.resize(1446, 912)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.widget = D3Trajectory(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 500, 500))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.LowV_lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.LowV_lineEdit.setGeometry(QtCore.QRect(1130, 70, 71, 21))
        self.LowV_lineEdit.setObjectName(_fromUtf8("LowV_lineEdit"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(1090, 70, 41, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(1090, 100, 41, 21))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.HighV_lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.HighV_lineEdit.setGeometry(QtCore.QRect(1130, 100, 71, 21))
        self.HighV_lineEdit.setObjectName(_fromUtf8("HighV_lineEdit"))
        self.tableView = QtGui.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(1000, 220, 441, 281))
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.widget_2 = SpeedTrajectory(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(500, 0, 500, 500))
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.widget_3 = LinearSpeedTrajectory(self.centralwidget)
        self.widget_3.setGeometry(QtCore.QRect(0, 500, 1001, 361))
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.tableView_ShowPoint = QtGui.QTableView(self.centralwidget)
        self.tableView_ShowPoint.setGeometry(QtCore.QRect(1000, 500, 441, 361))
        self.tableView_ShowPoint.setObjectName(_fromUtf8("tableView_ShowPoint"))
        self.MarkNum_lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.MarkNum_lineEdit.setGeometry(QtCore.QRect(1130, 130, 71, 21))
        self.MarkNum_lineEdit.setObjectName(_fromUtf8("MarkNum_lineEdit"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(1095, 130, 21, 21))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.ShowNum1_lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.ShowNum1_lineEdit.setGeometry(QtCore.QRect(1130, 40, 71, 21))
        self.ShowNum1_lineEdit.setObjectName(_fromUtf8("ShowNum1_lineEdit"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(1210, 40, 31, 21))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.ShowNum2_lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.ShowNum2_lineEdit.setGeometry(QtCore.QRect(1240, 40, 81, 21))
        self.ShowNum2_lineEdit.setObjectName(_fromUtf8("ShowNum2_lineEdit"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(1090, 40, 31, 21))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.widget1 = QtGui.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(1010, 11, 77, 170))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget1)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.intialButton = QtGui.QPushButton(self.widget1)
        self.intialButton.setObjectName(_fromUtf8("intialButton"))
        self.verticalLayout.addWidget(self.intialButton)
        self.speedcreateButton = QtGui.QPushButton(self.widget1)
        self.speedcreateButton.setObjectName(_fromUtf8("speedcreateButton"))
        self.verticalLayout.addWidget(self.speedcreateButton)
        self.marklowButton = QtGui.QPushButton(self.widget1)
        self.marklowButton.setObjectName(_fromUtf8("marklowButton"))
        self.verticalLayout.addWidget(self.marklowButton)
        self.markhighButton = QtGui.QPushButton(self.widget1)
        self.markhighButton.setObjectName(_fromUtf8("markhighButton"))
        self.verticalLayout.addWidget(self.markhighButton)
        self.markpointButton = QtGui.QPushButton(self.widget1)
        self.markpointButton.setObjectName(_fromUtf8("markpointButton"))
        self.verticalLayout.addWidget(self.markpointButton)
        self.saveButton = QtGui.QPushButton(self.widget1)
        self.saveButton.setObjectName(_fromUtf8("saveButton"))
        self.verticalLayout.addWidget(self.saveButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1446, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.saveButton.clicked.connect(self.save)
        self.intialButton.clicked.connect(self.intial)
        self.marklowButton.clicked.connect(self.marklow)
        self.markhighButton.clicked.connect(self.markhigh)
        self.markpointButton.clicked.connect(self.markpoint)
        self.speedcreateButton.clicked.connect(self.speedcreate)
        self.tableView_set()#初始化表格
        self.tableView1_set()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "初始轨迹", None))
        self.label_3.setText(_translate("MainWindow", "LowV:", None))
        self.label_4.setText(_translate("MainWindow", "HighV:", None))
        self.label_5.setText(_translate("MainWindow", "Num:", None))
        self.label_7.setText(_translate("MainWindow", "Num2:", None))
        self.label_8.setText(_translate("MainWindow", "Num1:", None))
        self.intialButton.setText(_translate("MainWindow", "Intial", None))
        self.speedcreateButton.setText(_translate("MainWindow", "SpeedCreate", None))
        self.marklowButton.setText(_translate("MainWindow", "MarkLow", None))
        self.markhighButton.setText(_translate("MainWindow", "MarkHigh", None))
        self.markpointButton.setText(_translate("MainWindow", "MarkPoint", None))
        self.saveButton.setText(_translate("MainWindow", "SavePra", None))

        self.LowV_lineEdit.setText(_translate("MainWindow", "10000", None))
        self.HighV_lineEdit.setText(_translate("MainWindow", "13000", None))
        self.ShowNum1_lineEdit.setText(_translate("MainWindow", "0", None))
        self.ShowNum2_lineEdit.setText(_translate("MainWindow", "10", None))
        self.MarkNum_lineEdit.setText(_translate("MainWindow", "0", None))
        

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
        self.model1.setHeaderData(3,QtCore.Qt.Horizontal,_fromUtf8(u"Speed"))
        
        
        self.tableView_ShowPoint.setModel(self.model1)  
        #设置列宽  
        self.tableView_ShowPoint.setColumnWidth(0,50)  
        self.tableView_ShowPoint.setColumnWidth(1,100)  
        self.tableView_ShowPoint.setColumnWidth(2,100)
        self.tableView_ShowPoint.setColumnWidth(3,100)

        #表头信息显示居中  
        self.tableView_ShowPoint.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignCenter)


    def tableView_set(self):  
          
        #添加表头：  
        self.model = QtGui.QStandardItemModel(self.tableView)  
  
        #设置表格属性：  
        self.model.setRowCount(17)    
        self.model.setColumnCount(8)   
          
        #设置表头  
        self.model.setHeaderData(0,QtCore.Qt.Horizontal,_fromUtf8(u"BeginNum"))  
        self.model.setHeaderData(1,QtCore.Qt.Horizontal,_fromUtf8(u"EndNum"))  
        self.model.setHeaderData(2,QtCore.Qt.Horizontal,_fromUtf8(u"vinitial"))  
        self.model.setHeaderData(3,QtCore.Qt.Horizontal,_fromUtf8(u"vconstant"))
        self.model.setHeaderData(4,QtCore.Qt.Horizontal,_fromUtf8(u"vfinal"))
        self.model.setHeaderData(5,QtCore.Qt.Horizontal,_fromUtf8(u"tacc"))
        self.model.setHeaderData(6,QtCore.Qt.Horizontal,_fromUtf8(u"tconst"))
        self.model.setHeaderData(7,QtCore.Qt.Horizontal,_fromUtf8(u"tdec"))


        lineNum=0
        with open('speedpar.txt', 'r') as file_to_read:
            while True:
                lines = file_to_read.readline() # 整行读取数据
                if not lines:
                    break
                    pass
                a_tmp,b_tmp,c_tmp,d_tmp,e_tmp,f_tmp,g_tmp,h_tmp = [str(i) for i in lines.split()]
                self.model.setItem(lineNum, 0,QtGui.QStandardItem(_fromUtf8(a_tmp)))
                self.model.setItem(lineNum, 1,QtGui.QStandardItem(_fromUtf8(b_tmp)))
                self.model.setItem(lineNum, 2,QtGui.QStandardItem(_fromUtf8(c_tmp)))
                self.model.setItem(lineNum, 3,QtGui.QStandardItem(_fromUtf8(d_tmp)))
                self.model.setItem(lineNum, 4,QtGui.QStandardItem(_fromUtf8(e_tmp)))
                self.model.setItem(lineNum, 5,QtGui.QStandardItem(_fromUtf8(f_tmp)))
                self.model.setItem(lineNum, 6,QtGui.QStandardItem(_fromUtf8(g_tmp)))
                self.model.setItem(lineNum, 7,QtGui.QStandardItem(_fromUtf8(h_tmp)))
                lineNum=lineNum+1
                pass           
            pass
      
        
        self.tableView.setModel(self.model)  
        #设置列宽  
        self.tableView.setColumnWidth(0,100)  
        self.tableView.setColumnWidth(1,100)  
        self.tableView.setColumnWidth(2,100)
        self.tableView.setColumnWidth(3,100)
        self.tableView.setColumnWidth(4,100)  
        self.tableView.setColumnWidth(5,100)  
        self.tableView.setColumnWidth(6,100)
        self.tableView.setColumnWidth(7,100)

        #表头信息显示居中  
        self.tableView.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignCenter)

    def save(self):
            
        fileObject = open('speedpar.txt', 'w')
        for im in range(0,17):
            a=self.model.data(self.model.index(im,0)).toPyObject()
            b=self.model.data(self.model.index(im,1)).toPyObject()
            c=self.model.data(self.model.index(im,2)).toPyObject()
            d=self.model.data(self.model.index(im,3)).toPyObject()
            e=self.model.data(self.model.index(im,4)).toPyObject()
            f=self.model.data(self.model.index(im,5)).toPyObject()
            g=self.model.data(self.model.index(im,6)).toPyObject()
            h=self.model.data(self.model.index(im,7)).toPyObject()
            if(a<>None and b<>None and c<>None and d<>None and e<>None and f<>None and g<>None and h<>None and
               a<>'' and b<>'' and c<>'' and d<>'' and e<>'' and f<>'' and g<>'' and h<>''):
                fileObject.write(str(a)+' '+str(b)+' '+str(c)+' '+str(d)+' '+str(e)+' '+str(f)+' '+str(g)+' '+str(h))
                fileObject.write('\n')
            else:
                break
        fileObject.close()



    def intial(self):
        X=[]
        Y=[]
        #lineNum=0
        CutPoint=[]
        with open('SmoothPoint.txt', 'r') as file_to_read:
            while True:
                lines = file_to_read.readline() # 整行读取数据
                if not lines:
                    break
                    pass
                a_tmp,b_tmp,c_tmp,d_tmp = [str(i) for i in lines.split()]
                X.append(eval(b_tmp))
                Y.append(eval(c_tmp))
                
              #  lineNum=lineNum+1
                pass           
            pass
        self.startPlot3(X,Y)


    def markpoint(self):

        markpoint=int(self.MarkNum_lineEdit.text())

        X=[]
        Y=[]
        XMark=[]
        YMark=[]
        with open('SmoothPoint.txt', 'r') as file_to_read:
            while True:
                lines = file_to_read.readline() # 整行读取数据
                if not lines:
                    break
                    pass
                a_tmp,b_tmp,c_tmp,d_tmp = [str(i) for i in lines.split()]
                if(int(a_tmp)==markpoint):
                    XMark.append(eval(b_tmp))
                    YMark.append(eval(c_tmp))
                X.append(eval(b_tmp))
                Y.append(eval(c_tmp))
                
                pass           
            pass

       
        self.startPlot5(X,Y,XMark,YMark,markpoint)
        
    def marklow(self):

        X=[]
        Y=[]
        #lineNum=0
        CutPoint=[]
        with open('SmoothPoint.txt', 'r') as file_to_read:
            while True:
                lines = file_to_read.readline() # 整行读取数据
                if not lines:
                    break
                    pass
                a_tmp,b_tmp,c_tmp,d_tmp = [str(i) for i in lines.split()]
                X.append(eval(b_tmp))
                Y.append(eval(c_tmp))
                
              #  lineNum=lineNum+1
                pass           
            pass

        marklow=int(self.LowV_lineEdit.text())
        XM=[]
        YM=[]
        XY=[]
        Collect=[]
        #Num=0
        mark=1
        marknum=0
        CutPoint=[]
        with open('SpeedPoint.txt', 'r') as file_to_read:
            while True:
                lines = file_to_read.readline() # 整行读取数据
                if not lines:
                    if(mark==1):
                        XY=[XM,YM]
                        Collect.append(XY)
                    break
                    pass
                a_tmp,b_tmp,c_tmp,d_tmp,e_tmp,f_tmp = [str(i) for i in lines.split()]
                if(eval(d_tmp)>marklow):
                    if(mark==1):
                        XY=[XM,YM]
                        Collect.append(XY)
                    mark=0
                    XM=[]
                    YM=[]
                    XY=[]
                if(eval(d_tmp)<=marklow):
                    mark=1
                    XM.append(eval(b_tmp))
                    YM.append(eval(c_tmp))
                    
                
              #  lineNum=lineNum+1
                pass           
            pass
        #print(Collect)
        self.startPlot4(X,Y,Collect)


    def markhigh(self):

        X=[]
        Y=[]
        #lineNum=0
        CutPoint=[]
        with open('SmoothPoint.txt', 'r') as file_to_read:
            while True:
                lines = file_to_read.readline() # 整行读取数据
                if not lines:
                    break
                    pass
                a_tmp,b_tmp,c_tmp,d_tmp = [str(i) for i in lines.split()]
                X.append(eval(b_tmp))
                Y.append(eval(c_tmp))
                
              #  lineNum=lineNum+1
                pass           
            pass

        markhigh=int(self.HighV_lineEdit.text())
        XM=[]
        YM=[]
        XY=[]
        Collect=[]
        #Num=0
        mark=1
        marknum=0
        CutPoint=[]
        with open('SpeedPoint.txt', 'r') as file_to_read:
            while True:
                lines = file_to_read.readline() # 整行读取数据
                if not lines:
                    if(mark==1):
                        XY=[XM,YM]
                        Collect.append(XY)
                    break
                    pass
                a_tmp,b_tmp,c_tmp,d_tmp,e_tmp,f_tmp = [str(i) for i in lines.split()]
                if(eval(d_tmp)<markhigh):
                    if(mark==1):
                        XY=[XM,YM]
                        Collect.append(XY)
                    mark=0
                    XM=[]
                    YM=[]
                    XY=[]
                if(eval(d_tmp)>=markhigh):
                    mark=1
                    XM.append(eval(b_tmp))
                    YM.append(eval(c_tmp))
                    
                
              #  lineNum=lineNum+1
                pass           
            pass
        #print(Collect)
        self.startPlot4(X,Y,Collect)
       


    
    def speedcreate(self):

        CircleOffset=-1800
        
        X=[]
        Y=[]
        A=[]
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
        Fvec=[]
        T=[]
        Vbra=[]
        Vl=[]
        Fz=[]
        for iv in range(0,len(X)):
            Fvec.append(0)
            T.append(0)
            Vbra.append(0)
            Vl.append(0)
            Fz.append(0)


        tnow=0
        Fvec[0]=[1000]
        for im in range(0,17):
            a=self.model.data(self.model.index(im,0)).toPyObject()
            b=self.model.data(self.model.index(im,1)).toPyObject()
            c=self.model.data(self.model.index(im,2)).toPyObject()
            d=self.model.data(self.model.index(im,3)).toPyObject()
            e=self.model.data(self.model.index(im,4)).toPyObject()
            f=self.model.data(self.model.index(im,5)).toPyObject()
            g=self.model.data(self.model.index(im,6)).toPyObject()
            h=self.model.data(self.model.index(im,7)).toPyObject()
            
            
            if(a<>None and b<>None and c<>None and d<>None and e<>None and f<>None and g<>None and h<>None and
               a<>'' and b<>'' and c<>'' and d<>'' and e<>'' and f<>'' and g<>'' and h<>''):
                
                tbegin=tnow
                vbegin=eval(str(c))                 #初始速度mm/min
                conspeed=eval(str(d))              #目标速度mm/min
                vfinal=eval(str(e))

                tacc=eval(str(f))                   #加速时间s
                tdec=eval(str(h))
                tconsp=eval(str(g))
                vdiff1=conspeed-vbegin      #计算加速度单位mm/min²
                a1=vdiff1/tacc*60


                vdiff2=vfinal-conspeed      #计算减速度单位mm/min²
                a2=vdiff2/tdec*60

                vnow = vbegin
                for iz in range(int(a),int(b)):
                    xdifz = X[iz+1] - X[iz]
                    ydifz = Y[iz+1] - Y[iz]
                    xdifz2 = xdifz*xdifz
                    ydifz2 = ydifz*ydifz
                    xydifz=math.sqrt(xdifz2+ydifz2)

                    xdifc = X[iz+1]
                    ydifc = Y[iz+1] - CircleOffset
                    xdifc2 = xdifc*xdifc
                    ydifc2 = ydifc*ydifc 
                    xydifc=math.sqrt(xdifc2+ydifc2)

                    vec1 = xdifz*xdifc/xydifz/xydifc
                    vec2 = ydifz*ydifc/xydifz/xydifc
                    vec = vec1+vec2


                    T[iz]=tnow
                    if (tnow<=(tbegin+tacc)): 
                        xydifz2=xydifz*2
                        xydifz2a=xydifz2*a1
                        vnow2=vnow*vnow
                        vnowtemp=math.sqrt(vnow2+xydifz2a)
                        tnow=tnow+(vnowtemp-vnow)/a1*60
        
                    if (tnow>(tbegin+tacc) and tnow<=(tbegin+tacc+tconsp)):
                        tdiff=xydifz/conspeed*60
                        tnow=tnow+tdiff
                        vnowtemp=conspeed

                    if(tnow>(tbegin+tacc+tconsp) and tnow<=(tbegin+tacc+tconsp+tdec)):
                        xydifz2=xydifz*2
                        xydifz2adec=xydifz2*a2
                        vnow2=vnow*vnow
                        if(vnow2+xydifz2adec>0):
                            vnowtemp=math.sqrt(vnow2+xydifz2adec)
                            tnow=tnow+(vnowtemp - vnow)/a2*60
                        if(vnow2+xydifz2adec<=0):
                            vnowtemp=vfinal
                            tnow=tnow+(vnowtemp - vnow)/a2*60
                    if(tnow>(tbegin+tacc+tconsp+tdec)):
                        vnowtemp=vfinal
                        tdiff=xydifz/vnowtemp*60
                        tnow=tnow+tdiff
                    Fvec[iz]=vnow
                    Vbra[iz]=vnow*vec

                    vnow=vnowtemp
            else:
                break

        ###########################################

        Fvec[len(X)-1]=vnow
        T[len(X)-1]=tnow
        Vbra[len(X)-1]=vnow*vec


        ######################
        vl1begin=8000
        vl2=15660
        vl1now=vl1begin
        for ib in range(0,len(X)-1):
            vbardif = Vbra[ib+1] - Vbra[ib]
            vdiff=vl1begin*vbardif/(vl2)
            Vl[ib]=vl1now
            vl1now = vl1now + vdiff

    
        Vl[len(X)-1]=vl1now

        ######################
        for ib in range(0,len(X)):
            Fz[ib] = Vl[ib]/15660*50


        ######################
        self.startPlot1(X,Y,Fvec)
        self.startPlot2(T,Fz)
        
        fileObject = open('SpeedPoint.txt', 'w')
        for i in range(0,len(X)):
            fileObject.write(str(i)+' '+str(X[i])+' '+str(Y[i])+' '+str(Fvec[i])+' '+str(T[i])+' '+str(Fz[i]))
            fileObject.write('\n')
               
        fileObject.close()


        fileObject = open('G-Point.txt', 'w')
        for key in range(0,len(X)):  
            fileObject.write('G01 X'+str(X[key])+' Y'+str(Y[key])+' F'+str(Fvec[key])+' A'+str(A[key]))
            fileObject.write('\n')

        fileObject.close()


        
        ShowNum1=int(self.ShowNum1_lineEdit.text())
        ShowNum2=int(self.ShowNum2_lineEdit.text())

        self.model1.setRowCount(ShowNum2-ShowNum1+1)
        lineNum=0
        with open('SpeedPoint.txt', 'r') as file_to_read:
            while True:
                lines = file_to_read.readline() # 整行读取数据
                if not lines:
                    break
                    pass
                a_tmp,b_tmp,c_tmp,d_tmp,e_tmp,f_tmp = [str(i) for i in lines.split()]
                if(int(a_tmp)>=ShowNum1 and int(a_tmp)<=ShowNum2):
                    self.model1.setItem(lineNum, 0,QtGui.QStandardItem(_fromUtf8(a_tmp)))
                    self.model1.setItem(lineNum, 1,QtGui.QStandardItem(_fromUtf8(b_tmp)))
                    self.model1.setItem(lineNum, 2,QtGui.QStandardItem(_fromUtf8(c_tmp)))
                    self.model1.setItem(lineNum, 3,QtGui.QStandardItem(_fromUtf8(d_tmp)))
                    lineNum=lineNum+1
                pass           
            pass

class Code_MainWindow(Ui_MainWindow):
    def __init__(self, parent = None):
        super(Code_MainWindow, self).__init__(parent)
        self.setupUi(self)


    def startPlot1(self,x,y,z):
        ''' begin to plot'''
        self.widget.startPlot1(x,y,z)
        pass
    def startPlot2(self,x,y):
        ''' begin to plot'''
        self.widget_3.startPlot1(x,y)
        pass

    def startPlot3(self,x,y):
        ''' begin to plot'''
        self.widget_2.startPlot1(x,y)
        pass
    def startPlot4(self,x,y,xy):
        ''' begin to plot'''
        self.widget_2.startPlot2(x,y,xy)
        pass
    def startPlot5(self,x,y,markx,marky,num):
        ''' begin to plot'''
        self.widget_2.startPlot3(x,y,markx,marky,num)
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
