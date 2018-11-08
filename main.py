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

endpoint = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&"
#origins = input("Where from?:").replace(" ","+")
#destinations = input("Where to?:").replace(" ","+")
#origins = "1902+Rosalie+Ridge+Dr+Huntsville+AL"
#destinations = "143+Tuscany+Lane+Vine+Grove+KY|704+Desoto+Rd+Huntsville+AL"

#Load in all the locations
df = pd.read_csv("Locations.csv")
lat_lon = df[["Latitude","Longitude"]].copy()

#Clean the data and format the dataframe
df = df.drop(["Latitude","Longitude"], axis = 1)
for j in range(len(df)):
    df.iloc[j,1] = df.iloc[j,1].replace(" ","+")

#Create a dictionary to store all the transportation costs for every (origin,destination)
#transportation_costs = dict()
for i in range(len(df)):
    origins = df.iloc[i,1]
    destinations = "|".join(list(df.iloc[:i,1])+list(df.iloc[i+1:,1]))
    nav_req = "origins={}&destinations={}&key={}".format(origins, destinations, my_key)
    request = endpoint + nav_req
    response = urllib.request.urlopen(request).read()
    data = json.loads(response)
    
    transportation_costs[df.iloc[i,0]] = dict()
    distances = data['rows'][0]['elements']
    for j in range(len(distances)):
        distance = distances[j]['distance']['text']
        duration = distances[j]['duration']['text']
        length, l_unit = distance.split()
        length = float(length)
        time, t_unit = duration.split()
        time = float(time)
        transportation_costs[df.iloc[i,0]][df.iloc[j,0]] = time

#matrix = []        
#for k in transportation_costs.keys():
#    v = list(transportation_costs[k].values())
#    row = [0]*(len(df)-len(v))+v
#    matrix.append(row)
#    
#matrix = np.array(matrix)
#matrix = matrix.T
        



        
