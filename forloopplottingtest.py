# -*- coding: utf-8 -*-
"""
Created on Fri May 31 16:32:56 2019

@author: Alex&Liana
"""

from matplotlib.pyplot import *

from numpy import *

t = arange(0,1,.01)

y = 2*sin(2*pi*t)

N = len(y)
y_min= zeros(N)

for i in range(N):
    y_i = y[i]
    if y_i < .5:
        y_min[i] = 0
    else:
        y_min[i] = y_i


figure(1)
clf()
plot(t,y,'r--')
plot(t, y_min, label='$y(t)$', linewidth=2.0)
ylabel('$y(t)$')
xlabel('Time (s)')
show()
