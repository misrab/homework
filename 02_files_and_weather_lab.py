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

with open('c:\mystuff\homework', 'rU') as f:
        header = csv.reader(f).next()
        data = [row for row in csv.reader(f)]
print header
print data
'''
PART 2:
Isolate the beer_servings column in a list of integers called 'beers'
Hint: you can use a list comprehension to do this in one line
Expected output:
    beers == [0, 89, ..., 32, 64]
    len(beers) == 193
'''
beers = [d[1] for d in data]
print beers

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
NA_beers = [float(d[1]) for d in data if d[5] == 'NA']
EU_beers = [float(d[1]) for d in data if d[5] == 'EU']
print NA_beers
len(NA_beers)
print EU_beers
len(EU_beers)

'''
PART 4:
Calculate the average NA and EU beer servings to 2 decimals: 'NA_avg', 'EU_avg'
Hint: don't forget about data types!
Expected output:
    NA_avg == 145.43
    EU_avg == 193.78
'''
NA_avg = sum(NA_beers) / len(NA_beers)
print NA_avg
EU_avg = sum(EU_beers) / len(EU_beers)
print EU_avg


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


'''
Part 6:
Use the requests module to pull in weather data for any city
Hint: you can use Istanbul from the other code file but you can search
for cities at http://openweathermap.org/find

Create a dates list that stores the date of each datapoint as well as
temperature and humidity

You've already seen this code!
'''



'''
Part 7
Create a list of the pressure measurements and plot it against dates
'''




'''
Part 8
Make a scatter plot plotting pressure against temperature and humidity
'''





'''
BONUS:
Learn csv.DictReader() and use it to redo Parts 1, 2, and 3.
'''
