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

class Images:
    def __init__(self):
        self._images = {}

    @property
    def images(self):
        return self._images

    @images.setter
    def images(self, value):
        if not isinstance(value, dict):
            raise Exception('Value of image should be of type dictionary')
        self._images = value

    def append(self, image):
        if not isinstance(image, Image):
            raise Exception('Unable to append non Image type to Images')
        image_data = image.json()
        del image_data['type']
        if image.image_type not in self._images.keys():
            self._images[image.image_type] = [image_data]
        else:
            self._images[image.image_type].append(image_data)

    def json(self):
        return self._images

    def __repr__(self):
        return f'Images: {json.dumps(self.json())}'


