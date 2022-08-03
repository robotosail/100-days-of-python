import requests
import datetime

USERNAME = "bave"
TOKEN = "121klafiohoi32joklsa"
pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_id = "graph14"
# params = {
#     "token": "121klafiohoi32joklsa",
#     "username": "bave",
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }

# # response = requests.post(url=pixela_endpoint, json=params)
# # print(response.text)

graph_param = {
    "id": graph_id,
    "name": "coding",
    "unit": "hours",
    "type": "float",
    "color": "sora"
}

# using request headers to decode the url
headers = {
    "X-USER-TOKEN": TOKEN
}

# requests.post(url=graph_endpoint, json=graph_param, headers=headers)

# getting todays date
date = datetime.datetime.now()

# day = date.day
# month = date.month
# year = date.year

# if day < 10:
#     day = f"0{day}"
# if month < 10:
#     month = f"0{month}"

# print(f"{year}{month}{day}")
print(date.strftime("%Y%m%d"))
# connecting to the graph endpoint
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_id}"
pixel_data = {
    "date": date.strftime("%Y%m%d"),
    "quantity": "1",
}

# response = requests.post(url=pixel_creation_endpoint,
#                          json=pixel_data, headers=headers)
# print(response.text)

update_endpoint = f"{pixela_endpoint}/bave/graphs/{graph_id}/{date.strftime('%Y%m%d`z')}"

new_pixel_data = {
    "quantity": "100"
}

# response = requests.put(url=update_endpoint,
#                         json=new_pixel_data, headers=headers)
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_id}/{date.strftime('%Y%m%d')}"
response = requests.delete(url=delete_endpoint, headers=headers)
