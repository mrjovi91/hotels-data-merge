import json

class Location:
    def __init__(self, address, city=None, country = None, lat=None, lng=None):
        self._address = address
        self._city = city
        self._country = country
        self._lat = lat
        self._lng = lng

    @property
    def address(self):
        return self._address

    @property
    def city(self):
        return self._city

    @property
    def country(self):
        return self._country

    @property
    def lat(self):
        return self._lat

    @property
    def lng(self):
        return self._lng

    def json(self):
        return {
            'lat': self._lat,
            'lng': self._lng,
            'address': self._address,
            'city': self._city,
            'country': self._country
        }
    
    def __repr__(self):
        return f'Location: {json.dumps(self.json())}'

