import requests


city_name = "Kyiv"
url = f"https://open-meteo.com/v1/geo?q={city_name}"
response = requests.get(url)
#latitude = response['data'][0]['latitude']
#longitude = response['data'][0]['longitude']
print(response)

#url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}"
#response = requests.get(url).json()
#weather_data = response['current_weather']

#print(f"Поточна погода у місті {city_name}:")
#print(f"Температура: {weather_data['temperature']}°C")
#print(f"Вітер: {weather_data['wind']['speed']} м/с")
#print(f"Вологість: {weather_data['humidity']}%")
