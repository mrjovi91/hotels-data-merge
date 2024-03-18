from abc import ABC, abstractmethod, abstractclassmethod
import requests

class Supplier(ABC):

    def __init__(self, name, url, search_parameters):
        if search_type not in ['hotel', 'destination']:
            raise Exception('Error: Invalid Search Type. Search Type should be either hotel or destination')
        self._name = name
        self._supplier_url = url
        self._raw_data = None
        self._search_parameters = search_parameters

    def fetch_data(self):
        response = requests.get(self.supplier_url)
        if response.status_code != 200:
            raise Exception('Error: Failed to connect to supplier. Please try again')
        self._raw_data = response.json

    @abstractmethod
    def return_raw_data(self):
        if self._raw_result is None:
            raise Exception('Error: Fetch Data has not been run on this supplier yet.')

    @abstractmethod
    def return_formatted_data(self):
        pass

    @abstractclassmethod
    def get_id(cls, data_item):
        pass

    @abstractclassmethod
    def get_destination_id(cls, data_item):
        pass

    @abstractclassmethod
    def get_name(cls, data_item):
        pass

    @abstractclassmethod
    def get_location(cls, data_item):
        pass

    @abstractclassmethod
    def get_description(cls, data_item):
        pass

    @abstractclassmethod
    def get_amenities(cls, data_item):
        pass

    @abstractclassmethod
    def get_images(cls, data_item):
        pass

    @abstractclassmethod
    def get_booking_conditions(cls, data_item):
        pass
