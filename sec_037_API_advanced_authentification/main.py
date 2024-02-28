import requests
import os
from datetime import datetime

# PIXELA api doc https://docs.pixe.la

TOKEN = os.environ.get("PIXELA_TOKEN")
USERNAME = "springtheory"


# ------------------ creating an user account on Pixela ---------------------#
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# -------------------- creating a new graph on Pixela ----------------------#
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_params = {
    "id": "graph1",
    "name": "Coding Time",
    "unit": "Hours",
    "type": "float",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)
# result: https://pixe.la/v1/users/springtheory/graphs/graph1.html

# ----------------------- creating a new pixel ----------------------------#
today = datetime.now()

GRAPH_ID = "graph1"
create_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_params = {
    # "date": today.strftime("%Y%m%d"),
    "date": "20240214",
    "quantity": "2.5",
}

response = requests.post(url=create_pixel_endpoint, json=pixel_params, headers=headers)
print(response.text)


# ----------------------- update the pixel ----------------------------#
updating_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20240228"
updating_pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "3",
}

# response = requests.put(url=updating_endpoint, json=updating_pixel_params, headers=headers)
# print(response.text)


# ----------------------- update the pixel ----------------------------#
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20240228"

# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)