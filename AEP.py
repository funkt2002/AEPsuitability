from importlib.machinery import WindowsRegistryFinder
import json
import statistics as stat
import math
import numpy as np
import matplotlib.pyplot as plt
from geopy.geocoders import nominatim




Airport={
'windspeed':12.301423877327544,
'temp':59.758926615553115,
'pressure':1014.9667031763418,
'humidity':73.88318729463309,
'Air Density':1.061596496188917,
'AEP':15520886.529846704
}

Cachuma={
'windspeed':13.336199342825873,
'temp':58.02316538882803,
'pressure':1015.499178532311,
'humidity':70.15624315443593,
'Air Density':1.0677197688686593,
'AEP':19890441.18286713
}

El_Capitan={
'windspeed':12.183187294633079,
'temp':58.52157721796276,
'pressure':1015.3057502738226,
'humidity':71.30909090909091,
'Air Density':1.0659123605130232,
'AEP':15138929.18887238
}

Farren={
'windspeed':11.607995618838988,
'temp':59.23406352683461,
'pressure':1015.0336801752464,
'humidity':72.90635268346112,
'Air Density':1.0633427109880134,
'AEP':13062787.497252442
}

Gaviota={
'windspeed':12.337239868565225,
'temp':59.76621029572837,
'pressure':1014.9665388828039,
'humidity':73.88181818181819,
'Air Density':1.0615731032891158,
'AEP':15656505.298507612
}

Holiday_hill={
'windspeed':12.108871851040519,
'temp':59.62864184008762,
'pressure':1014.9678532311062,
'humidity':73.86122672508215,
'Air Density':1.0620132295223548,
'AEP':14809209.361230614
}

Hollister_ranch={
'windspeed':13.085980284775449,
'temp':57.74041621029573,
'pressure':1016.0130887185104,
'humidity':72.23915662650603,
'Air Density':1.0691732886506067,
'AEP':18817320.505112473
}

paradise={
'windspeed':11.739649507119381,
'temp':59.24277108433735,
'pressure':1015.0542168674699,
'humidity':72.39961664841184,
'Air Density':1.0633363965800189,
'AEP':13512228.147767385
}
point_conception={
'windspeed':15.939156626506032,
'temp':56.761938663745894,
'pressure':1016.5408543263966,
'humidity':72.39961664841184,
'Air Density':1.0729012016332644,
'AEP':34122955.78408149
}
Rincon={
'windspeed':12.192716319824788,
'temp':60.85859802847754,
'pressure':1015.2587623220153,
'humidity':70.45859802847754,
'Air Density':1.0584069093241992,
'AEP':15067630.848765777    
}

San_Marcos={
'windspeed':11.930284775465486,
'temp':59.55963855421687,
'pressure':1014.9872946330777,
'humidity':73.42261774370209,
'Air Density':1.0622538072253442,
'AEP':14166795.486275364
}
SB_Harbor={
'windspeed':12.23165388828038,
'temp':59.876451259583796,
'pressure':1015.3082146768894,
'humidity':72.08050383351588,
'Air Density':1.0615793804206162,
'AEP':15258046.08123318
}

Vandenburg={
'windspeed':15.05947426067908,
'temp':56.08329682365827,
'pressure':1016.6170317634171,
'humidity':79.14507119386636,
'Air Density':1.0751929017814985,
'AEP':28840761.10038117}

###windspeed###
AEP={'Vandenburg':28840761.1,'SB_Harbor':15258046.08,'San_Marcos':14166795.49,
'paradise':13512228.15,'Holiday_hill':14809209.361230614,'Hollister_ranch':18817320.50,
'Gaviota':15656505.298507612,'Farren':13062787.497252442,'El_Capitan':15138929.18887238,
'Cachuma':19890441.18286713,'Airport':15520886.529846704,'Rincon':15067630.848765777,'point_conception':34122955.78408149}

keys=AEP.keys()
values=AEP.values()
plt.bar(keys,values)

def watts_to_dolars():
    for i in (values):
        return(0.084*i) #watts into doll hairs

watts_to_dolars()

