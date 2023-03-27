import requests

city = 'Kyiv'
url = f'https://open-meteo.com/en/docs#latitude=50.45&longitude=30.52/v1/forecast'

response = requests.get(url)
print(response)