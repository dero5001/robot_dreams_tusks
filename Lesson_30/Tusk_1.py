import requests
import random


websites = ['google.com', 'facebook.com', 'twitter.com', 'amazon.com', 'apple.com']
random_website = random.choice(websites)
response = requests.get(f'https://{random_website}')

print(f'Website: {random_website}')
print(f'Status code: {response.status_code}')
print(f'HTML length: {len(response.text)}')
