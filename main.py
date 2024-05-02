import os
import requests
from datetime import datetime


API_ID = os.environ["API_ID"]
API_KEY = os.environ["API_KEY"]
date = datetime.now()
new_date = date.strftime("%d/%m/%Y")
new_time = date.strftime("%H:%M:%S")
# print(new_date)

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

user_input = input("Tell me what exercises you did: ")
weight_kg = 74
height_cm = 175
# weight_check = input(f"Are you still {weight_kg}kg ? (Type 'yes' or 'no'): ").lower()
# if weight_check == "no":
#     new_weight = float(input("Enter current weight: "))
#     weight_kg = new_weight

parameters = {
    "query": user_input,
    "weight_kg": weight_kg,
    "height_cm": height_cm
}

header = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=header)
response.raise_for_status()
response_text = response.json()
# print(response_text)

new_response_list = [value for (key, value) in response_text.items()]
# print(new_response_list)
time_duration = int(new_response_list[0][0]["duration_min"])
# print(time_duration)
exercise_name = (new_response_list[0][0]["name"]).title()
# print(exercise_name)
calories_burnt = new_response_list[0][0]["nf_calories"]


### Sheety API
B_TOKEN = os.environ["B_TOKEN"]
SHEETY_POST_ENDPOINT = os.environ["SHEETY_POST_ENDPOINT"]

JSON_file = {
  "workout": {
      "date": new_date,
      "time": new_time,
      "exercise": exercise_name,
      "duration": time_duration,
      "calories": calories_burnt,
  }
}

sheety_header = {
  "Authorization": B_TOKEN,
}

sheety_response = requests.post(url=SHEETY_POST_ENDPOINT, json=JSON_file, headers=sheety_header)
# print(sheety_response.text)