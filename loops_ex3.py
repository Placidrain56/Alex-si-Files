# -*- coding: utf-8 -*-
"""
Created on Fri May 24 10:21:50 2019

@author: Alex&Liana
"""

myvect1 = ['a','b','c','d'] #this is called a list
myvect2 = [1 , 2 , 3, 56]



for item1, item2 in zip(myvect1, myvect2): #will only work for the shortest list
    
    print('item1 = '+str(item1))
    print('item2 = ' +str(item2))
    

print('this is the end of the loop')