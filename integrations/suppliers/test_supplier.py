import requests

class TestSupplier():

    def __init__(self, name=None, url=None, search_parameters=None):
        self._name = name
        self._supplier_url = url
        self._raw_data = None
        self._search_parameters = search_parameters

    def fetch_data(self):
        response = requests.get(self._supplier_url)
        if response.status_code != 200:
            raise Exception('Error: Failed to connect to supplier. Please try again')
        self._raw_data = response.json()

    def return_raw_data(self):
        if self._raw_data is None:
            raise Exception('Error: Fetch Data has not been run on this supplier yet.')
        return self._raw_data

