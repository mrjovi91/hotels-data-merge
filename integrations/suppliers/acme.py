from integrations.suppliers.supplier import Supplier
from model.location import Location
from model.result_Item import ResultItem
from settings import settings

import pycountry

class AcmeSupplier(Supplier):

    def __init__(self, search_parameters):
        super().__init__(
            name = 'Acme',
            url = settings['suppliers']['Acme'],
            search_parameters = search_parameters
        )

    def return_raw_data(self):
        super().return_raw_data()
        output = []
        for data_item in self._raw_data:
            if self._search_parameters.get('destination_id', None) is not None:
                if self._search_parameters['destination_id'] != data_item['DestinationId']:
                    continue

            hotel_ids = self._search_parameters('hotels_id', None)
            if hotel_ids is not None:
                if len(hotel_ids) > 0 and data_item['Id'] not in hotel_ids:
                    continue

            output.append(data_item)
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
        country = pycountry.countries.get(alpha_2=data_item['Country'])
        
        return Location(
            address = final_address,
            city = data_item['City'],
            country = country.name,
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
