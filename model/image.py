import json

class Image:
    def __init__(self, link, description, image_type):
        self._link = link
        self._description = description
        self._image_type = image_type

    @property
    def link(self):
        return self._link

    @property
    def description(self):
        return self._description

    @property
    def image_type(self):
        return self._image_type

    def json(self):
        return {
            'link': self._link,
            'description': self._description,
            'type': self._image_type
        }
    
    def __repr__(self):
        return f'Image: {json.dumps(self.json())}'

