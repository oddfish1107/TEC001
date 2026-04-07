import requests
city = input('Enter city: ')
weatherapi ='https://api.openweathermap.org/data/2.5/weather'
geocodeapi = 'http://api.openweathermap.org/geo/1.0/direct'
API_KEY = '1b7b23ab686f604761128500dbdbbf1a'
try:
    geocode = requests.get(geocodeapi, params={"q":city, "limit":1, "appid": API_KEY}).json()
    latitude = geocode[0]['lat']
    longitude = geocode[0]['lon']
    print(f'Latitude: {latitude}, Longitude: {longitude}')
    weather = requests.get(weatherapi, params={"lat":latitude, "lon":longitude, "units": "metric", "appid": API_KEY}).json()
    temperature = weather['main']['temp']
    print(f'Temperature: {temperature} C')

except requests.exceptions.RequestException as e:
    print(e)
