#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Tp
#1ère_fractale
import matplotlib.pyplot as plt
import random 
M = [[0.5,0.0]]
x0=0.5
y0=0.0
for i in range(1,30001):
    p = random.uniform(0,1)
    if p<=0.1:
        x = x0*0.05
        y = y0*0.6
    elif 0.1<p<=0.2:
        x = x0*0.05
        y = (y0*(-0.5))+1

    elif 0.2<p<=0.4:
        x = x0*0.46 - y0*0.32
        y = x0*0.39 + y0*0.38 +0.6

    elif 0.4<p<=0.6:
        x = x0*0.47 - y0*0.15
        y = x0*0.17 + y0*0.42 +1.1

    elif 0.6<p<=0.8:
        x = x0*0.43 + y0*0.28
        y = x0*(-0.25) + y0*0.45 +1

    elif 0.8<p<=1:
        x = x0*0.42 + y0*0.26
        y = x0*(-0.35) + y0*0.31 +0.7
    M=M+[[x,y]]
    x0=x
    y0=y
Mx=[i[0] for i in M]
My=[i[1] for i in M]
plt.plot(Mx, My, 'b.')
plt.show()


# In[6]:


#Algorithme_de_barnsley
import matplotlib.pyplot as plt
import random
M = [[0.05,0.0]]
x0=0.05
y0=0.0
for i in range(1,30001):
    p = random.uniform(0,1)
    if p<=0.02:
        x = 0.5
        y = y0*0.27
    elif 0.02<p<=0.17:
        x = x0*(-0.139)+y0*0.263+0.57
        y = x0*0.246+y0*0.224-0.036
       
    elif 0.17<p<=0.30:
        x = x0*0.17 - y0*0.215+0.408
        y = x0*0.222 + y0*0.176 +0.0893
       
    elif 0.30<p<=1:
        x = x0*0.781 + y0*0.034 + 0.1075
        y = x0*(-0.032) + y0*0.739 +0.27
    M=M+[[x,y]]
    x0=x
    y0=y
Mx=[i[0] for i in M]
My=[i[1] for i in M]
plt.plot(Mx, My, 'r.')
plt.show()


# In[3]:


#Triangle de Sierpiński
import matplotlib.pyplot as plt
import random
P0=[[2,2]]
M1=[0,0]
M2=[4,4]
M3=[4,0]
x0=2
y0=1
for i in range(1,15001):
    p = random.uniform(0,1)
    if p<=0.33:
        x=(x0+M1[0])/2
        y=(y0+M1[1])/2
    elif 0.33<p<=0.66:
        x=(x0+M2[0])/2
        y=(y0+M2[1])/2
    elif 0.66<p<=1:
        x=(x0+M3[0])/2
        y=(y0+M3[1])/2
    P0=P0+[[x,y]]
    x0=x
    y0=y
Px=[i[0] for i in P0]
Py=[i[1] for i in P0]
plt.plot(Px, Py, 'gx')
plt.show()

