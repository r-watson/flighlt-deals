class FlightData:
    #This class is responsible for structuring the flight data.
    # keys = dict_keys(['search_id', 'time', 'currency', 'fx_rate', 'data', 'search_params', 'all_airlines', 'all_stopover_airports', 'del', 'currency_rate', 'connections', 'refresh', 'ref_tasks', 'sort_version'])
    def __init__(self, all_flights):
        self.all_flights = all_flights["data"][0]
        self.formatted_flights = {}
        # print(self.all_flights)

    def display_flights(self):
        """ display resulsts of flight_search request """
        # for flight in range(len(self.all_flights)):
        formatted_flights = {
            "price": self.all_flights['price'],
            "departure_city": self.all_flights["cityFrom"],
            "dest_city": self.all_flights["cityTo"],
        }
            # print(formatted_flights)
            # formatted_flights = formatted_flights
        print(f"{formatted_flights['dest_city']}: {formatted_flights['price']}")
        # print(formatted_flights)



