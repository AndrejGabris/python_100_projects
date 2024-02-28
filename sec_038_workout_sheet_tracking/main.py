import requests
import os
from datetime import datetime


NUTIX_API_KEY = os.environ.get("NUTRITIONIX_API_KEY", "Variable doesn't exists")
NUTIX_APP_ID = os.environ.get("NUTRITIONIX_APP_ID", "Variable doesn't exists")

default_endpoint = "https://trackapi.nutritionix.com"
user_input = input("Tell me which exercise you did: ")

exercise_parameters = {
    "query": user_input,
}

nutix_headers = {
    "x-app-id": NUTIX_APP_ID,
    "x-app-key": NUTIX_API_KEY,    
}

response = requests.post(url=f"{default_endpoint}/v2/natural/exercise", json=exercise_parameters, headers=nutix_headers)
response.raise_for_status()
output = response.json()

sheety_post_endpoint = "https://api.sheety.co/86c4c95cb8178445abacdc0922c67e65/myWorkouts/workouts"

SHEETY_TOKEN = os.environ.get("SHEETY_BEARER_KEY", "Variable doesn't exists")
headers = {
    "Authorization": f"Bearer {SHEETY_TOKEN}",
}

exercises = output["exercises"]
for exercise in exercises:
    today_date = datetime.now().strftime("%d/%m/%Y")
    today_time = datetime.now().strftime("%X")
    type_of_exercise = exercise["name"].title()
    duration = exercise["duration_min"]
    calories = exercise["nf_calories"]
    data = {
        "workout": {
            "date": today_date,
            "time": today_time,
            "exercise": type_of_exercise,
            "duration": duration,
            "calories": calories,
        }
    }
        
    response = requests.post(url=sheety_post_endpoint, json=data, headers=headers)
    print(response.text)