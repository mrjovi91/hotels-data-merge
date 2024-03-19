from integrations.suppliers.supplier import Supplier
from model.location import Location
from model.result_Item import ResultItem
from settings.settings import settings

class PaperfliesSupplier(Supplier):

    def __init__(self, search_type, search_parameters):
        super().__init__(
            name = 'Paperflies',
            url = settings['suppliers']['Paperflies'],
            search_type = search_type,
            search_parameters = search_parameters
        )

    def return_raw_data(self):
        super().return_raw_data()
        output = []
        for data_item in self._raw_data:
            if self._search_parameters.get('destination_id', None) is not None:
                if self._search_parameters['destination_id'] != data_item['destination_id']:
                    continue

            hotel_ids = self._search_parameters('hotels_id', None)
            if hotel_ids is not None:
                if len(hotel_ids) > 0 and data_item['hotel_id'] not in hotel_ids:
                    continue

            output.append(data_item)
        return output

    def return_formatted_data(self):
        output = []
        filtered_raw_data = self.return_raw_data()
        for data_item in filtered_raw_data:
            output.append(ResultItem(
                id = PaperfliesSupplier.get_id(data_item),
                destination_id = PaperfliesSupplier.get_destination_id(data_item),
                name = PaperfliesSupplier.get_name(data_item),
                location = PaperfliesSupplier.get_location(data_item),
                description = PaperfliesSupplier.get_description(data_item),
                amenities = PaperfliesSupplier.get_amenities(data_item),
                images = PaperfliesSupplier.get_images(data_item),
                booking_conditions = PaperfliesSupplier.get_booking_conditions(data_item)
            ))
        return output

    def get_id(cls, data_item):
        return data_item['hotel_id']

    def get_destination_id(cls, data_item):
        return data_item['destination_id']

    def get_name(cls, data_item):
        return data_item['hotel_name']

    def get_location(cls, data_item):
        address = data_item['location']['address'].strip() if data_item['location']['address'] else None
        return Location(
            address = address
            country = data_item['location']['country'],
            lat = data_item['Latitude'],
            lng = data_item['Longitude']
        )

    def get_description(cls, data_item):
        return data_item['Description']

    def get_amenities(cls, data_item):
        return None

    def get_images(cls, data_item):
        return None

    def get_booking_conditions(cls, data_item):
        return None
