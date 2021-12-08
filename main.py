from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch

#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.


data_manager = DataManager()
sheet_data = data_manager.get_flight_data()
pprint(sheet_data)

for row in sheet_data:
    iata_code = row["iataCode"]
    city = row["city"]
    id = row["id"]
    if iata_code == "":
        flight_out = FlightSearch(city)
        code_return = flight_out.return_iata()
        row.update({'iataCode': code_return})
        data_manager.put_flight_data(id)
print(sheet_data)




