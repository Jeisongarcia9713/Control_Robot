
import serial 
import time
import numpy as np
import pandas as pd

def guardar():  
        VL=[]
        VR=[]
        Motor1=[]
        Motor2=[]
        Motor3=[]
        Motor4=[]
        W=[]
        theta=[]
        
        for i in datosID:
                resultados=i.split(",")
                #print(resultados)
                VR.append(resultados[0])
                VL.append(resultados[1])
                Motor1.append(resultados[2])
                Motor2.append(resultados[3])
                Motor3.append(resultados[4])
                Motor4.append(resultados[5])
                W.append(resultados[6])
                theta.append(resultados[7])
                
        Tiempo  = pd.Series(tiempo,name='t')        
        In   = pd.Series(VR,name='i1')
        In1  = pd.Series(VL,name='i2')
        Mot1 = pd.Series(Motor1,name='i3')
        Mot2 = pd.Series(Motor2,name='i4')
        Mot3 = pd.Series(Motor3,name='i5')
        Mot4 = pd.Series(Motor4,name='i6')
        Vangular = pd.Series(W,name='i7')
        angulo = pd.Series(theta,name='i8')

        m =pd.concat([Tiempo,In,In1,Mot1,Mot2,Mot3,Mot4,Vangular,angulo],axis=1)
        m.to_csv('linea_recta3.txt',header=True,index=False)
        print('termino')

if __name__ == "__main__":
                 
        tiempo=[]
        datosID=[]
        times=0
        ser = serial.Serial()
        ser.baudrate = 115200
        ser.port = '/dev/ttyACM0'
        ser.open()
        time.sleep(2)
        #ser.write(('b').encode('cp1250'))
        ser.write(('a').encode('cp1250'))
        
        while 1:
                ser.flush()
                datos=ser.readline()
                print(datos)
                if (datos.decode('cp1250').replace('\n','')=='B'):
                        guardar()
                        ser.close()
                        break
                else:
                        datosID.append(datos.decode('cp1250').replace('\n',''))
                        tiempo.append(times)
                        times=times+0.01


