# -*- coding: utf-8 -*-
"""
Created on Thu May 23 15:56:55 2019

@author: Alex&Liana
"""
from matplotlib.pyplot import *

from numpy import *

t = arange(0,1,.01)

y = 2*sin(2*pi*t)


#if y > 1.5: this is a bad idea and it doesnt work!
#    y = 1.5
#elif y < -1.5:
#    y = -1.5
#    
figure(1)
clf()
plot(t,y)
