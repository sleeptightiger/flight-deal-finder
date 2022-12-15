import requests
from pprint import pprint
from flight_data import FlightData
from notification_manager import NotificationManager

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self, flight_data, row_data):
        self.flight_data = flight_data
        self.row_data = row_data
        self.sheety_endpoint = "https://api.sheety.co/2da02e54e21dacd55c8528fd518405ba/flightDeals/prices/"
        # self.sheet_data = sheet_data
        self.sheety_header = {
            "Authorization": "Basic Z2Vycnltb3JhbGVzNzQxQGdtYWlsLmNvbTpyZWRTZWEyMg=="
        }

        # self.post()

    # def post(self):
    #     for data in self.sheet_data:
    #         config = {
    #             "price": {
    #                 "iataCode": data["iataCode"]
    #             }
    #         }
    #         endpoint = self.sheety_endpoint + str(data["id"])
    #         response = requests.put(url=endpoint, json=config, headers=self.sheety_header)
    def post_prices(self):
        if int(self.flight_data['data'][0]['price']) < self.row_data['lowestPrice']:
            flight_data_manager = FlightData(self.flight_data)
            config = {
                "price": {
                    "lowestPrice": self.flight_data['data'][0]['price']
                }
            }
            endpoint = self.sheety_endpoint + str(self.row_data["id"])
            response = requests.put(url=endpoint, json=config, headers=self.sheety_header)
            notification_manager = NotificationManager(flight_data_manager)
        else:

            pass


