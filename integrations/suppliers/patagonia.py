from integrations.suppliers.supplier import Supplier
from model.amenities import Amenities
from model.image import Image, Images
from model.location import Location
from model.result_Item import ResultItem
from model.search_results import SearchResults
from settings.settings import settings

class PatagoniaSupplier(Supplier):

    def __init__(self, search_parameters={}):
        super().__init__(
            name = 'Patagonia',
            url = settings['suppliers']['Patagonia']['url'],
            search_parameters = search_parameters
        )

    def return_raw_data(self):
        super().return_raw_data()
        output = []
        for data_item in self._raw_data:
            if self._search_parameters.get('destination_id', None) is not None:
                if self._search_parameters['destination_id'] != data_item['destination']:
                    continue

            hotel_ids = self._search_parameters.get('hotels_id', None)
            if hotel_ids is not None:
                if len(hotel_ids) > 0 and data_item['id'] not in hotel_ids:
                    continue

            output.append(data_item)
        return output

    def return_formatted_data(self):
        search_results = SearchResults()
        filtered_raw_data = self.return_raw_data()
        for data_item in filtered_raw_data:
            search_results.append(ResultItem(
                id = PatagoniaSupplier.get_id(data_item),
                destination_id = PatagoniaSupplier.get_destination_id(data_item),
                name = PatagoniaSupplier.get_name(data_item),
                location = PatagoniaSupplier.get_location(data_item),
                description = PatagoniaSupplier.get_description(data_item),
                amenities = PatagoniaSupplier.get_amenities(data_item),
                images = PatagoniaSupplier.get_images(data_item),
                booking_conditions = PatagoniaSupplier.get_booking_conditions(data_item)
            ))
        return search_results

    @classmethod
    def get_id(cls, data_item):
        return data_item['id']

    @classmethod
    def get_destination_id(cls, data_item):
        return data_item['destination']

    @classmethod
    def get_name(cls, data_item):
        return data_item['name'].strip() if isinstance(data_item['name'], str) else data_item['name']

    @classmethod
    def get_location(cls, data_item):
        return Location(
            address = data_item['address'].strip() if isinstance(data_item['address'], str) else None,
            lat = data_item['lat'] if data_item['lat'] and isinstance(data_item['lat'], float) else None,
            lng = data_item['lng'] if data_item['lng'] and isinstance(data_item['lng'], float) else None
        )

    @classmethod
    def get_description(cls, data_item): 
        return data_item['info'].strip() if isinstance(data_item['info'], str) else data_item['info']

    @classmethod
    def get_amenities(cls, data_item):
        if data_item['amenities'] is None:
            return None
        amenities = Amenities()
        amenities.room = [ item.lower() for item in data_item['amenities'] ]
        return amenities

    @classmethod
    def get_images(cls, data_item):
        if data_item['images'] is None:
            return None
        images = Images()
        for image_type, image_items in data_item['images'].items():
            for image_item in image_items:
                image = Image(
                    link = image_item['url'],
                    description = image_item['description'],
                    image_type = image_type
                )
                images.append(image)
        return images

    @classmethod
    def get_booking_conditions(cls, data_item):
        return None
