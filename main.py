from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch

#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.


data_manager = DataManager()
sheet_data = data_manager.get_flight_data(call_sheety=False)
pprint(sheet_data)

if sheet_data[0]["iataCode"] != "":
    flight_search = FlightSearch()
    for row in sheet_data:
        row["iataCode"] = flight_search.return_iata(row["city"])
        flight_search.find_cheap_flights(row["city"])
    print(f"sheet_data:\n {sheet_data}")

    data_manager.flight_data = sheet_data
    # data_manager.put_flight_data()





