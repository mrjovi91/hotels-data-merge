from model.result_Item import ResultItem
import json

class SearchResults:
    def __init__(self):
        self._results = []
        self._hotels_id_in_results = []

    @property
    def results(self):
        return self._results

    @property
    def hotels_id_in_results(self):
        return self._hotels_id_in_results


    def append(self, result):
        if not isinstance(result, ResultItem):
            raise Exception('Unable to append non ResultItem type to SearchResults')
        self._results.append(result)
        self._hotels_id_in_results.append(result.id)

    def get_hotel(self, hotel_id):
        if hotel_id not in self._hotels_id_in_results:
            return None
        for hotel in self._results:
            if hotel.id == hotel_id:
                return hotel

    def get_hotel_field(self, hotel_id, field):
        hotel = self.get_hotel(hotel_id).json()
        return hotel[field]

    def json(self):
        output = []
        for result in self._results:
            output.append(result.json())
        return output

    def __repr__(self):
        return f'SearchResults: {json.dumps(self.json())}'