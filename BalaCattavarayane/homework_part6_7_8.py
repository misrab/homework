import requests
import datetime
import matplotlib.pyplot as plt

#retreive weather data for city Pondicherry. India
r = requests.get('http://api.openweathermap.org/data/2.5/forecast/city?id=1259424&APPID=1a356081cea2e44548fc39c036355ef7')
#print r.text
jsonData = r.json()
weatherData = jsonData['list']

#print r.jsonData()
print weatherData[0]

temps = [data['main']['temp'] for data in weatherData]
print temps

humidity = [data['main']['humidity'] for data in weatherData]
print humidity

pressures = [data['main']['pressure'] for data in weatherData]
print pressures

#dates = [data['dt'] for data in weatherData]
#print dates
#plt.show()
#.strftime("%y-%m-%d-%H-%M")

dates = [data['dt'] for data in weatherData]
from datetime import datetime
dates = [datetime.fromtimestamp(epoch) for epoch in dates]

plt.plot(dates, pressures)
plt.scatter(dates, pressures)
plt.show()

plt.xlabel('Humidity') 
plt.ylabel('Temperature') 
plt.scatter(humidity, temps)
plt.show()
