from twilio.rest import Client
import os

# twillio api
AUTH_TOKEN = os.environ.get("TWILLIO_AUTH_TOKEN") 
ACCOUNT_SID = os.environ.get("TWILLIO_ACCOUNT_SID")

class NotificationManager:
    
    def __init__(self):
        self.client = Client(ACCOUNT_SID, AUTH_TOKEN)
        
    def send_a_message(self, data):
        price = data[0]["price"]
        fly_from_city = data[0]["cityFrom"]
        fly_from_airport = data[0]["flyFrom"]
        fly_to_city = data[0]["cityTo"]
        fly_to_airport = data[0]["flyTo"]
        departure_date = data[0]["route"][0]["local_departure"].split("T")[0]
        arrival_date = data[0]["route"][0]["local_arrival"].split("T")[0]
     
        message = self.client.messages \
                .create(
                    body = f"Low price alert! Only €{price} fly from {fly_from_city}-{fly_from_airport} to {fly_to_city}-{fly_to_airport}, from {departure_date} to {arrival_date}.",
                    from_ = "+13253134794",
                    to = os.environ.get("MY_NUMBER")
                )
        print(message.sid)

    