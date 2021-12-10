from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.


data_manager = DataManager()
notification_manager = NotificationManager()
sheet_data = data_manager.get_flight_data(call_sheety=False)
# pprint(sheet_data)

flight_search = FlightSearch()
# add iata codes to google spreadsheet
if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.return_iata(row["city"])
    data_manager.flight_data = sheet_data
    # print(f"sheet_data:\n {sheet_data}")
    # data_manager.put_flight_data()
# get flight prices based on city names from kiwi

for row in sheet_data:
    all_flights = flight_search.find_cheap_flights(row["iataCode"])
    flight_data = FlightData(all_flights)
    flight_data.display_flights()
    if row["lowestPrice"] > all_flights["data"][0]["price"]:
        notification_manager.send_text(all_flights["data"][0])









