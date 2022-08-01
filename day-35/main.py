#------- Weather Checker App----------#
import requests
# working with enviroment variables
import os
# from twilio.rest import client
API_KEY = os.getenv("API_KEY")
account_sid = ""
auth_token = ""

params = {
    "lat": 41.053429,
    "long": -73.538734,
    "appid": API_KEY}

# creating a fetch request
response = requests.get(
    "https://api.openweathermap.org/data/3.0/onecall?", params=params)
# checking for any errors
response.raise_for_status()
weather_data = response.json()
# slicing the data
weather_slice = weather_data["hourly"][:12]
# print(weather_data["hourly"][0]["weather"][0]["id"])

# print(weather_slice)
# looping through the weather and getting the values under the key weather

will_rain = False
for hour_data in weather_slice:
    # gettting each of the id
    code = int(hour_data["weather"][0]["id"])
    # if the code is less than 700 then it is raining
    if code < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella")
    # # client = Client(account_sid, auth_token)
    # message = client.messages \
    #     .create(
    #         body="",
    #         from="",
    #         to=""
    #     )
