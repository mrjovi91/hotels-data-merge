from integrations.suppliers.supplier import Supplier
from model.amenities import Amenities
from model.image import Image, Images
from model.location import Location
from model.result_Item import ResultItem
from model.search_results import SearchResults
from settings.settings import settings

class PaperfliesSupplier(Supplier):

    def __init__(self, search_parameters={}):
        super().__init__(
            name = 'Paperflies',
            url = settings['suppliers']['Paperflies']['url'],
            search_parameters = search_parameters
        )

    def return_raw_data(self):
        super().return_raw_data()
        output = []
        for data_item in self._raw_data:
            if self._search_parameters.get('destination_id', None) is not None:
                if self._search_parameters['destination_id'] != data_item['destination_id']:
                    continue

            hotel_ids = self._search_parameters.get('hotels_id', None)
            if hotel_ids is not None:
                if len(hotel_ids) > 0 and data_item['hotel_id'] not in hotel_ids:
                    continue

            output.append(data_item)
        return output

    def return_formatted_data(self):
        search_results = SearchResults()
        filtered_raw_data = self.return_raw_data()
        for data_item in filtered_raw_data:
            search_results.append(ResultItem(
                id = PaperfliesSupplier.get_id(data_item),
                destination_id = PaperfliesSupplier.get_destination_id(data_item),
                name = PaperfliesSupplier.get_name(data_item),
                location = PaperfliesSupplier.get_location(data_item),
                description = PaperfliesSupplier.get_description(data_item),
                amenities = PaperfliesSupplier.get_amenities(data_item),
                images = PaperfliesSupplier.get_images(data_item),
                booking_conditions = PaperfliesSupplier.get_booking_conditions(data_item)
            ))
        return search_results

    @classmethod
    def get_id(cls, data_item):
        return data_item['hotel_id']

    @classmethod
    def get_destination_id(cls, data_item):
        return data_item['destination_id']

    @classmethod
    def get_name(cls, data_item):
        return data_item['hotel_name'].strip() if isinstance(data_item['hotel_name'], str) else data_item['hotel_name']

    @classmethod
    def get_location(cls, data_item):
        if data_item['location'] is not None:
            address = data_item['location']['address'].strip() if isinstance(data_item['location']['address'], str) else None
            country = data_item['location']['country'].strip() if isinstance(data_item['location']['country'], str) else None
        else:
            address = None
            country = None
        
        return Location(
            address = address,
            country = country
        )

    @classmethod
    def get_description(cls, data_item): 
        return data_item['details'].strip() if isinstance(data_item['details'], str) else data_item['details']

    @classmethod
    def get_amenities(cls, data_item):
        if data_item['amenities'] is None:
            return None
        amenities = Amenities()

        amenities.general = data_item['amenities']['general'] if data_item['amenities']['general'] else []
        amenities.room = data_item['amenities']['room'] if data_item['amenities']['room'] else []
        return amenities

    @classmethod
    def get_images(cls, data_item):
        if data_item['images'] is None:
            return None
        images = Images()
        for image_type, image_items in data_item['images'].items():
            for image_item in image_items:
                image = Image(
                    link = image_item['link'],
                    description = image_item['caption'],
                    image_type = image_type
                )
                images.append(image)
        return images

    @classmethod
    def get_booking_conditions(cls, data_item):
        return data_item['booking_conditions']
