#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 14:19:39 2021

@author: lolo
"""

#%%


from numpy import *
# import matplotlib.pyplot as plt


write_files=False

#T      = int(504)   #   2*3*3*7*4
#T      = int(48)   #   3*4*4
T      = int(120)   #   4*4*3*10


xx     = arange(0,T)
A      = (2**12-1)
scos   = cos((xx+0.5)*2*pi/T)  *A
scos2  = cos((xx+0.5)*2*pi/T*2)*A
scos3  = cos((xx+0.5)*2*pi/T*3)*A
scos4  = cos((xx+0.5)*2*pi/T*4)*A
ssin   = sin((xx+0.5)*2*pi/T)  *A

#%%

#y1 = scos.round().astype(int)
#y2 = scos2.round().astype(int)
#y3 = scos3.round().astype(int)
#y4 = scos4.round().astype(int)
#
#
#disp(sum(y1))
#disp(sum(y2))
#disp(sum(y3))
#
#print('')
#disp(sum(y1*y2))
#disp(sum(y1*y3))
#disp(sum(y1*y4))
#disp(sum(y2*y3))
#disp(sum(y2*y4))
#disp(sum(y3*y4))


#%%

write_files = True


files = ['data_sin1.dat']+[ 'data_cos{}.dat'.format(ii) for ii in range(1,5) ]
datas = [ssin,scos,scos2,scos3,scos4]
dlims = [1,1,2,3,4]


for dat,fn,dlim in zip(datas, files, dlims):
    tmp=dat[0:T//dlim//4].astype(uint16)
    # plt.plot(tmp,'.-')
    if write_files:
        with open(fn, 'w') as content_file:
            tmp2=[]
            for i in tmp:
                tmp2.append('{0:016b}'.format(i)[-14:])
            content_file.write('\n'.join(tmp2))
