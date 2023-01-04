from importlib.machinery import WindowsRegistryFinder
import json
import statistics as stat
import math
import numpy as np
import geopy.distance
from matplotlib import pyplot as plt

cost_per_watt_per_mile=0.001502 #dollars

AEP={'Vandenburg':28840761.1,'SB_Harbor':15258046.08,'San_Marcos':14166795.49,
'paradise':13512228.15,'Holiday_hill':14809209.361230614,'Hollister_ranch':18817320.50,
'Gaviota':15656505.298507612,'Farren':13062787.497252442,'El_Capitan':15138929.18887238,
'Cachuma':19890441.18286713,'Airport':15520886.529846704,'Rincon':15067630.848765777,'point_conception':34122955.78408149}

keys=AEP.keys()
values=AEP.values()


def watts_to_dolars():
    for i in (values):
        print(0.084*i) #watts into doll hairs

watts_to_dolars()

transportcost_Airport=0.931*0.001502
transportcost_Cachuma=16.081*0.001502
transportcost_El_Capitan=1.232*0.001502
transportcost_Farren=2.874*0.001502
transportcost_Gaviota=2.78*0.001502
transportcost_Holliday=2.053*0.001502
transportcost_Hollister=10.737*0.001502
transportcost_Paradise=7.496*0.001502
transportcost_Point=37.195*0.001502
transportcost_Rincon=7.95*0.001502
transportcost_SanMarcos=3.4*0.001502
transportcost_SBHArbor=7.95*0.001502
transportcost_Vandenburg=41.4*0.001502
AEPvalue_Van=2422623.93
AEPvalue_SBH=1281675.87
AEPvalue_SAN=1190010.82
AEPvalue_PAR=1135027.165
AEPvalue_GAV=1243973.59
AEPvalue_HILL=1580654.922
AEPvalue_RAN=1315146.445
AEPvalue_FAR=1097274.15
AEPvalue_ELC=1271670.052
AEPvalue_CAC=1670797.06
AEPvalue_AIR=1303754.49
AEPvalue_RIN=1265680.99
AEPvalue_POI=2866328.285
Airportnet=AEPvalue_AIR-(AEPvalue_AIR*transportcost_Airport)
Cachumanet=AEPvalue_CAC-(AEPvalue_CAC*transportcost_Cachuma)
Elcapnet=AEPvalue_ELC-(AEPvalue_ELC*transportcost_El_Capitan)
Farrennet=AEPvalue_FAR-(AEPvalue_FAR*transportcost_Farren)
Gaviotanet=AEPvalue_GAV-(AEPvalue_GAV*transportcost_Gaviota)
Hollidaynet=AEPvalue_HILL-(AEPvalue_HILL*transportcost_Holliday)
Paradisenet=AEPvalue_PAR-(AEPvalue_PAR*transportcost_Paradise)
Pointnet=AEPvalue_POI-(AEPvalue_POI*transportcost_Point)
Hollisternet=AEPvalue_RAN-(AEPvalue_RAN*transportcost_Hollister)
Rinconnet=AEPvalue_RIN-(AEPvalue_RIN*transportcost_Rincon)
Vandenburgnet=AEPvalue_Van-(AEPvalue_Van*transportcost_Vandenburg)
SanMarcosnet=AEPvalue_SAN-(AEPvalue_SAN*transportcost_SanMarcos)
SBHarbornet=AEPvalue_SBH-(AEPvalue_SBH*transportcost_SBHArbor)
net_list=[Airportnet,Cachumanet,Elcapnet,Farrennet,Gaviotanet,Hollidaynet,Paradisenet,Pointnet,Hollisternet,Rinconnet,Vandenburgnet,SanMarcosnet,SBHarbornet]
locations=['Airport','Cachuma', 'Elcap', 'Farren', 'Gaviota', 'Holliday_Hill', 'Paradise', 'Point_Conception','Hollister', 'Rincon', 'Vandenburg', 'SanMarcos','SBharbor']

print(net_list)
plt.bar(locations,net_list)
plt.show()