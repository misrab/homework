'''Nelson Lau GA Data Science Lesson 01 REQUIRED HW'''

import csv

print "\n---PART 1---"
data_folder = 'C:\\Users\\Nelson\\SG_DAT1\\data\\'

with open('%sdrinks.csv' % data_folder) as f:
    reader = csv.reader(f)
    header = next(reader)
    print header
    data = []
    for row in reader:
        data.append(row)


print "\n---PART 2---"
beers = [int(row[1]) for row in data]
print "beers == ", beers
print "len(beers) == ", len(beers)


print "\n---PART 3---"
NA_beers = [int(row[1]) for row in data if row[5].upper() == 'NA']
print "NA_beers == ", NA_beers
print "len(NA_beers) == ", len(NA_beers)

EU_beers = [int(row[1]) for row in data if row[5].upper() == 'EU']
print "EU_beers == ", EU_beers
print "len(EU_beers) == ", len(EU_beers)


print "\n---PART 4---"
NA_avg = round(float(sum(NA_beers))/len(NA_beers),2)
print "NA_avg == ", NA_avg

EU_avg = round(float(sum(EU_beers))/len(EU_beers),2)
print "EU_avg == ", EU_avg


print "\n---PART 5---"
avg_dict = {"NA":NA_avg, "EU":EU_avg}
output_folder = 'C:\\Users\\Nelson\\homework\\NelsonLau\\01\\'
outputfile_name = 'avg_beer.csv'
outputfile_path = output_folder + outputfile_name
with open(outputfile_path,'wb') as outputfile:
    outputwriter = csv.writer(outputfile)
    outputwriter.writerow(['continent','avg_beer'])
    for continent in avg_dict:
        outputwriter.writerow([continent,avg_dict[continent]])
print "wrote output to %s" % outputfile_path

print "\n---PART 6---"
import requests

api_endpoint = 'http://api.openweathermap.org/data/2.5/forecast/city'
params = {}
params['id'] = 2158177 #Melbourne
params['units'] = 'metric'
params['APPID'] = '80575a3090bddc3ce9f363d40cee36c2'
request = requests.get(api_endpoint, params = params)

data = request.json()
city_data = data['city']
city_name = city_data['name']
country_code = city_data['country']
lat = city_data['coord']['lat']
lon = city_data['coord']['lon']
print "Working on %s in %s (lat %s and lon %s)" % (city_name, country_code, lat, lon)

weather_data = data['list']
from datetime import datetime
format_string = '%Y-%m-%d %H:%M:%S'
dates = [datetime.strptime(row['dt_txt'], format_string) for row in weather_data]
temperatures = [row['main']['temp'] for row in weather_data]
humidities = [row['main']['humidity'] for row in weather_data]
for data_row in zip(dates,temperatures,humidities):
    print data_row


print "\n---PART 7---"
import matplotlib.pyplot as plt

pressures = [row['main']['pressure'] for row in weather_data]
plt.plot(dates,pressures)
plt.xlabel("Time")
plt.ylabel("Pressure in hPa")
plt.title("Pressure in Melbourne")
plt.show()


print "\n---PART 8---"
fig, ax1 = plt.subplots()
temp_scatter = ax1.scatter(pressures,temperatures, label='Temperature')
ax1.set_xlabel("Pressure in hPa")
ax1.set_ylabel("Temperature in Celsius")
ax2 = ax1.twinx()
pres_scatter = ax2.scatter(pressures,humidities, marker='x', color='r', label='Humidity')
ax2.set_ylabel("Humidity in %")
plt.legend(handles = [temp_scatter, pres_scatter])
plt.title("Pressure vs Temperature and Humidity in Melbourne")
plt.show()


print "\n---BONUS: PART 1---"
data_folder = 'C:\\Users\\Nelson\\SG_DAT1\\data\\'

with open('%sdrinks.csv' % data_folder) as f:
    reader = csv.DictReader(f)
    bonus_header = reader.fieldnames
    print bonus_header
    bonus_data = []
    for row in reader:
        bonus_data.append(row)

print "\n---BONUS PART 2---"
bonus_beers = [int(row['beer_servings']) for row in bonus_data]
print "beers == ", bonus_beers
print "len(beers) == ", len(bonus_beers)


print "\n---BONUS PART 3---"
bonus_NA_beers = [int(row['beer_servings']) for row in bonus_data if row['continent'].upper() == 'NA']
print "NA_beers == ", bonus_NA_beers
print "len(NA_beers) == ", len(bonus_NA_beers)

bonus_EU_beers = [int(row['beer_servings']) for row in bonus_data if row['continent'].upper() == 'EU']
print "EU_beers == ", bonus_EU_beers
print "len(EU_beers) == ", len(bonus_EU_beers)