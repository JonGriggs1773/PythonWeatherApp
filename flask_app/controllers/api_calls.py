from flask_app import app
from dotenv import load_dotenv
load_dotenv()
import requests
import pprint
import os
api_key = os.getenv("API_KEY")




def find_lat_and_long_by_city(city):
    geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={api_key}"
    return geo_url


def get_geo_by_city(city):
    url = find_lat_and_long_by_city(city)
    response = requests.get(url)
    return response


def configure_url(city):
    geo_response = get_geo_by_city("Leoma")
    geo_response = geo_response.json()
    print("LAT HERE-------------------")
    pprint.pp(geo_response)
    geo_response = geo_response[0]
    url = f"https://api.openweathermap.org/data/3.0/onecall?lat={geo_response['lat']}&lon={geo_response['lon']}&appid={api_key}"
    print("API URL HERE-------------------", url)
    return url 


def weather_api_call(city):
    url = configure_url(city)
    response = requests.get(url)
    response = response.json()
    print("Weather API Response Here-------------------------")
    print(response)
