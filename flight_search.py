import os, requests

class FlightSearch:
    def __init__(self) -> None:
        self._api_key = os.getenv("AMADEUS_API_KEY")
        self._api_secret = os.getenv("AMADEUS_SECRET")
        self._amadeus_endpoint = "https://test.api.amadeus.com"
        # Get new token every time program is run.
        self._token = self._get_new_token()

    def _get_new_token(self) -> str:
        """
        Generates the authentication token used for accesing the Amadeus
        API and returns it.

        Returns:
            str: The new acces token obtained from the API response
        """

        # Header with content type as per Amadeus documentation
        header = {
            'Content-Type': 'application/x-www-form-urlencoded' 
        }

        body = {
            'grant_type': 'client_credentials',
            'client_id': self._api_key,
            'client_secret': self._api_secret
        }

        response = requests.post(url=f"{self._amadeus_endpoint}/v1/security/oauth2/token",
                                 headers=header, data=body)
         # New bearer token. Typically expires in 1799 seconds (30min)
        print(f"Your token is {response.json()['access_token']}")
        print(f"Your token expires in {response.json()['expires_in']} seconds")
        return response.json()['access_token']
    

    def get_destination_code(self, city_name):
        code = "TESTING"
        return code