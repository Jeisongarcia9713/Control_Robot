import pandas as pd 
import csv 
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

datos=pd.read_csv('VelocidadAngular4.txt',header=0)
tiempo=datos['t']
VL=datos['i1']/60
VR=datos['i2']/60
motor1=datos['i3']/60
motor2=datos['i4']/60
motor3=datos['i5']/60
motor4=datos['i6']/60
W=datos['i7']
Angulo=datos['i8']
fig, ax = plt.subplots()
ax.plot(tiempo, VR)

ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='About as simple as it gets, folks')
ax.grid()
plt.hold(True);
ax.plot(tiempo, VL)
ax.plot(tiempo, motor1)
ax.plot(tiempo, motor2)
ax.plot(tiempo, motor3)
ax.plot(tiempo, motor4)
ax.plot(tiempo, W)
ax.legend(['VR','VL','motor1','motor2','motor3','motor4','W'])
plt.show()

print(np.mean(motor1))
print(np.mean(motor2))
print(np.mean(motor3))
print(np.mean(motor4))
print(np.mean(W))