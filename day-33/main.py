## API Request ####
import requests

MY_Lat = 51.507351
MY_Long = -0.127758

params = {
    "lat": MY_Lat,
    "long": MY_Long}


response = requests.get("https://api.sunrise-sunset.org/json", params=params)
response.raise_for_status()

# response = requests.get(url="http://api.open-notify.org/iss-now.json")

# # prints the response code
# # print(response.status_code)

# # catching errors
# response.raise_for_status()

# # getting the data

# data = response.json()
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
# print(longitude)

# iss_pos = (longitude, latitude)
# print(iss_pos)
# # Response code and meaning
# 100 and something = hold on
# 200 and something = successful
# 300 and something = You don't have permission to view the data
# 400 and something = You messed up, and didn't spell something right
# 500 and something = The server messed up - like the server being down
# for more indept view link below 👇
# https://www.webfx.com/web-development/glossary/http-status-codes/
