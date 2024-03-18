from integrations.suppliers.supplier import Supplier
from model.location import Location
from model.result_Item import ResultItem
from settings import settings

class PaperfliesSupplier(Supplier):

    def __init__(self, search_type, search_parameters):
        super().__init__(
            name = 'Paperflies',
            url = settings['suppliers']['Paperflies'],
            search_type = search_type,
            search_parameters = search_parameters
        )

    def return_raw_data(self):
        super().return_raw_results()
        output = []
        for result in self._raw_data:
            if self._search_type == 'hotel' and result['Id'] in self._search_parameters:
                output.append(result)
            elif self._search_type == 'destination' and result['DestinationId'] == self._search_parameters:
                output.append(result)
        return output

    def return_formatted_data(self):
        output = []
        filtered_raw_data = self.return_raw_data()
        for data_item in filtered_raw_data:
            output.append(ResultItem(
                id = AcmeSupplier.get_id(data_item),
                destination_id = AcmeSupplier.get_destination_id(data_item),
                name = AcmeSupplier.get_name(data_item),
                location = AcmeSupplier.get_location(data_item),
                description = AcmeSupplier.get_description(data_item),
                amenities = AcmeSupplier.get_amenities(data_item),
                images = AcmeSupplier.get_images(data_item),
                booking_conditions = AcmeSupplier.get_booking_conditions(data_item)
            ))
        return output

    def get_id(cls, data_item):
        return data_item['Id']

    def get_destination_id(cls, data_item):
        return data_item['DestinationId']

    def get_name(cls, data_item):
        return data_item['Name']

    def get_location(cls, data_item):
        address = data_item['Address'].strip() if data_item['Address'] else ''
        postal_code = data_item['PostalCode'].strip() if data_item['PostalCode'] else ''
        final_address = f'{address} {postal_code}'.strip()
        if final_address == '':
            final_address = None
        return Location(
            address = final_address,
            lat = data_item['Latitude'],
            lng = data_item.get['Longitude']
        )

    def get_description(cls, data_item):
        return data_item['Description']

    def get_amenities(cls, data_item):
        return None

    def get_images(cls, data_item):
        return None

    def get_booking_conditions(cls, data_item):
        return None
