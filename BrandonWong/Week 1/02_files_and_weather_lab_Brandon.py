print "\nBRANDON WONG - Required HW Week 1 (02_files_and_weather_lab)"
print "\n"

#Part 1 - Store header in list 'header' & data in list of lists 'data'

print "\nPART 1" #Title
print "\n" #New empty opening paragraph

import csv
with open('C:\Users\Brandon\SG_DAT1\data\drinks.csv', 'rU') as f:
	header = csv.reader(f).next()
	data = [row for row in csv.reader(f)]
	print "Header:"
	print header

print "\n" #New empty closing paragraph

#Part 2 - Isolate beer_servings column in list of int 'beers'

print "\nPART 2"
print "\n"

beers = [int(row[1]) for row in data]
print "beers =", beers
print "\n" #just to differentiate
print "len(beers) =", len(beers)

print "\n"

#Part 3 - Create seperate lists of NA & EU beer servings: 'NA_beers', 'EU_beers'

print "\nPART 3"
print "\n"

NA_beers = [int(row[1]) for row in data if row[5].upper() == 'NA']
print "NA_beers =", NA_beers
print "\n"
print "len(NA_beers) =", len(NA_beers)

print "\n" 

EU_beers = [int(row[1]) for row in data if row[5].upper() == 'EU']
print "EU_beers =", EU_beers
print "\n"
print "len(EU_beers) =", len(EU_beers)

print "\n"


#Part 4 - Calculate avg NA and EU beer servings to 2 decimals: 'NA_avg', 'EU_avg'

print "\nPART 4"
print "\n"

NA_avg = round(float(sum(NA_beers))/len(NA_beers),2) #round off to 2 dp
print "NA_avg =", NA_avg

print "\n"

EU_avg = round(float(sum(EU_beers))/len(EU_beers),2) 

print "\n"


#Part 5 - Write CSV called 'avg_beer.csv' w 2 columns 3 rows.

print "\nPART 5"
print "\n"

avg_dict = {"NA":NA_avg, "EU":EU_avg}
output_folder = 'C:\\Users\\Brandon\\SG_DAT1_Brandon\\' #need double slash "\\" to clearly define folder
outputfile_name = 'avg_beer.csv' #no need to add "\" before outputfile_name
outputfile_path = output_folder + outputfile_name
with open(outputfile_path,'wb') as outputfile:
    outputwriter = csv.writer(outputfile)
    outputwriter.writerow(['continent','avg_beer'])
    for continent in avg_dict:
        outputwriter.writerow([continent,avg_dict[continent]])
print "Wrote output to %s" % outputfile_path

print "\n"


#Part 6 - Use requests module to pull in weather data for any city (Chose Singapore)

print "\nPART 6"
print "\n"

import requests #module for reading web

api_endpoint = 'http://api.openweathermap.org/data/2.5/forecast/city'

params = {}
params['id'] = 1561096 #Hanoi, Vietnam ID
params['units'] = 'metric'
params['APPID'] = '85c936ecf55d1973bf69098c9e5b62f1' #my own unique APPID
request = requests.get(api_endpoint, params = params)

data = request.json()
weather_data = data['list']

temperatures = [data_point['main']['temp'] for data_point in weather_data]
humidity = [data_point['main']['humidity'] for data_point in weather_data]

print "DATA FOR HANOI" #title for data block
print "\n"

dates = [data_point['dt'] for data_point in weather_data]
from datetime import datetime
dates = [datetime.fromtimestamp(epoch) for epoch in dates]
for data_row in zip(dates,temperatures,humidity):
    print data_row

print "\n"

#Part 7 - Create a list of the pressure measurements and plot it against dates

print "\nPART 7"
print "\n"

import matplotlib.pyplot as plt #module for plot

pressures = [data_point['main']['pressure'] for data_point in weather_data]
plt.plot(dates, pressures)
plt.xlabel("Time")
plt.ylabel("Pressure [hPa]")
plt.title("Pressure in Hanoi")
plt.show()

#note: Idk why my time (x-axis) is so muddled. Need to figure out!

print "'Pressure in Hanoi' graph printed out in word file"

print "\n"

#Part 8 - Make a scatter plot plotting pressure against temperature and humidity

print "\nPART 8"
print "\n"

import numpy as np #module for numpy
import matplotlib.pyplot as plt

fig = plt.figure()
ax1 = fig.add_subplot(111)
Temperature = ax1.scatter(pressures, temperatures, label='Temperature')
ax2 = ax1.twinx() #adding a secondary y-axis
Humidity = ax2.scatter(pressures, humidity, marker='x', color='r', label='Humidity')
plt.legend(handles = [Temperature, Humidity]) #state plot legends
ax1.set_xlabel("Pressure [hPa]") #x-axis label
ax1.set_ylabel("Temperature [C]")#y-axis1 label
ax2.set_ylabel("Humidity [%]") #y-axis2 label
plt.title("Pressure (x) vs Temperature (y1) & Humidity (y2): Hanoi")
plt.show()

print "'Multi-Axis Scatterplot Graph for Hanoi' graph printed out in word file"
print "\n"