'''
Lab: Reading and Writing Files in Python
'''

import csv

'''
PART 1:
Read in drinks.csv
Store the header in a list called 'header'
Store the data in a list of lists called 'data'
Hint: you've already seen this code!
'''

header = None
data = []

with open('data/drinks.csv', 'rb') as csvfile:
    drinks = csv.reader(csvfile)
    index = 0
    for drink in drinks:
        if index == 0:
            header = drink
        else:
            data.append(drink)
        index += 1

print "Part 1a - Header list of drinks.csv is as follows:"
print header
print
print "Part 1b - The data in the list of lists is as follows:"
print len(data)
print 

'''
PART 2:
Isolate the beer_servings column in a list of integers called 'beers'
Hint: you can use a list comprehension to do this in one line
Expected output:
    beers == [0, 89, ..., 32, 64]
    len(beers) == 193
'''

beers = [int(row[1]) for row in data]

print "Part 2a - The list representing the data for the beer_servings column is as follows:"
print beers
print
print "Part 2b - The list has", len(beers), "items."
print

'''
PART 3:
Create separate lists of NA and EU beer servings: 'NA_beers', 'EU_beers'
Hint: you can use a list comprehension with a condition
Expected output:
    NA_beers == [102, 122, ..., 197, 249]
    len(NA_beers) == 23
    EU_beers == [89, 245, ..., 206, 219]
    len(EU_beers) == 45
'''

NA_beers = [int(row[1]) for row in data if row[5] == 'NA']
EU_beers = [int(row[1]) for row in data if row[5] == 'EU']

print "Part 3a - The list of NA beer servings is as follows:"
print NA_beers
print
print "Part 3b - The NA beers servings list has", len(NA_beers), "items."
print
print "Part 3c - The list of EU beer servings is as follows:"
print EU_beers
print 
print "Part 3d - The EU beers servings list has", len(EU_beers), "items."
print

'''
PART 4:
Calculate the average NA and EU beer servings to 2 decimals: 'NA_avg', 'EU_avg'
Hint: don't forget about data types!
Expected output:
    NA_avg == 145.43
    EU_avg == 193.78
'''

NA_avg = round(sum(NA_beers) * 1.0 / len(NA_beers), 2)
EU_avg = round(sum(EU_beers) * 1.0 / len(EU_beers), 2)

print "Part 4a - NA beers servings has an average of", NA_avg
print
print "Part 4b - EU beers servings has an average of", EU_avg
print

'''
PART 5:
Write a CSV file called 'avg_beer.csv' with two columns and three rows.
The first row is the column headers: 'continent', 'avg_beer'
The second and third rows contain the NA and EU values.
Hint: think about what data structure will make this easy
Expected output (in the actual file):
    continent,avg_beer
    NA,145.43
    EU,193.78
'''

b = open('avg_beer.csv', 'w')
a = csv.writer(b)
data = [['continent', 'avg_beer'],\
        ['NA', NA_avg],\
        ['EU', EU_avg]]
a.writerows(data)
b.close()

print "Part 5 - In the same folder as the python file, there should be a file created named avg_beer.csv that contains the average beer servings for the NA and EU continents"
print

'''
Part 6:
Use the requests module to pull in weather data for any city
Hint: you can use Istanbul from the other code file but you can search
for cities at http://openweathermap.org/find

Create a dates list that stores the date of each datapoint as well as
temperature and humidity

You've already seen this code!
'''

import requests

params = {}
params['id'] = '5375480' #Mountain View
params['units'] = 'metric'
params['APPID'] = 'd54751d82949bf8b57dffb9161671f07'

r = requests.get('http://api.openweathermap.org/data/2.5/forecast/city', params = params)

# print r
# print r.text
d = r.json()

#print d.keys()
#print d['city']
#print d['cnt']
dates = []
temps = []
humis = []

from datetime import datetime

for item in d['list']:
    date = datetime.fromtimestamp(item['dt'])
    temp = item['main']['temp']
    humi = item['main']['humidity']
    dates.append(date)
    temps.append(temp)
    humis.append(humi)

