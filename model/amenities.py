import json

class Amenities:
    def __init__(self):
        self._general = []
        self._room = []

    def append_general(self, item):
        self._general(item)

    @property
    def general(self):
        return self._general

    @property
    def room(self):
        return self._room

    @general.setter
    def general(self, value):
        if not isinstance(value, list) and value is not None:
            raise Exception('Please provide list of strings when setting amenties')
        if value is None:
            self._general = []
        else:
            self._general = value

    @room.setter
    def room(self, value):
        if not isinstance(value, list):
            raise Exception('Please provide list of strings when setting amenties')
        if value is None:
            self._room = []
        else:
            self._room = value

    def append_general(self, item):
        self._general(item)

    def append_room(self, item):
        self._room(item)

    def json(self):
        return {
            "general": self._general,
            "room": self._room
        }
    
    def __repr__(self):
        return f'Amenities: {json.dumps(self.json())}'

