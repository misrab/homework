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
with open(filename, 'rb') as csvf:
	myReader = csv.reader(csvf)
	header = myReader.next()
	data = [row for row in myReader]
		

'''
PART 2:
Isolate the beer_servings column in a list of integers called 'beers'
Hint: you can use a list comprehension to do this in one line
Expected output:
    beers == [0, 89, ..., 32, 64]
    len(beers) == 193
'''

beers = [x[header.index('beer_servings')] for x in data ]


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

NA_beers = [val for idx, val in enumerate(beers) if liston[idx][header.index('continent')]=='NA']
EU_beers = [val for idx, val in enumerate(beers) if liston[idx][header.index('continent')]=='EU']

'''
PART 4:
Calculate the average NA and EU beer servings to 2 decimals: 'NA_avg', 'EU_avg'
Hint: don't forget about data types!
Expected output:
    NA_avg == 145.43
    EU_avg == 193.78
'''

import numpy
NA_avg = numpy.around(numpy.mean([int(x) for x in NA_beers]),decimals=2)
EU_avg = numpy.around(numpy.mean([int(x) for x in EU_beers]),decimals=2)

or
NA_avg = round(numpy.mean([int(x) for x in NA_beers]), 2)
EU_avg = round(numpy.mean([int(x) for x in EU_beers]), 2)


'''
I might have found some numpy bug for NA_avg. It happens only for NA_avg!
'''

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
output = [['continent','avg_beer'], ['NA','NA_avg'],['EU','EU_avg']]
with open('avg_beer.csv','wb') as csvwf:
	for row in output:
		csv.writer(csvwf).writerow(row)
	
	
'''
Addtional playing

Any list comprehension idea like bwlow which don't work?
cont_header = [i[header.index('continent')] for i in data if not (i[header.index('continent')] in cont_header]
beer_set_cont = [val for j in cont_header for idx, val in enumerate(beers) if liston[idx][header.index('continent')] == j]
'''
cont_header = []
for i in data:
	if not (i[header.index('continent')] in cont_header): cont_header.append(i[header.index('continent')])
beer_set_cont = []
for j in cont_header: beer_set_cont.append([val for idx, val in enumerate(beers) if liston[idx][header.index('continent')]==j])
beer_avg_allcont = [round(numpy.mean([int(x) for x in k]), 2) for k in beer_set_cont]

with open('avg_beer_all.csv', 'wb') as csvwf1:
	myWriter1 = csv.writer(csvwf1)
	myWriter1.writerow(['continent','avg_beer'])
	for id, v in enumerate(cont_header):
		myWriter1.writerow([v, beer_avg_allcont[id]])
		



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
api_endpoint = 'http://api.openweathermap.org/data/2.5/forecast/city'
params={}
params['id'] = '1850147' 
params['units'] = 'metric'
params['APPID'] = '80575a3090bddc3ce9f363d40cee36c2'
request = requests.get(api_endpoint, params = params)
data=request.json()
date=[i['dt_txt'] for i in data['list']]
temp=[i['main']['temp'] for i in data['list']]
hum=[i['main']['humidity'] for i in data['list']]

dates = [i['dt'] for i in data['list']]
dates = [datetime.fromtimestamp(epoch) for epoch in dates]

'''
Part 7
Create a list of the pressure measurements and plot it against dates
'''
press = [i['main']['pressure'] for i in data['list']]
import matplotlib.pyplot as plt
plt.xlabel("Time")
plt.ylabel("Pressure (hPa)")
plt.title("Pressure forecast for next 105 hrs in Tokyo")
plt.plot(dates, press)
plt.show()

'''
Part 8
Make a scatter plot plotting pressure against temperature and humidity
'''

plt.scatter(press, hum)
plt.show()

plt.scatter(press, temp)
plt.show()

'''
Playing:
plt.scatter([j.hour for j in dates], temp)
plt.scatter([j.day for j in dates], temp)
These show that temp correlates time of day, rather than date while
plt.scatter([j.hour for j in dates], press)
plt.scatter([j.day for j in dates], press)
show press correlates date
'''




'''
BONUS:
Learn csv.DictReader() and use it to redo Parts 1, 2, and 3.
'''