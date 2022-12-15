from flight_data import FlightData
from pprint import pprint
from twilio.rest import Client
class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self, flight_data):
        self.data = flight_data
        self.send_notification()

    def send_notification(self):
        account_sid = 'ACf22f4ffa32d290a001af369f6455cb71'
        auth_token = 'a0b084fba3cb1f77e0dd82930d47b676'
        text = f"Low price alert! Only £{self.data.lowest_price}" \
               f" to fly from {self.data.departure_city}-{self.data.departure_code}" \
               f" to {self.data.city_to}-{self.data.code_to}, from" \
               f" {self.data.departure_date} to {self.data.arrival_date}."
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body=text,
            from_='+15102408628',
            to='+19563265811'
        )