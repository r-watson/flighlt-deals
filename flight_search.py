import os
from dotenv import load_dotenv
import requests
import datetime
load_dotenv(r"G:\My Drive\Programming\Python\EnvironmentVariables\.env.txt")
API_URL = "https://tequila-api.kiwi.com"
HEADERS = {
    "apikey": os.getenv("TEQUILA_API"),
    "Content-Encoding": "gzip",
}


class FlightSearch():
    #This class is responsible for talking to the Flight Search API.

    def return_iata(self, city):
        query = {
            "term": city
        }
        request = requests.get(f"{API_URL}/locations/query", headers=HEADERS, params=query)
        print(request.text)
        request.raise_for_status()
        iata = request
        return iata

    def find_cheap_flights(self, city):
        tomorrow_get = datetime.date.today() + datetime.timedelta(days=1)
        tomorrow = tomorrow_get.strftime("%d/%m/%Y")
        plus_six_months_get = datetime.date.today() + datetime.timedelta(days=181)
        plus_six_months = plus_six_months_get.strftime("%d/%m/%Y")
        params = {
            "fly_from": "LON",
            "fly_to": city,
            "date_from": tomorrow,
            "date_to": plus_six_months,
            "max_stopovers": 0,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "curr": "GBP",
        }
        request = requests.get(f"{API_URL}/v2/search", params=params, headers=HEADERS)
        print(request.text)
        request.raise_for_status()
        print(request.json())