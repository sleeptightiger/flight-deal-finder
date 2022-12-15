#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from flight_search import FlightSearch
from data_manager import DataManager
import requests
from pprint import pprint

sheety_endpoint = "https://api.sheety.co/2da02e54e21dacd55c8528fd518405ba/flightDeals/prices"
sheety_header = {
    "Authorization": "Basic Z2Vycnltb3JhbGVzNzQxQGdtYWlsLmNvbTpyZWRTZWEyMg=="
}

response = requests.get(url=sheety_endpoint, headers=sheety_header)
sheet_data = response.json()['prices']

#check spreadsheet


#posts a lower price
for data in sheet_data:
    flight = FlightSearch(data)
    flight.flight_search()
    data_manager = DataManager(flight.flight_data, data)
    data_manager.post_prices()

