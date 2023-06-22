# Task 1

import requests

url_1 = 'https://uk.wikipedia.org/robots.txt'
url_2 = 'https://twitter.com/robots.txt'


rez_1 = requests.get(url_1)
rez_2 = requests.get(url_2)

if rez_1.status_code:
    with open("robots_wiki.txt", "wb") as file_1:
        file_1.write(rez_1.content)
        print("You are legendary downloader :)")
else:
    print('somthing wrong')

if rez_2.status_code:
    with open("robots_twit.txt", "wb") as file_2:
        file_2.write(rez_1.content)
        print("You are legendary downloader twice:)")
else:
    print('Somthing went wrong')


# Task 3

import requests


def weather_app(city_name):

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=dbf6455ad98e3999bfaead3775d141eb&units=metric'

    resp = requests.get(url)

    if resp.status_code == 404:
        return 'Сity not found or check what you wrote :) '

    if resp.status_code:
        rez = resp.json()

        temperature = rez['main']['temp']
        feels = rez['main']['feels_like']
        max_temp = rez['main']['temp_max']
        wind_speed = rez['wind']['speed']
        sky_status = rez['weather'][0]['description']
        # print(rez)
        return (f'\n Temperature: {temperature}°C\n Feels like: {feels}°C\n The max temperature during the day: {max_temp}°C\n '
              f'The speed of the wind : {wind_speed}m/c\n The sky status: {sky_status}\n')
    else:
        print('Somthing went wrong')


if __name__ == '__main__':
    city_name = input('select the city for the Weather info for the present day: ')
    print(weather_app(city_name))
