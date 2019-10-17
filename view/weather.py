import requests
import os
from _datetime import datetime

def getWeather(city, country_code):
    query = {'q': city + "," + country_code, 'units': 'imperial', 'appid': '9db10307657b0ff8224b0da642ac57f7'}
    url = 'http://api.openweathermap.org/data/2.5/forecast'
    try:
        data = requests.get(url, params=query).json()
        forecast_items = data['list']
        printcount = 0
        values = [0,8,16,24,32]
        daycount = 1
        print(f"\n5 Day Forecast for {city}\n")
        for forecast in forecast_items:
            if (printcount in values):
                timestamp = forecast['dt']
                date = datetime.fromtimestamp(timestamp)
                weather_description = forecast['weather'][0]['description']
                temp_f = forecast['main']['temp']
                wind_speed = forecast['wind']['speed']
                if (daycount) == 1:
                    print("Today")
                else:
                    print(f'Day{daycount}')
                print(f'Weather description: {weather_description}')
                print(f'Temperature: {temp_f:.2f} F')
                print(f'Wind speed: {wind_speed} \n')
                daycount += 1

            printcount += 1


        return True

    except:
        print("Please enter a valid city/country code\n")
        return False







