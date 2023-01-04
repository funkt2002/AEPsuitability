from importlib.machinery import WindowsRegistryFinder
import json
import statistics as stat
import math
import numpy as np
import geopy.distance


def distance_Airport():
    loc=(34.4253,-119.836)
    battery=(34.42,-119.851)
    AirD=geopy.distance.geodesic(loc,battery).miles
    print(AirD)
def distance_Cachuma():
    loc=(34.5857,-119.992)
    battery=(34.452,-119.761)
    CacD=geopy.distance.geodesic(loc,battery).miles
    print(CacD)
def distance_El_Capitan():
    loc=(34.465,-120.026)
    battery=(34.477,-120.042)
    ElD=geopy.distance.geodesic(loc,battery).miles
    print(ElD)
def distance_Farren():
    loc=(34.4685,-119.922)
    battery=(34.431,-119.9)
    FarD=geopy.distance.geodesic(loc,battery).miles
    print(FarD)
def distance_Gaviota():
    loc=(34.4349,-119.828)
    battery=(34.476,-120.199)
    GavD=geopy.distance.geodesic(loc,battery).miles
    print(GavD)
def distance_Holliday():
    loc=(34.4349,-119.828)
    battery=(34.4644,-119.833)
    dayD=geopy.distance.geodesic(loc,battery).miles
    print(dayD)
def distance_Hollister():
    loc=(34.4718,-120.23)
    battery=(34.477,-120.042)
    HollD=geopy.distance.geodesic(loc,battery).miles
    print(HollD)
def distance_Paradise():
    loc=(34.4349,-119.828)
    battery=(34.5436,-119.824)
    ParD=geopy.distance.geodesic(loc,battery).miles
    print(ParD)
def distance_Point():
    loc=(34.6556,-119.828)
    battery=(34.6556,-120.481)
    PointD=geopy.distance.geodesic(loc,battery).miles
    print(PointD)
def distance_Rincon():
    loc=(34.4349,-119.828)
    battery=(34.4036,-119.694)
    RinD=geopy.distance.geodesic(loc,battery).miles
    print(RinD)
def distance_SanMarcos():
    loc=(34.49,-119.799)
    battery=(34.452,-119.761)
    SanD=geopy.distance.geodesic(loc,battery).miles
    print(SanD)
def distance_SBHArbor():
    loc=(34.4349,-119.828)
    battery=(34.4036,-119.694)
    HarD=geopy.distance.geodesic(loc,battery).miles
    print(HarD)
def distance_Vandenburg():
    loc=(34.4349,-119.828)
    battery=(34.7376,-120.45535)
    VanD=geopy.distance.geodesic(loc,battery).miles
    print(VanD)

distance_Airport()
distance_Cachuma()
distance_El_Capitan()
distance_Farren()
distance_Gaviota()
distance_Holliday()
distance_Hollister()
distance_Paradise()
distance_Point()
distance_Rincon()
distance_SanMarcos()
distance_SBHArbor()
distance_Vandenburg()
    
