'''
Lab: Reading and Writing Files in Python
'''

'''
PART 1:
Read in drinks.csv
Store the header in a list called 'header'
Store the data in a list of lists called 'data'
Hint: you've already seen this code!
'''
import csv
with open('../data/drinks.csv', 'rU') as drinkfile:
    reader = csv.reader(drinkfile)
    header = reader.next()
    data = [row for row in reader]
print header
'''
PART 2:
Isolate the beer_servings column in a list of integers called 'beers'
Hint: you can use a list comprehension to do this in one line
Expected output:
    beers == [0, 89, ..., 32, 64]
    len(beers) == 193
'''
beers = [row[1] for row in data]
print len(beers)

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
NA_beers = [float(row[1]) for row in data if row[5] == 'NA']
EU_beers = [float(row[1]) for row in data if row[5] == 'EU']
print len(NA_beers)
print len(EU_beers)
'''
PART 4:
Calculate the average NA and EU beer servings to 2 decimals: 'NA_avg', 'EU_avg'
Hint: don't forget about data types!
Expected output:
    NA_avg == 145.43
    EU_avg == 193.78
'''

NA_avg = sum(NA_beers)/len(NA_beers)
EU_avg = sum(EU_beers)/len(EU_beers)
print "%.2f" % NA_avg
print "%.2f" % EU_avg

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
with open('avg_beer.csv', 'wb') as avg_beer_file:
    beer_writer = csv.writer(avg_beer_file, delimiter=",")
    beer_writer.writerow(['continent', 'avg_beer'])
    beer_writer.writerow(['NA', "%.2f" % NA_avg])
    beer_writer.writerow(['EU', "%.2f" % EU_avg])

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

params = {
    "APPID" : "fab51159f54f45dbd3c398613c7736de",
    "q" : "singapore",
    "units": "metric"
}
r = requests.get("http://api.openweathermap.org/data/2.5/forecast", params=params)

print r.status_code

sg_data = r.json()
from datetime import datetime
dates = [ datetime.fromtimestamp(day["dt"]) for day in sg_data["list"]]

temp = [ day["main"]["temp"] for day in sg_data["list"]]
humidity = [ day["main"]["humidity"] for day in sg_data["list"]]

'''
Part 7
Create a list of the pressure measurements and plot it against dates
'''

pressures = [ day["main"]["pressure"] for day in sg_data["list"]]

import matplotlib.pyplot as plt

plt.plot(dates, pressures)
plt.ylabel('Pressure')
plt.xlabel('Date')
plt.show()

'''
Part 8
Make a scatter plot plotting pressure against temperature and humidity
'''

plt.scatter(pressures, temp, c=humidity, alpha=0.5)
plt.show()



'''
BONUS:
Learn csv.DictReader() and use it to redo Parts 1, 2, and 3.
'''