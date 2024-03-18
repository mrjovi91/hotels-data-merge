from integrations.suppliers.supplier import Supplier
from model.result_Item import ResultItem
from settings import settings

class AcmeSupplier(Supplier):

    def __init__(self, search_type, search_parameters):
        super().__init__(
            name = 'Acme',
            url = settings['suppliers']['Acme'],
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
        filtered_raw_data = self.return_raw_data()
        output = []
        for result in filtered_raw_data:


    def get_id(cls, data_item):
        pass

    def get_destination_id(cls, data_item):
        pass

    def get_name(cls, data_item):
        pass

    def get_location(cls, data_item):
        pass

    def get_description(cls, data_item):
        pass

    def get_amenities(cls, data_item):
        pass

    @abstractclassmethod
    def get_images(cls, data_item):
        pass

    @abstractclassmethod
    def get_booking_conditions(cls, data_item):
        pass
