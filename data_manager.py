import os
from dotenv import load_dotenv
from requests import request


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        load_dotenv(r"C:\Users\watsorob\Google Drive\Programming\Python\EnvironmentVariables\.env.txt")
        self.flight_token = os.getenv("SHEETY_KEY")
        self.flight_endpoint = os.getenv("FLIGHT_ENDPOINT")
        self.headers = {
            "Authorization": self.flight_token,
        }

    def get_flight_data(self):
        """ Get flight info from spreadsheet """
        flight_response = request(url=self.flight_endpoint, method="GET", headers=self.headers)
        flight_data = flight_response.json()
        return flight_data["prices"]

    def put_flight_data(self, id):
        flight_put = request(url=self.flight_endpoint, method="PUT", headers=self.headers)
        print(flight_put.text)