import json

class Location:
    def __init__(self, address, postal_code, lat=None, lng=None):
        self._address = address
        self._postal_code = postal_code
        self._lat = lat
        self._lng = lng

    @property
    def address(self):
        return self._address

    @property
    def postal_code(self):
        return self._postal_code

    @property
    def lat(self):
        return self._lat

    @property
    def lng(self):
        return self._lng

    def json(self):
        return {
            'address': self._address,
            'postal_code': self._postal_code,
            'lat': self._lat,
            'lng': self._lng
        }
    
    def __repr__(self):
        return f'Location: {json.dumps(self.json())}'

