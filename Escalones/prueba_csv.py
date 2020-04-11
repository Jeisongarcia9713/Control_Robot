import pandas as pd 
import csv 
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

datos=pd.read_csv('con_2_mismoSentido_gan_60.txt',header=0)
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
ax.plot(tiempo, motor2)
ax.plot(tiempo, motor3)
ax.plot(tiempo, motor4)
#ax.plot(tiempo, control)
ax.legend(['entrada','motor1','motor2','motor3','motor4','control'])
plt.show()

print(np.mean(motor1))
print(np.mean(motor2))
print(np.mean(motor3))
print(np.mean(motor4))