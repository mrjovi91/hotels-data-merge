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

    def append(self, image):
        if not isinstance(image, Image):
            raise Exception('Unable to append non Image type to Images')
        if image.image_type not in self._images.keys():
            self._images[image.image_type] = [image]
        else:
            self._images[image.image_type].append(image)

    def json(self):
        output = {}
        for image_type, images in self._images.items():
            for image in images:
                image_json = image.json()
                del image_json['type']
                if image_type not in output.keys():
                    output[image_type] = [image_json]
                else:
                    output[image_type].append(image_json)
        return output

    def __repr__(self):
        return f'Images: {json.dumps(self.json())}'


