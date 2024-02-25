import requests
import os
from twilio.rest import Client

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = os.environ.get("OMW_API_KEY")
AUTH_TOKEN = os.environ.get("TWILLIO_AUTH_TOKEN") 
ACCOUNT_SID = os.environ.get("TWILLIO_ACCOUNT_SID")
MY_LAT = 49.1229
MY_LONG= 18.4405

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "cnt": 4,
}

response = requests.get(url=OWM_ENDPOINT , params=parameters)
response.raise_for_status()
weather_data = response.json()
rain_possibility = []

for time_stamp in weather_data["list"]:
    rain_possibility.append(time_stamp["weather"][0]["id"] < 700)
    
if True in rain_possibility:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages \
        .create(
            body = "Bring an umbrella. It will rain today.",
            from_ = "+13253134794",
            to = os.environ.get("MY_NUMBER")
    )
    print(message.status)
