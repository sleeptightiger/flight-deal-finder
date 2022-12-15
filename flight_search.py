import requests
from pprint import pprint
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from flight_data import FlightData
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self, data):
        self.flight_data = ''
        self.city = data["city"]
        self.tomorrow = datetime.today() + timedelta(days=1)
        self.six_months = datetime.today() + relativedelta(months=6)
        self.header = {
            "apikey": "Fjkom89d4FQliBZ36CK2DFv0THzwT9xK"
        }
        self.endpoint = "https://api.tequila.kiwi.com/locations/query"
        self.search_endpoint = "https://api.tequila.kiwi.com/v2/search"
        self.search_params = {
            "fly_from": "LON",
            "fly_to": data['iataCode'],
            "dateFrom": self.tomorrow.strftime('%d/%m/%Y'),
            "dateTo": self.six_months.strftime('%d/%m/%Y'),
            "limit": "5",
            "curr": "GBP"
        }
        self.search_headers = {
            "apikey": "Fjkom89d4FQliBZ36CK2DFv0THzwT9xK",
            "Content-Type": "application/json"
        }
        self.config = {
            "term": self.city
        }
        self.iataCode = ''


    def search(self):
        response = requests.get(url=self.endpoint, params=self.config, headers=self.header)
        self.iataCode = response.json()['locations'][0]['code']

    def flight_search(self):
        response = requests.get(url=self.search_endpoint, params=self.search_params, headers=self.search_headers)
        self.flight_data = response.json()