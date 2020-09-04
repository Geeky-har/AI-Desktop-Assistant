import json
import requests

api_key = '4a792593417d8ab5d8a771fb1674173d'

base_url = "http://api.openweathermap.org/data/2.5/weather?"

city_name = 'Delhi'

complete_url = base_url + "appid=" + api_key + "&q=" + city_name 

response = requests.get(complete_url)

x = response.json()

y = x['main']

def temp():

    return (round((int(y['temp']) - 273.15), 1))

def humid():
    return (y['humidity'])

def wind():
    return round(int((x['wind']['speed'])) * 1.6, 1)

if __name__ == "__main__":
    print('Temp is: ', end = '')
    temp()
    humid()
    wind()