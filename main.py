# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 17:04:06 2018

@author: mlhar
"""
import urllib.request
import json
from api_key import my_key

endpoint = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&"
origins = input("Where from?:").replace(" ","+")
destinations = input("Where to?:").replace(" ","+")
nav_req = "origins={}&destinations={}&key={}".format(origins, destinations, my_key)

request = endpoint + nav_req
response = urllib.request.urlopen(request).read()
distances = json.loads(response)

