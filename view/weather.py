import requests
import os
from _datetime import datetime

def getWeather(city, country_code):
    query = {'q': city + "," + country_code, 'units': 'imperial', 'appid': '9db10307657b0ff8224b0da642ac57f7'}
    url = 'http://api.openweathermap.org/data/2.5/forecast'
    try:
        data = requests.get(url, params=query).json()
        forecast_items = data['list']

        for forecast in forecast_items:
            timestamp = forecast['dt']
            date = datetime.fromtimestamp(timestamp)
            # I choose to convert the timestamp in to a datetime
            # to get a local Minneapolis time, my program is currently built
            # to be used in this area for educational purposed and not deployed to others around the world yet
            temp = forecast['main']['temp']
            description = forecast['weather'][0]['description']
            wind_speed = forecast['wind']['speed']

            city = city.capitalize()
            print(
                f'At {date} in {city} the temp is {temp:.2f}F. \n and {description} with a wind speed of {wind_speed:.1f}mph')

    except:
        print("Please enter a valid city/country code")
        getWeather()




