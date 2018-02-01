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
        canvas = FigureCanvas(self.fig)
        self.ax = self.fig.add_subplot(111,projection='3d')
        #self.ax.figure.canvas = canvas
        self.ax.mouse_init()
        FigureCanvas.__init__(self, self.fig)    
        #FigureCanvas.setSizePolicy(self, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)

        


    def plot1(self,datax,datay,dataz):
  
        self.ax.clear()
        self.ax.mouse_init()

        self.ax.set_title(u'Speed Trajectory',fontproperties=font)
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.set_zlabel('Z')
        self.ax.plot(datax,datay,dataz)
        #self.ax.legend(shadow=True, fancybox=True)
        self.draw()



class  D3Trajectory(QtGui.QWidget):
   
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


    def startPlot1(self,x,y,z):        

        self.canvas.plot1(x,y,z)
        
