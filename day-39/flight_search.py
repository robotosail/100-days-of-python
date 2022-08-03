from os import pardir
import data_manager
import requests

url = "https://tequilla-api.kiwi.com/locations/query"
# API_KEY = "KefD5-cTjTvRK1zZrQ9zbGRS4302meP_"
API_KEY = "GWNyR5BSGiO9Q_zVTo7oPWzWhWehbMAi"


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def search(self, info: data_manager):
        self.info = info
        for i in self.info["prices"]:
            if i["iataCode"] == "":
                i["iataCode"] = "testing"
        print(self.info)

    def get_iatacode(self, data):
        header = {
            "apikey": API_KEY
        }
        for city in data["prices"]:
            params = {
                "term": city["city"]
            }
            response = requests.get(url=url, params=params, headers=header)
            print(response.text)
        return response.json()
