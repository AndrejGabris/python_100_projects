#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from notification_manager import NotificationManager

data_manager = DataManager()
destinations = data_manager.create_destination()

for destination in destinations:
    from flight_search import FlightSearch
    flight_search = FlightSearch()
    if destination["iataCode"] == "":
        code = flight_search.find_IATA(destination["city"])
        destination["iataCode"] = code
        data_manager.destination_data = destinations
        data_manager.update_iata_code(destination)
    flight_search = FlightSearch()
    searched_flights = flight_search.search_for_flight(destination)
    if searched_flights != []:
        notification_manager = NotificationManager()
        notification_manager.send_a_message(searched_flights)
    else: 
        print("Price was set too low.")



