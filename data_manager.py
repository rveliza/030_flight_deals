import os, requests
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth
from pprint import pprint

load_dotenv()

class DataManager:
    def __init__(self) -> None:
        self._user = os.getenv("SHEETY_USERNAME")
        self._password = os.getenv("SHEETY_PASSWORD")
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=os.getenv("SHEETY_PRICES_ENDPOINT"), auth=self._authorization)
        data = response.json()
        self.destination_data = data['prices']
        return self.destination_data
    
    
    def update_destination_codes(self, row):
        new_data = {
            "price": {
                "iataCode": row["iataCode"]
            }
        }

        response = requests.put(url=f"{os.getenv("SHEETY_PRICES_ENDPOINT")}/{row['id']}", 
                                json=new_data, auth=self._authorization)
        print(response.text)


if __name__ == "__main__":
    myDataManager = DataManager()
    data = myDataManager.get_destination_data()
    pprint(data)

