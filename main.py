# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 17:04:06 2018

@author: mlhar
"""
import urllib.request
import json
import pandas as pd
import numpy as np
from api_key import my_key
from itertools import permutations
from model import cost_func, create_model, get_sample, test_pulp, create_poss


#endpoint = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&"
#
##Load in all the locations
#df = pd.read_csv("Locations.csv")
#lat_lon = df[["Latitude","Longitude"]].copy()
#
##Clean the data and format the dataframe
#df = df.drop(["Latitude","Longitude"], axis = 1)
#for j in range(len(df)):
#    df.iloc[j,1] = df.iloc[j,1].replace(" ","+")
#
##Create a dictionary to store all the transportation costs for every (origin,destination)
#transportation_costs = {name:dict() for name in df["Location"]}
#for i in range(len(df)):
#    origins = df.iloc[i,1]
#    destinations = "|".join(list(df.iloc[:,1]))
#    nav_req = "origins={}&destinations={}&key={}".format(origins, destinations, my_key)
#    request = endpoint + nav_req
#    response = urllib.request.urlopen(request).read()
#    data = json.loads(response)
#    
#    distances = data['rows'][0]['elements']
#    dest = list(df.iloc[:,0])
#    for j in range(len(distances)):
#        distance = distances[j]['distance']['text']
#        duration = distances[j]['duration']['text']
#        length, l_unit = distance.split()
#        length = float(length)
#        time, t_unit = duration.split()
#        time = float(time)        
#        transportation_costs[df.iloc[i,0]][dest[j]] = time

places = list(df.iloc[1:,0])
idx = list(range(1,len(places)+1))
perm = permutations(idx,5)
perm = np.array(list(perm))
    
costs = cost_func(transportation_costs, places, perm)
sample = create_poss(costs)

if test_pulp(sample):
    create_model(places, sample)
else:
    print("No such luck")
            