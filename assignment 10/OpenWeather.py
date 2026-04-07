import requests
print("Ha Noi's Coordinate: 21.028511, 105.804817")
latitude = input("Enter latitude (e.g., 52.52, 21.028511): ") or "52.52"
longitude = input("Enter longitude (e.g., 13.41, 105.804817): ") or "13.41"
url ='https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m'
city_url = f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m'
try:
    response = requests.get(city_url)
    data = response.json()
    if response.status_code == 200:
        times = data['hourly']['time']
        temper = data['hourly']['temperature_2m']
        print(f'Coordinates: {latitude}: {longitude}')
        for i in range(5):
            formattime = times[i].replace('T', ' ')
            temp = temper[i]
            print(f'Time: {formattime}: Temp: {temp} °C')
        else:
            print('no data available')
except requests.exceptions.RequestException as e:
    print(e)
