# -*- coding: utf-8 -*-
import numpy as np
from math import pi
import math
import matplotlib.pyplot as plt



x=[]
y=[]
a='720*np.sin(i*1.9*pi/500-0.5*pi)'
b='720*np.cos(i*1.9*pi/500-0.5*pi)'
for i in range(0,490):
    x.append(eval(a))
    y.append(eval(b))

#绘出平面图像
fig2=plt.figure(2,figsize=(6,6))

plt.plot(x,y,label="$circle$",color="blue")



plt.xlabel("x(mm)")
plt.ylabel("y(mm)")
plt.title("PyPlot My Circle")

plt.legend()
plt.show()
