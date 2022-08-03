# ----------- Workout tracker---------------##

import requests
from datetime import datetime
import os
# auth
APP_ID = "6a710630"
APP_KEY = "d244d8f26d47de1b3d901f4da4d8d2c8"
sheet_usrname = "cb2f6702bedf235604a98edb6eee9179"
sheet_project_name = "workoutTracking"
sheet_name = "workouts"
# url
url = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_url = "https://api.sheety.co/"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
    "Content-Type": "application/json"
}

params = {
    # getting the exercises done
    "query": input("What excersise did you do: "),
    "gender": "female",
    "weight_kg": 72.5,
    "height_cm": 167.64,
    "age": 30
}

# posting the data
response = requests.post(url=url, headers=headers, json=params)
# getting the response data back
result = response.json()
# formating the date
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

# looping each excersise and adding the required infromation to the data
for exercise in result["exercises"]:
    data = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "excersise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    # setting the authorization
    bearer_headers = {
        "Authorization": "Bearer hjvlkafmdsaolvm"
    }
    sheet_response = requests.post(
        url=f"{sheet_url}/{sheet_usrname}/{sheet_project_name}/{sheet_name}", json=data, headers=bearer_headers)
    print(sheet_response.text)
# print(data)
