# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 13:55:38 2020

@author: User
"""
import matplotlib.pyplot as plt
import numpy as np

def J(Midx,Midx1,y,c0,c1,c2): #оценка функции
    j=0
    m=len(x)    
    for i in range(0,m):
        j+=((c0+c1*Midx[i]+c2*Midx1[i])-y[i])**2
    j/=(2*m)
    return j

def Grad0(Midx,Midx1,y,c0,c1,c2):
    grad0=0
    m=len(x)
    for i in range (0,m):
       grad0+=((c0+c1*Midx[i]+c2*Midx1[i])-y[i])
    grad0/=m
    return grad0
def Grad1(Midx,Midx1,y,c0,c1,c2):
    grad1=0
    m=len(x)
    for i in range (0,m):
       grad1+=((c0+c1*Midx[i]+c2*Midx1[i])-y[i])*Midx[i]
    grad1/=m
    return grad1
def Grad2(Midx,Midx1,y,c0,c1,c2):
    grad2=0
    m=len(x)
    for i in range (0,m):
       grad2+=((c0+c1*Midx[i]+c2*Midx1[i])-y[i])*Midx1[i]
    grad2/=m
    return grad2

f = open('data2.txt', 'r')
x = []
x1 = []
y = []
Midx=[]
Midx1=[]
Midy=[]
temp=0
c1=1
c2=1
c0=0
al=0.01
eps=0.000000001

for line in f:
    temp = line.split(' ')
    x.append(int(temp[0]))
    x1.append(int(temp[1]))
    y.append(int(temp[2]))
m=len(x)
j=0
print x
for i in range(0,m):
    j+=((c0+c1*x[i]+c2*x1[i])-y[i])**2
j/=(2*m)
cop1=np.array(x)
print x
cop2=np.array(x1)
cop3=np.array(y)
cop1*=c1
cop2*=c2
cop3=((c0+cop1+cop2)-cop3)**2

num1=cop1.sum()
num2=cop2.sum()
num3=cop3.sum()
j6=((c0+c1*num1+c2*num2)-num3)**2
m=len(x)    
cop3/=2*m
j6/=2*m
num3=cop3.sum()
print num3
print j
print j6



Maxx=max(x)
Minx=min(x)
for i in range(0,m):
    temp=(x[i]-Minx)/(Maxx-Minx)
    Midx.append(temp)
Maxx=max(x1)
Minx=min(x1)
for i in range(0,m):
    temp=(x1[i]-Minx)/(Maxx-Minx)
    Midx1.append(temp)
    
Jnew=J(Midx,Midx1,y,c0,c1,c2)
JOld=Jnew+1
temp2=0








while(JOld-Jnew)>eps:
    JOld=Jnew
    temp=Grad1(Midx,Midx1,y,c0,c1,c2)
    temp2=Grad2(Midx,Midx1,y,c0,c1,c2)
    c0-=al*Grad0(Midx,Midx1,y,c0,c1,c2)
    c1-=al*temp
    c2-=al*temp2
    Jnew=J(Midx,Midx1,y,c0,c1,c2)
    
print(c0)
print(c1)
print(c2)
smalx=(1500-min(x))/(max(x)-min(x))
smalx1=(3-min(x1))/(max(x1)-min(x1))
h=c0+c1*smalx+c2*smalx1
print(h)

fig, axs = plt.subplots(2, 2)
axs[0, 0].hist (x)
axs[0, 1].hist (x1)
axs[1, 0].hist (Midx)
axs[1, 1].hist (Midx1)