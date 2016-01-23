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
with open('../data/drinks.csv', 'rU') as f:
    header = csv.reader(f).next()
    data = [row for row in csv.reader(f)]


'''
PART 2:
Isolate the beer_servings column in a list of integers called 'beers'
Hint: you can use a list comprehension to do this in one line
Expected output:
    beers == [0, 89, ..., 32, 64]
    len(beers) == 193
'''
beers = [beers[1] for beers in data]


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
NA_beers = [beers[1] for beers in data if beers[5] == 'NA']
EU_beers = [beers[1] for beers in data if beers[5] == 'EU']


'''
PART 4:
Calculate the average NA and EU beer servings to 2 decimals: 'NA_avg', 'EU_avg'
Hint: don't forget about data types!
Expected output:
    NA_avg == 145.43
    EU_avg == 193.78
'''
NA_avg = round(sum(NA_beers)/float(len(NA_beers)), 2)
EU_avg = round(sum(EU_beers)/float(len(EU_beers)), 2)


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
output = [['continent', 'avg_beer'], ['NA', NA_avg], ['EU', EU_avg]]
with open('avg_beer.csv', 'wb') as f:
    csv.writer(f).writerows(output)


'''
Part 6:
Use the requests module to pull in weather data for any city
Hint: you can use Istanbul from the other code file but you can search
for cities at http://openweathermap.org/find

Create a dates list that stores the date of each datapoint as well as
temperature and humidity

You've already seen this code!
'''
#for St. Petersburg, Russia
import requests
api_endpoint = 'http://api.openweathermap.org/data/2.5/forecast/city'
params = {}
params['id'] = '498817'
params['units'] = 'metric'
params['APPID'] = '80575a3090bddc3ce9f363d40cee36c2'
request = requests.get(api_endpoint, params = params)

data = request.json()

weather_data = data['list']

temperatures = [data_point['main']['temp'] for data_point in weather_data]
humidity = [data_point['main']['humidity'] for data_point in weather_data]

dates = [data_point['dt'] for data_point in weather_data]

from datetime import datetime
dates = [datetime.fromtimestamp(epoch) for epoch in dates]

'''
Part 7
Create a list of the pressure measurements and plot it against dates
'''
pressure = [data_point['main']['pressure'] for data_point in weather_data]



'''
Part 8
Make a scatter plot plotting pressure against temperature and humidity
'''
import matplotlib.pyplot as plt
%matplotlib inline

plt.scatter(temperatures, humidity, pressure)

#this plot clearly shows a relationship between temperature and humidity,
#temperatures below -25 normally are dry - humidity is lower than 60 pct

plt.scatter(pressure, temperatures)

#clearly higher pressure for lower temperatures
# as St Petersburg is on the Baltic sea,
# winter temperatures are warmer when there is a humid depression coming from the sea
# winter is cold when ait comes from dry anti-cyclones from Siberia / Arctic





'''
BONUS:
Learn csv.DictReader() and use it to redo Parts 1, 2, and 3.
'''
