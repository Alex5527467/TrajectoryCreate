# -*- coding: utf-8 -*-
from PyQt4 import  QtGui
from matplotlib.backends.backend_qt4agg import  FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
import numpy as np
import matplotlib.dates as mdates
from matplotlib.figure import Figure
from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import MultipleLocator, FormatStrFormatter



font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)

class widget(FigureCanvas):
    def __init__(self):
        self.fig = Figure()
        self.ax = self.fig.add_subplot(111)
        
        FigureCanvas.__init__(self, self.fig)    
        FigureCanvas.setSizePolicy(self, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
 




    def plot1(self,datax,datay,xmark,ymark):
        self.ax.clear()
        self.ax.set_title(u'Inatial Trajectory',fontproperties=font)
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.plot(datax,datay)
        self.ax.scatter(xmark,ymark)
        #self.ax.legend(shadow=True, fancybox=True)
        self.draw()
    def plot2(self,datax,datay,xmark,ymark,cutpoint):
        self.ax.clear()
        self.ax.set_title(u'Smooth Trajectory',fontproperties=font)
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.plot(datax,datay)
        self.ax.scatter(xmark,ymark)
        for i in range(0,len(cutpoint)):
            self.ax.annotate(str(cutpoint[i]), xy=(xmark[i], ymark[i]), xytext=(xmark[i]+10, ymark[i]+10))#,arrowprops=dict(facecolor='black', shrink=0.05))
        #self.ax.legend(shadow=True, fancybox=True)
        self.draw()
    def plot3(self,datax,datay):
        self.ax.clear()
        self.ax.set_title(u'Smooth Trajectory',fontproperties=font)
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.plot(datax,datay)
        #self.ax.legend(shadow=True, fancybox=True)
        self.draw()
   
    def plot4(self,datax,datay):
        self.ax.clear()
        self.ax.set_title(u'Speed Trajectory',fontproperties=font)
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.plot(datax,datay)
        #self.ax.legend(shadow=True, fancybox=True)
        self.draw()
    def plot5(self,datax,datay):
        ##########################################################
        xmajorLocator   = MultipleLocator(5) #将x主刻度标签设置为20的倍数  
        xmajorFormatter = FormatStrFormatter('%1.1f') #设置x轴标签文本的格式
        xminorLocator   = MultipleLocator(1) #将x轴次刻度标签设置为5的倍数

        ymajorLocator   = MultipleLocator(5) #将y轴主刻度标签设置为0.5的倍数  
        ymajorFormatter = FormatStrFormatter('%1.1f') #设置y轴标签文本的格式  
        yminorLocator   = MultipleLocator(1) #将此y轴次刻度标签设置为0.1的倍数 
        self.ax.clear()
        #设置主刻度标签的位置,标签文本的格式 
        self.ax.xaxis.set_major_locator(xmajorLocator)  
        self.ax.xaxis.set_major_formatter(xmajorFormatter)
        self.ax.xaxis.set_minor_locator(xminorLocator)

        self.ax.yaxis.set_major_locator(ymajorLocator)  
        self.ax.yaxis.set_major_formatter(ymajorFormatter)
        self.ax.yaxis.set_minor_locator(yminorLocator)
        
        self.ax.set_title(u'LinearSpeed Trajectory',fontproperties=font)
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.plot(datax,datay)
        self.ax.xaxis.grid(True, which='major') #x坐标轴的网格使用主刻度  
        self.ax.yaxis.grid(True, which='major') #y坐标轴的网格使用次刻度
        #self.ax.legend(shadow=True, fancybox=True)
        self.draw()
    def plot6(self,datax,datay,dataxy):
        self.ax.clear()
        self.ax.set_title(u'Speed Trajectory',fontproperties=font)
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.plot(datax,datay)
        for xy in dataxy:
            self.ax.plot(xy[0],xy[1],color='red')
        #self.ax.legend(shadow=True, fancybox=True)
        self.draw()

    def plot7(self,datax,datay,xmark,ymark,cutpoint):
        self.ax.clear()
        self.ax.set_title(u'Speed Trajectory',fontproperties=font)
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.plot(datax,datay)
        self.ax.scatter(xmark,ymark)
        self.ax.annotate(cutpoint, xy=(xmark[0], ymark[0]), xytext=(xmark[0]+10, ymark[0]+10))
        self.draw()
    def plot8(self,datax,datay,xmark,ymark,cutx,cuty,marknum,limit):
        self.ax.clear()
        self.ax.set_xlim(limit[0],limit[1])
        self.ax.set_ylim(limit[2],limit[3])
        self.ax.set_title(u'Speed Trajectory',fontproperties=font)
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.plot(datax,datay)
        self.ax.plot(cutx,cuty,color='red')
        self.ax.scatter(xmark,ymark)
        self.ax.annotate(marknum, xy=(xmark[0], ymark[0]), xytext=(xmark[0]+10, ymark[0]+10))
        self.draw()


class  IntialTrajectory(QtGui.QWidget):
   
    def __init__(self , parent =None):
        QtGui.QWidget.__init__(self, parent)
        self.canvas = widget()
        self.vbl = QtGui.QVBoxLayout()
        self.ntb = NavigationToolbar(self.canvas, parent)
        self.vbl.addWidget(self.ntb)
        self.vbl.addWidget(self.canvas)
        self.setLayout(self.vbl)


        
    def releasePlot(self):
         self.__exit  = True


    def startPlot1(self,x,y,xmark,ymark):        

        self.canvas.plot1(x,y,xmark,ymark)

class  SmoothTrajectory(QtGui.QWidget):
   
    def __init__(self , parent =None):
        QtGui.QWidget.__init__(self, parent)
        self.canvas = widget()
        self.vbl = QtGui.QVBoxLayout()
        self.ntb = NavigationToolbar(self.canvas, parent)
        self.vbl.addWidget(self.ntb)
        self.vbl.addWidget(self.canvas)
        self.setLayout(self.vbl)


        
    def releasePlot(self):
         self.__exit  = True


    def startPlot1(self,x,y,xmark,ymark,cutpoint):        

        self.canvas.plot2(x,y,xmark,ymark,cutpoint)
        
    def startPlot2(self,x,y):        

        self.canvas.plot3(x,y)

    def startPlot3(self,x,y,xmark,ymark,xcut,ycut,marknum,limit):        

        self.canvas.plot8(x,y,xmark,ymark,xcut,ycut,marknum,limit)
        
class  SpeedTrajectory(QtGui.QWidget):
   
    def __init__(self , parent =None):
        QtGui.QWidget.__init__(self, parent)
        self.canvas = widget()
        self.vbl = QtGui.QVBoxLayout()
        self.ntb = NavigationToolbar(self.canvas, parent)
        self.vbl.addWidget(self.ntb)
        self.vbl.addWidget(self.canvas)
        self.setLayout(self.vbl)


        
    def releasePlot(self):
         self.__exit  = True


    def startPlot1(self,x,y):        

        self.canvas.plot4(x,y)
    def startPlot2(self,x,y,xy):

        self.canvas.plot6(x,y,xy)

    def startPlot3(self,x,y,xmark,ymark,num):

        self.canvas.plot7(x,y,xmark,ymark,num)
        


class  LinearSpeedTrajectory(QtGui.QWidget):
   
    def __init__(self , parent =None):
        QtGui.QWidget.__init__(self, parent)
        self.canvas = widget()
        self.vbl = QtGui.QVBoxLayout()
        self.ntb = NavigationToolbar(self.canvas, parent)
        self.vbl.addWidget(self.ntb)
        self.vbl.addWidget(self.canvas)
        self.setLayout(self.vbl)


        
    def releasePlot(self):
         self.__exit  = True


    def startPlot1(self,x,y):        

        self.canvas.plot5(x,y)


