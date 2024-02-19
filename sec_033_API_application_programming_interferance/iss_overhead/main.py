import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 47 # Your latitude
MY_LONG = -147 # Your longitude

SENDER_EMAIL = "random_test@gmail.com"
SENDER_PASSWORD = "generated_password"          # this password is genreated after enabling 2 steps verification -> generate app password for gmail account
SMTP_SERVER = 'smtp.gmail.com' 
RECIPIENT_EMAIL = 'random_test@yahoo.com'



#Your position is within +5 or -5 degrees of the ISS position.
def iss_position_check():
    global iss_longitude, iss_latitude
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])  
      
    if (MY_LAT - 5 <= iss_latitude <= MY_LAT + 5) and (MY_LONG - 5 <= iss_longitude <= MY_LONG + 5):
        return True
    else:
        return False
    

def night_check():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour
    
    if sunset <= time_now <= 24 or 0 <= time_now <= sunrise:
        return True
    else:
        return False





iss_longitude = None
iss_latitude = None

while True:
    time.sleep(60) # delay
    if iss_position_check() and night_check(): 
        with smtplib.SMTP(SMTP_SERVER) as connection:
            connection.starttls()
            connection.login(user=SENDER_EMAIL, password=SENDER_PASSWORD)
            message_body=f"""
            You can now observer an ISS solar station.
            
            Its current position is:
            Longitude: {iss_longitude}
            Latitude: {iss_latitude}
            """
            connection.sendmail(
                from_addr=SENDER_EMAIL,
                to_addrs=RECIPIENT_EMAIL,
                msg=f"Subject: ISS information\n\n{message_body}"
            )





