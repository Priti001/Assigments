
# coding: utf-8

# In[1]:

# Dependencies
import csv
import matplotlib.pyplot as plt
import requests as req
import pandas as pd


# In[3]:

# Save config information.
api_key = "3f1f5f418e58028aa38ca108fb027e36"
#url = "http://api.openweathermap.org/data/2.5/weather?"
url = "http://api.openweathermap.org/data/2.5/find?"
cityno= 50
# Build partial query URL
query_url = url + "appid=" + api_key + "lat=55.5&lon=37.5&cnt=" + str(cityno)

#+ "lat=55.5&lon=37.5&cnt=" + cityno


# In[4]:

weather_data = []
cities = randPoints

# Loop through the list of cities and perform a request for data on each
for city in cities:
    response = req.get(query_url + str(cityno) ).json()
    weather_data.append(response)

weather_data


# In[9]:

import random

radius = 200
rangeX = (0, 2500)
rangeY = (0, 2500)
qty = 100  # or however many points you want

# Generate a set of all points within 200 of the origin, to be used as offsets later
# There's probably a more efficient way to do this.
deltas = set()
for x in range(-radius, radius+1):
    for y in range(-radius, radius+1):
        if x*x + y*y <= radius*radius:
            deltas.add((x,y))

randPoints = []
excluded = set()
i = 0
while i<qty:
    x = random.randrange(*rangeX)
    y = random.randrange(*rangeY)
    if (x,y) in excluded: continue
    randPoints.append((x,y))
    i += 1
    excluded.update((x+dx, y+dy) for (dx,dy) in deltas)
print (randPoints)


# In[10]:

# Dependencies
get_ipython().system('pip install citipy')
from citipy import citipy

# Some random coordinates
#coordinates = [(200, 200), (23, 200), (42, 100)]
coordinates = randPoints
cities = []
for coordinate_pair in coordinates:
    lat, lon = coordinate_pair
    cities.append(citipy.nearest_city(lat, lon))

for city in cities:
    country_code = city.country_code
    name = city.city_name
    print("The country code of " + name + " is '" + country_code + "'.")


# In[8]:

cities 


# In[ ]:



