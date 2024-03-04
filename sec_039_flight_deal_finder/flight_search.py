import os
import requests
import datetime as dt

TQ_API_KEY = os.environ.get("TEQUILA_API_KEY")
TQ_FLY_FROM = "VIE"

MIN_STAY_DAYS = dt.datetime.now() + dt.timedelta(days=1)
MAX_STAY_DAYS = dt.datetime.now() + dt.timedelta(days=180)

tq_header = {
    "apikey": TQ_API_KEY,
}

class FlightSearch:
        
    def find_IATA(self, city):
        parameters = {
            "term": city,
            "location_types": "city",
            "limit": 1,
        }
        
        output = requests.get(url=f"https://api.tequila.kiwi.com/locations/query", params=parameters, headers=tq_header)
        output.raise_for_status()
        data = output.json()
        iata_city = data["locations"][0]["code"]
        return iata_city

    def search_for_flight(self, destination):
             
        parameters = {
            "fly_from": TQ_FLY_FROM,
            "fly_to": destination["iataCode"],
            "date_from": str(MIN_STAY_DAYS.strftime("%d/%m/%Y")),
            "date_to": str(MAX_STAY_DAYS.strftime("%d/%m/%Y")),
            "sort": "price",
            "nights_in_dst_from": 6,
            "nights_in_dst_to": 28,
            "curr": "EUR",
            "price_to": int(destination["lowestPrice"]),
            "limit": 1,
        }
        
        output = requests.get(url=f"https://api.tequila.kiwi.com/v2/search", params=parameters, headers=tq_header)
        output.raise_for_status()
        data = output.json()["data"]
        return data
            
            
            
            