class ResultItem:
    def __init__(self, id, destination_id, name, location, description, amenities, images, booking_conditions):
        self._id = id
        self._destination_id = destination_id
        self._name = name
        self._location = location
        self._description = description
        self._amenities = amenities
        self._images = images
        self._booking_conditions = booking_conditions

    @property
    def id(self):
        return self._id

    @property
    def destination_id(self):
        return self._destination_id

    @property
    def name(self):
        return self._name

    @property
    def location(self):
        return self._location

    @property
    def description(self):
        return self._description

    @property
    def amenities(self):
        return self._amenities

    @property
    def images(self):
        return self._images

    @property
    def booking_conditions(self):
        return self._booking_conditions

    def json(self):
        return {
            'id': self._id,
            'destination_id': self._destination_id,
            'name': self._name,
            'location': self._location.json() if self._location else None,
            'description': self._description,
            'amenities': self._amenities.json() if self._amenities else None,
            'images': self._images.json() if self._images else None,
            'booking_conditions': self._booking_conditions
        }

    def __repr__(self):
        return f'ResultItem: {self.json()}'