import requests
import os

SH_API_KEY = os.environ.get("SHEETY_FLIGHT_SEARCH_BEARER_KEY")
auth_param = {
    "Authorization": f"Bearer {SH_API_KEY}"
}

class DataManager:
    def __init__(self):
        self.destination_data = {}
        
        
    def create_destination(self):
        sheety_get_endpoint = "https://api.sheety.co/86c4c95cb8178445abacdc0922c67e65/flightFinder/destinations"
        response = requests.get(url=sheety_get_endpoint, headers=auth_param)
        response.raise_for_status()
        output = response.json()
    
        self.destination_data = output["destinations"]
        return self.destination_data
    
    def update_iata_code(self, destination):
        iata_update = {
            "destination": {
                "iataCode": destination["iataCode"],
            }
        }

        sheety_put_endpoint = f"https://api.sheety.co/86c4c95cb8178445abacdc0922c67e65/flightFinder/destinations/{destination["id"]}"
        response = requests.put(url=sheety_put_endpoint, json=iata_update, headers=auth_param)
        response.raise_for_status()