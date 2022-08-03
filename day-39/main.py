# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
import flight_search


data_manager = DataManager()
flightSearch = flight_search.FlightSearch()
sheet_data = data_manager.get_data()
# changing the data
new = flightSearch.search(sheet_data)
# updated_sheet = data_manager.updated(sheet_data)
