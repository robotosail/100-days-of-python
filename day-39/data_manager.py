import requests

endpoint = 'https://api.sheety.co/cb2f6702bedf235604a98edb6eee9179/flightsearch/prices'


class DataManager:
    def get_data(self) -> None:
        # getting the data
        response = requests.get(url=endpoint)
        response.raise_for_status()
        result = response.json()
        return result

    def updated(self, data):
        # looping through each value under the prices key word
        for info in data["prices"]:
            # setting a new parameter
            params = {
                "price": {
                    "iataCode": info["iataCode"]
                }
            }
            # sending a put request to updated the data
            response = requests.put(
                url=f"{endpoint}/{info['id']}", json=params)
            result = response.json()
        print(result)
