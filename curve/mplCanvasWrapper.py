# -*- coding: utf-8 -*-
from PyQt4 import  QtGui
import pymssql
from matplotlib.backends.backend_qt4agg import  FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
import numpy as np
import matplotlib.dates as mdates
from matplotlib.figure import Figure
import threading
import time
import datetime
from matplotlib.dates import date2num,MinuteLocator, SecondLocator,DateFormatter
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)
X_MINUTES = 10
INTERVAL = 2
Y_MAX1 = 5
Y_MIN1 = 0
Y_MAX2 = 50
Y_MIN2 = 0
Y_MAX3 = 50
Y_MIN3 = -10
Y_MAX4 = 100
Y_MIN4 = 0
MAXCOUNTER = int(X_MINUTES * 60/ INTERVAL)
class MplCanvas(FigureCanvas):
    def __init__(self):
        self.fig = Figure(facecolor="white")
        self.ax1 = self.fig.add_subplot(221)
        self.ax2 = self.fig.add_subplot(222)
        self.ax3 = self.fig.add_subplot(223)
        self.ax4 = self.fig.add_subplot(224)
        self.fig.subplots_adjust(wspace=0.3,hspace=0.3)
        """
        self.fig.autofmt_xdate()
        """
        FigureCanvas.__init__(self, self.fig)
        FigureCanvas.setSizePolicy(self, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        self.ax1.set_xlabel("time of data generator")
        self.ax1.set_ylabel('random data value')
        """self.ax.legend()
        self.ax1.xaxis.set_major_locator(MinuteLocator())  # every minute is a major locator
        self.ax1.xaxis.set_minor_locator(SecondLocator([10,20,30,40,50])) # every 10 second is a minor locator
        self.ax1.xaxis.set_major_formatter( DateFormatter('%H:%M') ) #tick label formatter
        self.ax1.format_xdata = mdates.DateFormatter('%Y-%m-%d %H:%M:%S')
        self.ax2.set_xlabel("time of data generator")
        self.ax2.set_ylabel('random data value')
        self.ax.legend()

        self.ax3.set_xlabel("time of data generator")
        self.ax3.set_ylabel('random data value')
        self.ax.legend()

        self.ax4.set_xlabel("time of data generator")
        self.ax4.set_ylabel('random data value')
        self.ax.legend()"""

    def plot1(self,datax,datay1,datay2,datay3):
        self.ax1.clear()
        self.ax1.set_title(u'蒸汽压力',fontproperties=font)
        self.ax1.set_ylabel('value')
        self.ax1.set_ylim(Y_MIN1,Y_MAX1)
        self.ax1.xaxis.set_major_locator(MinuteLocator())  # every minute is a major locator
        self.ax1.xaxis.set_minor_locator(SecondLocator([20,40])) # every 10 second is a minor locator
        self.ax1.xaxis.set_major_formatter( DateFormatter('%H:%M:%S') ) #tick label formatter
        self.ax1.format_xdata = mdates.DateFormatter('%H:%M:%S')
        labels1 =self.ax1.get_xticklabels()
        plt.setp(labels1,rotation=30,fontsize=10)
        self.ax1.plot(datax,datay1,label='1#')
        self.ax1.plot(datax,datay2,label='2#')
        self.ax1.plot(datax,datay3,label='3#')
        self.ax1.legend(shadow=True, fancybox=True)
        self.draw()
    def plot2(self,datax,datay1,datay2,datay3):
        self.ax2.clear()
        self.ax2.set_title(u'出酒温度',fontproperties=font)
        self.ax2.set_ylabel('value')
        self.ax2.set_ylim(Y_MIN2,Y_MAX2)
        self.ax2.xaxis.set_major_locator(MinuteLocator())  # every minute is a major locator
        self.ax2.xaxis.set_minor_locator(SecondLocator([20,40])) # every 10 second is a minor locator
        self.ax2.xaxis.set_major_formatter( DateFormatter('%H:%M:%S') ) #tick label formatter
        self.ax2.format_xdata = mdates.DateFormatter('%H:%M:%S')
        labels2 =self.ax2.get_xticklabels()
        plt.setp(labels2,rotation=30,fontsize=10)
        self.ax2.plot(datax,datay1,label='1#')
        self.ax2.plot(datax,datay2,label='2#')
        self.ax2.plot(datax,datay3,label='3#')
        self.ax2.legend(shadow=True, fancybox=True)
        self.draw()

        
    def plot3(self,datax,datay1,datay2):
        self.ax3.clear()
        self.ax3.set_title(u'摊粮温度',fontproperties=font)
        self.ax3.set_ylabel('value')
        self.ax3.set_ylim(Y_MIN3,Y_MAX3)
        self.ax3.xaxis.set_major_locator(MinuteLocator())  # every minute is a major locator
        self.ax3.xaxis.set_minor_locator(SecondLocator([20,40])) # every 10 second is a minor locator
        self.ax3.xaxis.set_major_formatter( DateFormatter('%H:%M:%S') ) #tick label formatter
        self.ax3.format_xdata = mdates.DateFormatter('%H:%M:%S')
        labels3 =self.ax3.get_xticklabels()
        plt.setp(labels3,rotation=30,fontsize=10)
        self.ax3.plot(datax,datay1,label='1#')
        self.ax3.plot(datax,datay2,label='2#')
        self.ax3.legend(shadow=True, fancybox=True)
        self.draw()

    def plot4(self,datax,datay1,datay2,datay3):
        self.ax4.clear()
        self.ax4.set_title(u'锅内温度',fontproperties=font)
        self.ax4.set_ylabel('value')
        self.ax4.set_ylim(Y_MIN4,Y_MAX4)
        self.ax4.xaxis.set_major_locator(MinuteLocator())  # every minute is a major locator
        self.ax4.xaxis.set_minor_locator(SecondLocator([20,40])) # every 10 second is a minor locator
        self.ax4.xaxis.set_major_formatter( DateFormatter('%H:%M:%S') ) #tick label formatter
        self.ax4.format_xdata = mdates.DateFormatter('%H:%M:%S')
        labels4 =self.ax4.get_xticklabels()
        plt.setp(labels4,rotation=30,fontsize=10)
        self.ax4.plot(datax,datay1,label='1#')
        self.ax4.plot(datax,datay2,label='2#')
        self.ax4.plot(datax,datay3,label='3#')
        self.ax4.legend(shadow=True, fancybox=True)
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
        self.dataY1=[]
        self.dataY2=[]
        self.dataY3=[]
        self.dataY4=[]
        self.dataY5=[]
        self.dataY6=[]
        self.dataY7=[]
        self.dataY8=[]
        self.dataY9=[]
        self.dataY10=[]
        self.dataY11=[]
        self.dataX=[]

        self.counter=0
        self.initDataGenerator()

        
    def releasePlot(self):
         self.__exit  = True
         self.tData.join()



    def startPlot2(self):
        self.__generating = True
            
        
    def stopPlot(self):
        self.__generating=False
        self.__generating = False
        pass
    
    
    def initDataGenerator(self):
        self.__generating=True
        self.__exit = False
       
        self.tData = threading.Thread(name = "dataGenerator",target = self.generateData)
        self.tData.start()

        
    def generateData(self):
        print "线程以启动"
        while(True):
            if self.__exit:
                break
            if self.__generating:
                ms = MSSQL(host="localhost",user="sa",pwd="sa",db="DataSet")
                k="SELECT Value,DataType,CurrentTime FROM DataItemNow where Name ='1#蒸汽压力'or Name='2#蒸汽压力'or Name ='3#蒸汽压力' or Name ='1#出酒温度'or Name='2#出酒温度'or Name ='3#出酒温度' or Name='摊粮前温度'or Name ='摊粮后温度' or Name ='1#锅内温度'or Name='2#锅内温度'or Name ='3#锅内温度'order by ID"
                resList = ms.ExecQuery(k)
                r=[float(a)for (a,b,c) in resList]
                q=len(r)
                if r!=[] and q==11:
                    print len(r)
                    l1=r[0]
                    print l1
                    l2=r[1]
                    print l2
                    l3=r[2]
                    print l3
                    l4=r[3]
                    print l4
                    l5=r[4]
                    print l5
                    l6=r[5]
                    print l6
                    l7=r[6]
                    print l7
                    l8=r[7]
                    print l8
                    l9=r[8]
                    print l9
                    l10=r[9]
                    print l10
                    l11=r[10]
                    print l11
                    o=date2num(datetime.datetime.now())
                    self.dataY1.append(l1)
                    self.dataY2.append(l2)
                    self.dataY3.append(l3)
                    self.dataY4.append(l4)
                    self.dataY5.append(l5)
                    self.dataY6.append(l6)
                    self.dataY7.append(l7)
                    self.dataY8.append(l8)
                    self.dataY9.append(l9)
                    self.dataY10.append(l10)
                    self.dataY11.append(l11)
                    self.dataX.append(o)
                    self.canvas.plot1(self.dataX,self.dataY1,self.dataY2,self.dataY3)
                    self.canvas.plot2(self.dataX,self.dataY4,self.dataY5,self.dataY6)
                    self.canvas.plot3(self.dataX,self.dataY7,self.dataY8)
                    self.canvas.plot4(self.dataX,self.dataY9,self.dataY10,self.dataY11)
                    if self.counter >= MAXCOUNTER:
                        self.dataX.pop(0)
                        self.dataY1.pop(0)
                        self.dataY2.pop(0)
                        self.dataY3.pop(0)
                        self.dataY4.pop(0)
                        self.dataY5.pop(0)
                        self.dataY6.pop(0)
                        self.dataY7.pop(0)
                        self.dataY8.pop(0)
                        self.dataY9.pop(0)
                        self.dataY10.pop(0)
                        self.dataY11.pop(0)
                        print len(self.dataX)
                    else:
                        self.counter+=1
                        print len(self.dataX)
                else:
                    o2=date2num(datetime.datetime.now())
                    self.dataY1.append(l1)
                    self.dataY2.append(l2)
                    self.dataY3.append(l3)
                    self.dataY4.append(l4)
                    self.dataY5.append(l5)
                    self.dataY6.append(l6)
                    self.dataY7.append(l7)
                    self.dataY8.append(l8)
                    self.dataY9.append(l9)
                    self.dataY10.append(l10)
                    self.dataY11.append(l11)
                    self.dataX.append(o2)
                    self.canvas.plot1(self.dataX,self.dataY1,self.dataY2,self.dataY3)
                    self.canvas.plot2(self.dataX,self.dataY4,self.dataY5,self.dataY6)
                    self.canvas.plot3(self.dataX,self.dataY7,self.dataY8)
                    self.canvas.plot4(self.dataX,self.dataY9,self.dataY10,self.dataY11)
                    print("取数据错误")
                    if self.counter >= MAXCOUNTER:
                        self.dataX.pop(0)
                        self.dataY1.pop(0)
                        self.dataY2.pop(0)
                        self.dataY3.pop(0)
                        self.dataY4.pop(0)
                        self.dataY5.pop(0)
                        self.dataY6.pop(0)
                        self.dataY7.pop(0)
                        self.dataY8.pop(0)
                        self.dataY9.pop(0)
                        self.dataY10.pop(0)
                        self.dataY11.pop(0)
                        print len(self.dataX)
                    else:
                        self.counter+=1
                        print len(self.dataX)
                time.sleep(INTERVAL)

