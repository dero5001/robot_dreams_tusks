import requests


city_name = input('Введіть назву міста: ')
geo_url = f'https://geocoding-api.open-meteo.com/v1/search?name={city_name}'

res_geo = requests.get(geo_url).json()
data = res_geo["results"]
longitude = data[0]['longitude']
latitude = data[0]['latitude']

url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
res = requests.get(url).json()
curren_weather = res['current_weather']

print(f'Поточна погода у місті {city_name}:')
print(f'Температура: {curren_weather["temperature"]}°C')
print(f'Швидкість вітру: {curren_weather["windspeed"]} м/с')

