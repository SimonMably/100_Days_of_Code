from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()
notifier = NotificationManager()

sheet_data = data_manager.get_response()

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        flight_search.retrieve_iata_code(row["city"])

    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()
else:
    for row in sheet_data:
        row["iataCode"] = flight_search.search_flights(row["iataCode"])

# for destination in sheet_data:
#     flight = flight_search.search_flights()
#     if flight is not None and flight.price < destination["lowestPrice"]:
#         notifier.notify_by_email(
#             message="Low price alert!" \
#                     f" Only £{flight.price} to fly from {flight.origin_city}-"
#                     f"{flight.origin_airport} to {flight.destination_city}-"
#                     f"{flight.destination_airport}, from {flight.out_date} to "
#                     f"{flight.return_date}."
#         )
