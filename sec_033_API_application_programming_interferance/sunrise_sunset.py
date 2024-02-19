import requests
import datetime as dt

# https://www.latlong.net

PARAMETERS = {
    "lat": 49.115650,
    "lng": 18.442141,
    "formatted": 0,
}



response = requests.get(url="https://api.sunrise-sunset.org/json", params=PARAMETERS)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

time_now = dt.datetime.now().hour

print(sunrise)
print(time_now)