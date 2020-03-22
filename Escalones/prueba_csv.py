import pandas as pd 
import csv 
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

datos=pd.read_csv('datos_identificacion.txt',header=0)
tiempo=datos['tiempo']
entrada=datos['scontrol']

fig, ax = plt.subplots()
ax.plot(tiempo, entrada)

ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='About as simple as it gets, folks')
ax.grid()

plt.show()
