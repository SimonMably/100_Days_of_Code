class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, price, departure_airport_code, departure_city,
                 departure_date, arrival_city, arrival_city_code, return_date):
        self.price = price
        self.departure_city = departure_city
        self.departure_airport_code = departure_airport_code
        self.departure_date = departure_date
        self.arrival_city = arrival_city
        self.arrival_city_code = arrival_city_code
        self.return_date = return_date

