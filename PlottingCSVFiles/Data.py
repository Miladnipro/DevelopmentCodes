##
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
##
Data=pd.read_excel('Third.xlsx', sheet_name='First')
Data2=pd.read_excel('Third.xlsx', sheet_name='Second')
##
Datanp=np.array(Data)
Datanp2=np.array(Data2)
##
Time1=(Datanp[6:,0]*0.001)/60
P1=Datanp[6:,1]

Time2=(Datanp2[:,0]*0.001)/60
P2=Datanp2[:,1]

##
plt.plot(Time1, P1)
plt.title("PBin")
plt.xlabel("Time [ms]")
plt.ylabel("Pressure [mmHg]")
plt.xlim(1.509e7,1.67e7)
plt.grid()
plt.show()

##

plt.plot(Time2, P2)
plt.title("PBD")
plt.xlabel("Time [ms]")
plt.ylabel("Pressure [mmHg]")
plt.grid()
plt.show()
##
plt.subplot(2, 2, 1)
plt.plot(Time1-Time1[0], P1,color='red')
plt.title("PBin")
plt.xlabel("Time [min]")
plt.ylabel("Pressure [mmHg]")

plt.grid()
plt.show()

plt.subplot(2, 2, 2)
plt.plot(Time1-Time1[0], P1,color='red')
plt.title("PBin")
plt.xlabel("Time [min]")
plt.ylabel("Pressure [mmHg]")
# plt.xlim(1.509e7,1.67e7)
plt.xlim(250-Time1[0],280-Time1[0])
plt.ylim(50,180)
plt.grid()
plt.show()

plt.subplot(2, 2, 3)
plt.plot(Time2-Time2[0], P2,color='blue')
plt.title("PDin")
plt.xlabel("Time [min]")
plt.ylabel("Pressure [mmHg]")
plt.grid()
plt.show()

plt.subplot(2, 2, 4)
plt.plot(Time2-Time2[0], P2,color='blue')
plt.title("PDin")
plt.xlabel("Time [min]")
plt.ylabel("Pressure [mmHg]")
plt.xlim(250-Time2[0],280-Time2[0])
plt.ylim(50,180)
plt.grid()
plt.show()

##
Pressure1=

Time2=
Pressure2=

##
Qb=Datanp[:,0]
Clearance=Datanp[:,1]
UFrate=Datanp[:,2]
ReCirc=Datanp[:,3]
Treatment=Datanp[:,5]