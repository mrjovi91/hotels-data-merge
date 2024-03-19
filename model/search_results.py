from model.result_Item import ResultItem
import json

class SearchResults:
    def __init__(self):
        self._results = []

    def append(self, result):
        if not isinstance(result, ResultItem):
            raise Exception('Unable to append non ResultItem type to SearchResults')
        self._results.append(result)

    def json(self):
        output = []
        for result in self._results:
            output.append(result.json())
        return output

    def __repr__(self):
        return f'SearchResults: {json.dumps(self.json())}'