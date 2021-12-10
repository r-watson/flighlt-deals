import os
from dotenv import load_dotenv
import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        load_dotenv(r"G:\My Drive\Programming\Python\EnvironmentVariables\.env.txt")
        self.flight_token = os.getenv("SHEETY_KEY")
        self.flight_endpoint = os.getenv("FLIGHT_ENDPOINT")
        self.headers = {
            "Authorization": self.flight_token,
        }
        self.flight_data = {}

    def get_flight_data(self, call_sheety: bool = False) -> list:
        """ Get flight info from spreadsheet. Test with local JSON. """
        if call_sheety:
            flight_response = requests.get(url=self.flight_endpoint, headers=self.headers)
            flight_response.raise_for_status()
            print(flight_response.text)
            data = flight_response.json()
            self.flight_data = data["prices"]
        else:
            self.flight_data = [{"city": "Paris", "iataCode": "PAR", "lowestPrice": 54, "id": 2},
                    {"city": "Berlin", "iataCode": "BER", "lowestPrice": 42, "id": 3},
                    {"city": "Tokyo", "iataCode": "TYO", "lowestPrice": 485, "id": 4},
                    {"city": "Sydney", "iataCode": "SYD", "lowestPrice": 551, "id": 5},
                    {"city": "Istanbul", "iataCode": "IST", "lowestPrice": 95, "id": 6},
                    {"city": "Kuala Lumpur", "iataCode": "KUL", "lowestPrice": 414, "id": 7},
                    {"city": "New York", "iataCode": "NYC", "lowestPrice": 240, "id": 8},
                    {"city": "San Francisco", "iataCode": "SFO", "lowestPrice": 260, "id": 9},
                    {"city": "Cape Town", "iataCode": "CPT", "lowestPrice": 378, "id": 10},
                    {"city": "Bali", "iataCode": "DPS", "lowestPrice": 501, "id": 11}]
        return self.flight_data

    def put_flight_data(self):
        """ send flight data to Google spreadsheet """
        for city in self.flight_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"],
                }
            }
            flight_put = requests.put(url=f"{self.flight_endpoint}/{city['id']}", json=new_data, headers=self.headers)
            flight_put.raise_for_status()
            print(flight_put.text)