

class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, json):
        self.data = json['data'][0]
        self.lowest_price = str(self.data['price'])
        self.departure_airport_code = self.data['id']
        self.departure_code = self.data['flyFrom']
        self.departure_city = self.data['cityFrom']
        self.code_to = self.data['flyTo']
        self.city_to = self.data['cityTo']
        self.departure_date = self.data['route'][0]['local_departure'][0:10]
        self.arrival_date = self.data['route'][0]['local_arrival'][0:10]

