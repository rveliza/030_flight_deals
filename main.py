from data_manager import DataManager
from flight_search import FlightSearch


data_manager = DataManager()
flight_search = FlightSearch()

sheet_data = data_manager.get_destination_data()
# print(sheet_data)

for row in sheet_data:
    if row['iataCode'] == "":
        row['iataCode'] = flight_search.get_destination_code(row['city'])

data_manager.destination_data = sheet_data
print(data_manager.destination_data)
