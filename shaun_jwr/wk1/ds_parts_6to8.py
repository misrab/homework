import requests
from datetime import datetime
import matplotlib.pyplot as plt

# number six

api_endpoint = 'http://api.openweathermap.org/data/2.5/forecast/city'

params = {}
params['id'] = '1853909'
params['units'] = 'metric'
params['APPID'] = '12a338f3bcde6588f0f745f91dc2c7a7'

request = requests.get(api_endpoint, params=params)

data = request.json()

print data['city']

weather_data = data['list']
temperatures = [data_point['main']['temp'] for data_point in weather_data]
humidity = [data_point['main']['humidity'] for data_point in weather_data]

dates = [data_point['dt'] for data_point in weather_data]
dates = [datetime.fromtimestamp(epoch) for epoch in dates]

# number seven

pressures = [data_point['main']['pressure'] for data_point in weather_data]

plt.xlabel("Time")
plt.ylabel("pressure")
plt.title("Pressure today in Osaka")
locs, labels = plt.xticks()
plt.plot(dates, pressures)
plt.show()

# number eight

plt.scatter(pressures, humidity, color="black", marker="^")

plt.show()
