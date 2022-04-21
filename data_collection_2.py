# 2. Получение погоды с http://api.openweathermap.org

import requests

identifier = '88e2422f348025ed1e3a5dc46d34f997'


def get_weather():
    city = input("Enter city name: ")
    res = requests.get("http://api.openweathermap.org/geo/1.0/direct",
                       params={'q': city, 'limit': 1, 'appid': identifier})

    data = res.json()
    lat = data[0]['lat']
    lon = data[0]['lon']
    print("name:", data[0]['name'])
    print("lat:", lat)
    print("lon:", lon)

    res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                       params={'lat': lat, 'lon': lon, 'appid': identifier})
    data = res.json()

    print("description:", data['weather'][0]['description'])
    print("temp:", data['main']['temp'])
    print('\n')


while True:
    get_weather()
