# -*- coding: utf-8 -*-
"""
Created on Fri May 31 16:43:16 2019

@author: Alex&Liana
"""

from matplotlib.pyplot import *

from numpy import *

t = arange(0,1,.01)

y = 2*sin(2*pi*t)

import copy

y_min = copy.copy(y)

figure(1)
clf()
plot(t,y,'r--')


y_min[y_min < .5] = 0


plot(t, y_min, label='$y(t)$', linewidth=2.0)
ylabel('$y(t)$')
xlabel('Time (s)')
show()