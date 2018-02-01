# -*- coding: utf-8 -*-
from PyQt4 import  QtGui
import pymssql
from matplotlib.backends.backend_qt4agg import  FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
import numpy as np
import matplotlib.dates as mdates
from matplotlib.figure import Figure
import time
import datetime
from matplotlib.dates import date2num,MinuteLocator, SecondLocator,DateFormatter,DayLocator,HourLocator
from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt




font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)

class MplCanvas(FigureCanvas):
    def __init__(self):
        self.fig = Figure()
        self.ax = self.fig.add_subplot(111)
        FigureCanvas.__init__(self, self.fig)
        FigureCanvas.setSizePolicy(self, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        self.ax.set_xlabel("time of data generator")
        self.ax.set_ylabel('random data value')
        """self.ax.legend()"""
        self.ax.xaxis.set_major_locator(MinuteLocator())  # every minute is a major locator
        self.ax.xaxis.set_minor_locator(SecondLocator([10,20,30,40,50])) # every 10 second is a minor locator
        self.ax.xaxis.set_major_formatter( DateFormatter('%H:%M:%S') ) #tick label formatter
        self.ax.format_xdata = mdates.DateFormatter('%H:%M:%S')

    def plot1(self,datax,datay1,datay2,datay3,time1,time2):
        self.ax.clear()
        self.ax.set_title(u'蒸汽压力',fontproperties=font)
        self.ax.set_ylabel('value')
        self.ax.xaxis.set_major_formatter( DateFormatter('%H:%M:%S') ) #tick label formatter
        self.ax.format_xdata = mdates.DateFormatter('%H:%M:%S')
        self.ax.set_xlim( time1, time2 )
        self.ax.set_ylim( 0, 5 )
        labels1 =self.ax.get_xticklabels()
        plt.setp(labels1,rotation=30,fontsize=10)
        self.ax.plot(datax,datay1,label='1#')
        self.ax.plot(datax,datay2,label='2#')
        self.ax.plot(datax,datay3,label='3#')
        self.ax.legend(shadow=True, fancybox=True)
        self.fig.autofmt_xdate()
        self.draw()
    def plot2(self,datax,datay1,datay2,datay3,time1,time2):
        self.ax.clear()
        self.ax.set_title(u'锅内温度',fontproperties=font)
        self.ax.set_ylabel('value')
        self.ax.xaxis.set_major_formatter( DateFormatter('%H:%M:%S') ) #tick label formatter
        self.ax.format_xdata = mdates.DateFormatter('%H:%M:%S')
        self.ax.set_xlim( time1, time2 )
        self.ax.set_ylim( 0, 100 )
        labels1 =self.ax.get_xticklabels()
        plt.setp(labels1,rotation=30,fontsize=10)
        self.ax.plot(datax,datay1,label='1#')
        self.ax.plot(datax,datay2,label='2#')
        self.ax.plot(datax,datay3,label='3#')
        self.ax.legend(shadow=True, fancybox=True)
        self.fig.autofmt_xdate()
        self.draw()
    def plot3(self,datax,datay1,datay2,datay3,time1,time2):
        self.ax.clear()
        self.ax.set_title(u'出酒温度',fontproperties=font)
        self.ax.set_ylabel('value')
        self.ax.xaxis.set_major_formatter( DateFormatter('%H:%M:%S') ) #tick label formatter
        self.ax.format_xdata = mdates.DateFormatter('%H:%M:%S')
        self.ax.set_xlim( time1, time2 )
        self.ax.set_ylim( 0, 70 )
        labels1 =self.ax.get_xticklabels()
        plt.setp(labels1,rotation=30,fontsize=10)
        self.ax.plot(datax,datay1,label='1#')
        self.ax.plot(datax,datay2,label='2#')
        self.ax.plot(datax,datay3,label='3#')
        self.ax.legend(shadow=True, fancybox=True)
        self.fig.autofmt_xdate()
        self.draw()
    def plot4(self,datax,datay1,datay2,time1,time2):
        self.ax.clear()
        self.ax.set_title(u'摊粮温度',fontproperties=font)
        self.ax.set_ylabel('value')
        self.ax.xaxis.set_major_formatter( DateFormatter('%H:%M:%S') ) #tick label formatter
        self.ax.format_xdata = mdates.DateFormatter('%H:%M:%S')
        self.ax.set_xlim( time1, time2 )
        self.ax.set_ylim( -15, 70 )
        labels1 =self.ax.get_xticklabels()
        plt.setp(labels1,rotation=30,fontsize=10)
        self.ax.plot(datax,datay1,label='1#')
        self.ax.plot(datax,datay2,label='2#')
        self.ax.legend(shadow=True, fancybox=True)
        self.fig.autofmt_xdate()
        self.draw()
            
class MSSQL:
    def __init__(self,host,user,pwd,db):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db
 
    def __GetConnect(self):
        """
        得到连接信息
        返回: conn.cursor()
        """
        if not self.db:
            raise(NameError,"没有设置数据库信息")
        self.conn = pymssql.connect(host=self.host,user=self.user,password=self.pwd,database=self.db,charset="utf8")
        cur = self.conn.cursor()
        if not cur:
            raise(NameError,"连接数据库失败")
        else:
            return cur
 
    def ExecQuery(self,sql):
        """
        执行查询语句
        返回的是一个包含tuple的list，list的元素是记录行，tuple的元素是每行记录的字段
 
        调用示例：
                ms = MSSQL(host="localhost",user="sa",pwd="123456",db="PythonWeiboStatistics")
                resList = ms.ExecQuery("SELECT id,NickName FROM WeiBoUser")
                for (id,NickName) in resList:
                    print str(id),NickName
        """
        cur = self.__GetConnect()
        cur.execute(sql)
        resList = cur.fetchall()
 
        #查询完毕后必须关闭连接
        self.conn.close()
        return resList


    def ExecNonQuery(self,sql):
        """
        执行非查询语句
 
        调用示例：
            cur = self.__GetConnect()
            cur.execute(sql)
            self.conn.commit()
            self.conn.close()
        """
        cur = self.__GetConnect()
        cur.execute(sql)
        self.conn.commit()
        self.conn.close()


class  mplCanvasWrapper1(QtGui.QWidget):
   
    def __init__(self , parent =None):
        QtGui.QWidget.__init__(self, parent)
        self.canvas = MplCanvas()
        self.vbl = QtGui.QVBoxLayout()
        self.ntb = NavigationToolbar(self.canvas, parent)
        self.vbl.addWidget(self.ntb)
        self.vbl.addWidget(self.canvas)
        self.setLayout(self.vbl)
        self.dataY1= []
        self.dataY2= []
        self.dataY3= []
        self.dataX= []




        
    def releasePlot(self):
         self.__exit  = True


    def startPlot1(self,begintime,overtime):
        
        ms = MSSQL(host="localhost",user="sa",pwd="sa",db="DataSet")
        k1="SELECT ItemValue,ItemType,CurrentTime FROM ItemTimeHistory where ItemName ='1#蒸汽压力'and CurrentTime  between '"+begintime.strftime('%Y-%m-%d %H:%M:%S')+"'and '"+overtime.strftime('%Y-%m-%d %H:%M:%S')+"' order by CurrentTime"
        k2="SELECT ItemValue,ItemType,CurrentTime FROM ItemTimeHistory where ItemName ='2#蒸汽压力'and CurrentTime  between '"+begintime.strftime('%Y-%m-%d %H:%M:%S')+"'and '"+overtime.strftime('%Y-%m-%d %H:%M:%S')+"' order by CurrentTime"
        k3="SELECT ItemValue,ItemType,CurrentTime FROM ItemTimeHistory where ItemName ='3#蒸汽压力'and CurrentTime  between '"+begintime.strftime('%Y-%m-%d %H:%M:%S')+"'and '"+overtime.strftime('%Y-%m-%d %H:%M:%S')+"' order by CurrentTime"
        resList1 = ms.ExecQuery(k1)
        resList2 = ms.ExecQuery(k2)
        resList3 = ms.ExecQuery(k3)
        m1=[float(a)for (a,b,c) in resList1]
        m2=[float(a)for (a,b,c) in resList2]
        m3=[float(a)for (a,b,c) in resList3]
        l=[c for (a,b,c) in resList1]
        self.dataX=l
        self.dataY1=m1
        self.dataY2=m2
        self.dataY3=m3
        time1=begintime
        time2=overtime
        self.canvas.plot1(self.dataX,self.dataY1,self.dataY2,self.dataY3,begintime,overtime)


        
class  mplCanvasWrapper2(QtGui.QWidget):
   
    def __init__(self , parent =None):
        QtGui.QWidget.__init__(self, parent)
        self.canvas = MplCanvas()
        self.vbl = QtGui.QVBoxLayout()
        self.ntb = NavigationToolbar(self.canvas, parent)
        self.vbl.addWidget(self.ntb)
        self.vbl.addWidget(self.canvas)
        self.setLayout(self.vbl)
        self.dataY1= []
        self.dataY2= []
        self.dataY3= []
        self.dataX= []



        
    def releasePlot(self):
         self.__exit  = True


    def startPlot1(self,begintime,overtime):
        ms = MSSQL(host="localhost",user="sa",pwd="sa",db="DataSet")
        k1="SELECT ItemValue,ItemType,CurrentTime FROM ItemTimeHistory where ItemName ='1#锅内温度'and CurrentTime  between '"+begintime.strftime('%Y-%m-%d %H:%M:%S')+"'and '"+overtime.strftime('%Y-%m-%d %H:%M:%S')+"' order by CurrentTime"
        k2="SELECT ItemValue,ItemType,CurrentTime FROM ItemTimeHistory where ItemName ='2#锅内温度'and CurrentTime  between '"+begintime.strftime('%Y-%m-%d %H:%M:%S')+"'and '"+overtime.strftime('%Y-%m-%d %H:%M:%S')+"' order by CurrentTime"
        k3="SELECT ItemValue,ItemType,CurrentTime FROM ItemTimeHistory where ItemName ='3#锅内温度'and CurrentTime  between '"+begintime.strftime('%Y-%m-%d %H:%M:%S')+"'and '"+overtime.strftime('%Y-%m-%d %H:%M:%S')+"' order by CurrentTime"
        resList4 = ms.ExecQuery(k1)
        resList5 = ms.ExecQuery(k2)
        resList6 = ms.ExecQuery(k3)
        m1=[float(a)for (a,b,c) in resList4]
        m2=[float(a)for (a,b,c) in resList5]
        m3=[float(a)for (a,b,c) in resList6]
        l=[c for (a,b,c) in resList4]
        self.dataX=l
        self.dataY1=m1
        self.dataY2=m2
        self.dataY3=m3
        time1=begintime
        time2=overtime
        self.canvas.plot2(self.dataX,self.dataY1,self.dataY2,self.dataY3,begintime,overtime)


        
class  mplCanvasWrapper3(QtGui.QWidget):
   
    def __init__(self , parent =None):
        QtGui.QWidget.__init__(self, parent)
        self.canvas = MplCanvas()
        self.vbl = QtGui.QVBoxLayout()
        self.ntb = NavigationToolbar(self.canvas, parent)
        self.vbl.addWidget(self.ntb)
        self.vbl.addWidget(self.canvas)
        self.setLayout(self.vbl)
        self.dataY1= []
        self.dataY2= []
        self.dataY3= []
        self.dataX= []



        
    def releasePlot(self):
         self.__exit  = True


    def startPlot1(self,begintime,overtime):
        
        ms = MSSQL(host="localhost",user="sa",pwd="sa",db="DataSet")
        k1="SELECT ItemValue,ItemType,CurrentTime FROM ItemTimeHistory where ItemName ='1#出酒温度'and CurrentTime  between '"+begintime.strftime('%Y-%m-%d %H:%M:%S')+"'and '"+overtime.strftime('%Y-%m-%d %H:%M:%S')+"' order by CurrentTime"
        k2="SELECT ItemValue,ItemType,CurrentTime FROM ItemTimeHistory where ItemName ='2#出酒温度'and CurrentTime  between '"+begintime.strftime('%Y-%m-%d %H:%M:%S')+"'and '"+overtime.strftime('%Y-%m-%d %H:%M:%S')+"' order by CurrentTime"
        k3="SELECT ItemValue,ItemType,CurrentTime FROM ItemTimeHistory where ItemName ='3#出酒温度'and CurrentTime  between '"+begintime.strftime('%Y-%m-%d %H:%M:%S')+"'and '"+overtime.strftime('%Y-%m-%d %H:%M:%S')+"' order by CurrentTime"
        resList1 = ms.ExecQuery(k1)
        resList2 = ms.ExecQuery(k2)
        resList3 = ms.ExecQuery(k3)
        m1=[float(a)for (a,b,c) in resList1]
        m2=[float(a)for (a,b,c) in resList2]
        m3=[float(a)for (a,b,c) in resList3]
        l=[c for (a,b,c) in resList1]
        self.dataX=l
        self.dataY1=m1
        self.dataY2=m2
        self.dataY3=m3
        time1=begintime
        time2=overtime
        self.canvas.plot3(self.dataX,self.dataY1,self.dataY2,self.dataY3,begintime,overtime)





        
class  mplCanvasWrapper4(QtGui.QWidget):
   
    def __init__(self , parent =None):
        QtGui.QWidget.__init__(self, parent)
        self.canvas = MplCanvas()
        self.vbl = QtGui.QVBoxLayout()
        self.ntb = NavigationToolbar(self.canvas, parent)
        self.vbl.addWidget(self.ntb)
        self.vbl.addWidget(self.canvas)
        self.setLayout(self.vbl)
        self.dataY1= []
        self.dataY2= []
        self.dataX= []



        
    def releasePlot(self):
         self.__exit  = True


    def startPlot1(self,begintime,overtime):
        
        ms = MSSQL(host="localhost",user="sa",pwd="sa",db="DataSet")
        k1="SELECT ItemValue,ItemType,CurrentTime FROM ItemTimeHistory where ItemName ='摊粮前温度'and CurrentTime  between '"+begintime.strftime('%Y-%m-%d %H:%M:%S')+"'and '"+overtime.strftime('%Y-%m-%d %H:%M:%S')+"' order by CurrentTime"
        k2="SELECT ItemValue,ItemType,CurrentTime FROM ItemTimeHistory where ItemName ='摊粮后温度'and CurrentTime  between '"+begintime.strftime('%Y-%m-%d %H:%M:%S')+"'and '"+overtime.strftime('%Y-%m-%d %H:%M:%S')+"' order by CurrentTime"
        resList1 = ms.ExecQuery(k1)
        resList2 = ms.ExecQuery(k2)
        m1=[float(a)for (a,b,c) in resList1]
        m2=[float(a)for (a,b,c) in resList2]
        l=[c for (a,b,c) in resList1]
        self.dataX=l
        self.dataY1=m1
        self.dataY2=m2
        time1=begintime
        time2=overtime
        self.canvas.plot4(self.dataX,self.dataY1,self.dataY2,begintime,overtime)
