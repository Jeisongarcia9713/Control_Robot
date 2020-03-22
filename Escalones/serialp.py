
import serial 
import time
import numpy as np
import pandas as pd

def guardar():  
        Tiempo  = pd.Series(tiempo,name='t')
        Entrada=[]
        Motor1=[]
        Motor2=[]
        Motor3=[]
        Motor4=[]
        for i in datosID:
                resultados=i.split(",")
                #print(resultados)
                Entrada.append(resultados[0])
                Motor1.append(resultados[1])
                Motor2.append(resultados[2])
                Motor3.append(resultados[3])
                Motor4.append(resultados[4])
        In  = pd.Series(Entrada,name='i1')
        Mot1 = pd.Series(Motor1,name='i2')
        Mot2 = pd.Series(Motor2,name='i3')
        Mot3 = pd.Series(Motor3,name='i4')
        Mot4 = pd.Series(Motor4,name='i5')

        m =pd.concat([Tiempo,In,Mot1,Mot2,Mot3,Mot4],axis=1)
        #m.to_csv('datos_identificacion4_reversa_V1045.txt',header=True,index=False)
        print('termino')

if __name__ == "__main__":
                 
        tiempo=[]
        datosID=[]
        times=0
        ser = serial.Serial()
        ser.baudrate = 115200
        ser.port = 'com30'
        ser.open()
        time.sleep(2)
        #ser.write(('b').encode('cp1250'))
        ser.write(('a').encode('cp1250'))
        
        while 1:
                ser.flush()
                datos=ser.readline()
                if (datos.decode('cp1250').replace('\n','')=='B'):
                        guardar()
                        ser.close()
                        break
                else:
                        datosID.append(datos.decode('cp1250').replace('\n',''))
                        tiempo.append(times)
                        times=times+0.01