print "Part 6 - The date, temperature, and humidity datasets are as follows:"
print
print "Dates:"
print dates
print
print "Temperature:" 
print temps
print
print "Humidity:"
print humis
print

'''
Part 7
Create a list of the pressure measurements and plot it against dates
'''

press = []

for item in d['list']:
    pres = item['main']['pressure']
    press.append(pres)

import matplotlib.pyplot as plt

print "Part 7 - At this point, a chart showing the time series of the air pressure in Mountain View should appear as another window. Close that window to continue the program."
print

plt.xlabel('Time')
plt.ylabel('Pressure')
plt.title('Mountain View - Time vs. Pressure')
ocs, labels = plt.xticks()
plt.setp(labels, rotation=30)
plt.plot(dates, press, label='Pressure')
plt.show()

'''
Part 8
Make a scatter plot plotting pressure against temperature and humidity
'''

print "Part 8a - Now, a chart showing the air pressure vs. temperature in Mountain View should appear as another window. Close that window to continue the program."
print

plt.xlabel('Pressure')
plt.ylabel('Temperature (in celcius)')
plt.title('Mountain View - Pressure vs. Temperature')
plt.scatter(press, temps)
plt.show()

print "Part 8b - Lastly, a chart showing the air pressure vs. humidity in Mountain View should appear as another window. Close that window to continue the program."
print

plt.xlabel('Pressure')
plt.ylabel('Humidity')
plt.title('Mountain View - Pressure vs. Humidity')
plt.scatter(press, humis)
plt.show()

'''
BONUS:
Learn csv.DictReader() and use it to redo Parts 1, 2, and 3.
'''

print "Bonus questions!"
print 

'''
PART 1:
Read in drinks.csv
Store the header in a list called 'header'
Store the data in a list of lists called 'data'
Hint: you've already seen this code!
'''

dictheader = None
dictdata = []

with open('data/drinks.csv', 'rb') as csvfile:
    drinks = csv.DictReader(csvfile)
    for drink in drinks:
        if dictheader == None:
            dictheader = drink.keys()
        drinkdata = []
        for item in header:
            drinkdata.append(drink[item])
        dictdata.append(drinkdata)

print "Bonus 1a - Header list of drinks.csv is as follows:"
print dictheader
print
print "Bonus 1b - The data in the list of lists is as follows:"
print len(dictdata)
print 

'''
PART 2:
Isolate the beer_servings column in a list of integers called 'beers'
Hint: you can use a list comprehension to do this in one line
Expected output:
    beers == [0, 89, ..., 32, 64]
    len(beers) == 193
'''

with open('data/drinks.csv', 'rb') as csvfile:
    drinks = csv.DictReader(csvfile)
    dictbeers = [int(row['beer_servings']) for row in drinks]

print "Bonus 2a - The list representing the data for the beer_servings column is as follows:"
print dictbeers
print
print "Bonus 2b - The list has", len(dictbeers), "items."
print

'''
PART 3:
Create separate lists of NA and EU beer servings: 'NA_beers', 'EU_beers'
Hint: you can use a list comprehension with a condition
Expected output:
    NA_beers == [102, 122, ..., 197, 249]
    len(NA_beers) == 23
    EU_beers == [89, 245, ..., 206, 219]
    len(EU_beers) == 45
'''


dict_NA_beers = []
dict_EU_beers = []

with open('data/drinks.csv', 'rb') as csvfile:
    drinks = csv.DictReader(csvfile)

    for drink in drinks:
        if drink['continent'] == 'NA':
            dict_NA_beers.append(drink['beer_servings'])
        if drink['continent'] == 'EU':
            dict_EU_beers.append(drink['beer_servings'])

print "Bonus 3a - The list of NA beer servings is as follows:"
print dict_NA_beers
print
print "Bonus 3b - The NA beers servings list has", len(dict_NA_beers), "items."
print
print "Bonus 3c - The list of EU beer servings is as follows:"
print dict_EU_beers
print 
print "Bonus 3d - The EU beers servings list has", len(dict_EU_beers), "items."
print
print "And that's all I have for the files and weather lab, Misrab!"