from importlib.machinery import WindowsRegistryFinder
import json
import statistics as stat
import math
import numpy as np
with open('Point_Conception_Lompoc_CA.json') as f:
    data=json.load(f)
    def windspeed():
        avg=0
        sum=0
        for i in data['days']:
            sum+=i['windspeed']
            avg=sum/len(data['days'])
        return(avg)
        return(avg)
    windspeed=float(windspeed())
    def variance():  
         winddir=[]
         for i in data['days']:    
             winddir.append(i['winddir'])
         winds=np.array(winddir)
         return(np.std(winds, axis=0))
         
    def pressure():
        P=[] 
        for i in data['days']:
            P.append(i['pressure'])
        Press=np.array(P)
        return(np.mean(Press))
    pressure=float(pressure())
   
    def humidity():
        H=[] 
        for i in data['days']:
            H.append(i['humidity'])
        Hum=np.array(H)
        return(np.mean(Hum))
         
    def temperature():
        T=[]
        for i in data['days']:
            T.append(i['temp'])
        Temp=np.array(T)
        return(np.mean(Temp))
    temperature=(temperature())
    
    def air_Density(pressure=pressure, temperature=temperature):
        print('po')
        A=1.276/(1+(0.00366*temperature))
        B=(pressure-(0.378*2.718281828))/1000
        density=A*B
        return(density)
    air_Density=float(air_Density())
   
    def power_watts(air_Density=air_Density, windspeed=windspeed):
#AEP is calced by P=0.5Density*Cross-sctionbladearea(m^2)*windspeed^3
# blade length set to consistent 50m
#cross-sction=pi(50^2)
        A=air_Density*7854.0#m^2                      #number is a rough cross sectional area of wind turbine, same for all
        B=windspeed**3.0
        C=A*B
        return C
    power_watts=float(power_watts())



print(windspeed)        
print(temperature)
print(pressure)
print(humidity)
print(air_Density)
print(power_watts)
