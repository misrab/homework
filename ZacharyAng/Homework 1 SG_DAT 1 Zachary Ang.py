
# coding: utf-8

# In[326]:

#PART 1:

import pandas as pd
import csv
df=pd.read_csv('/Users/zachang/Desktop/Data Science Course/DAT1/SG_DAT1/data/drinks.csv',keep_default_na=False)    # Read in drinks.csv
header=list(df.columns.values)         # Store the header in a list called 'header'
data=df.values.tolist()                # Store the data in a list of lists called 'data'



# In[58]:

# Part 2 

#Isolate the beer_servings column in a list of integers called 'beers'

beers=df.ix[:,'beer_servings'].tolist() 


# In[78]:

#PART 3:
#Create separate lists of NA and EU beer servings: 'NA_beers', 'EU_beers'


NA_beers_Ind= df['continent']== 'NA'
NA_beers= df.ix[NA_beers_Ind,'beer_servings'].tolist()

EU_beers_Ind= df['continent']== 'EU'
EU_beers= df.ix[EU_beers_Ind,'beer_servings'].tolist()


print len(NA_beers)
print len (EU_beers)


# In[108]:

#PART 4
# Calculate the average NA and EU beer servings to 2 decimals: 'NA_avg', 'EU_avg'
NA_avg= round(float(sum(NA_beers))/len(NA_beers),2)
EU_avg = round(float(sum(EU_beers))/len(EU_beers),2)

print NA_avg
print EU_avg


# In[118]:

#PART 5

# Write a CSV file called 'avg_beer.csv' with two columns and three rows.
# The first row is the column headers: 'continent', 'avg_beer'
# The second and third rows contain the NA and EU values.

newcsv=[['continent','avg_beer'],['NA','145.53'],['EU','193.78']]

with open('avg_beer.csv','wb') as d:
    csv.writer(d).writerows(newcsv)
    
# Question: What is 'wb' in open() and how does with... as work? 
# Comment: Writing CSV doesn't work in python notebook



# In[171]:

# PART 6:
# Use the requests module to pull in weather data for any city

import requests as rq

api_endpoint = 'http://api.openweathermap.org/data/2.5/forecast/city'

params={}
params['APPID'] = '20cb4dc243b8bff294ab2aaa28178156'
params['id']='1880252' # ID for Singapore
params['units']='metric' # Metric System
r = rq.get(api_endpoint,params) # Executes GET query
json_weather_data = r.json() # Decodes response in JSON

weather_data=json_weather_data['list']


# In[290]:

## Extract Temperature, Humidity and Pressure

temperatures = [data_point['main']['temp'] for data_point in weather_data]
humidity = [data_point['main']['humidity'] for data_point in weather_data]
pressure = [data_point['main']['pressure'] for data_point in weather_data]



# In[292]:

# PART 7
# Create a list of the pressure measurements and plot it against dates

from datetime import datetime
import matplotlib.pyplot as plot

dates =[data_point['dt'] for data_point in weather_data]

dates = [datetime.fromtimestamp(d) for d in dates]
plot.scatter(dates,pressure, color='blue',s=1)

plot.ylabel('Pressure')
plot.xlabel('Date')
plot.title('Pressure vs Date')
plot.xlim(dates[0],dates[-1])
plot.show()

## Dates don't show properly


# In[293]:


#Part 8
# Make a scatter plot plotting pressure against temperature and humidity


plot.scatter(temperatures,humidity,color='blue',s=1)
plot.ylabel('Pressure')
plot.xlabel('Humidity')
plot.title('Pressure vs Humidity')
plot.show()


# In[327]:


'''
BONUS:
Learn csv.DictReader() and use it to redo Parts 1, 2, and 3.
'''

with open('/Users/zachang/Desktop/Data Science Course/DAT1/SG_DAT1/data/drinks.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    b_data = [row for row in reader]
    
beers = [d['beer_servings'] for d in b_data]
NA_beers = [d['beer_servings'] for d in b_data if d['continent'] == 'NA']
EU_beers = [d['beer_servings'] for d in b_data if d['continent'] == 'EU']

