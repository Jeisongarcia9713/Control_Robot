import pandas as pd 
import csv 
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

datos=pd.read_csv('control_5_suelo_adelante_1060.txt',header=0)
tiempo=datos['t']
entrada=datos['i1']
motor1=datos['i2']
motor2=datos['i3']
motor3=datos['i4']
motor4=datos['i5']
control=datos['i6']
fig, ax = plt.subplots()
ax.plot(tiempo, entrada)

ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='About as simple as it gets, folks')
ax.grid()
plt.hold(True);
ax.plot(tiempo, motor1)
#ax.plot(tiempo, motor2)
#ax.plot(tiempo, motor3)
#ax.plot(tiempo, motor4)
ax.plot(tiempo, control/4)

plt.show()
