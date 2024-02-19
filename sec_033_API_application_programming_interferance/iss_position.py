import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()  # checking for possible errors read documentation for request module

data = response.json()["iss_position"]
longitude = response.json()["iss_position"]["longitude"]
latitude = response.json()["iss_position"]["latitude"]

print(data)

# you can check position via https://www.latlong.net
