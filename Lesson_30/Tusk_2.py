import requests


city_name = input('Введіть назву міста: ')
geo_url = f'https://geocoding-api.open-meteo.com/v1/search?name={city_name}'

res_geo = requests.get(geo_url).json()

if "results" in res_geo:
    data = res_geo["results"]
    longitude = data[0]['longitude']
    latitude = data[0]['latitude']

    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
    res = requests.get(url).json()
    print(res)
    curren_weather = res['current_weather']

    print(f'Поточна погода у місті {city_name}:')
    print(f'Температура: {curren_weather["temperature"]}°C')
    print(f'Швидкість вітру: {curren_weather["windspeed"]} м/с')

else:
    print('Таке місто не знайдено')



