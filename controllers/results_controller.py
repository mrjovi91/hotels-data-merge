from integrations.suppliers.acme import AcmeSupplier
from integrations.suppliers.patagonia import PatagoniaSupplier
from integrations.suppliers.paperflies import PaperfliesSupplier
from model.search_results import SearchResults
from model.result_Item import ResultItem


suppliers = {
    'Acme': AcmeSupplier,
    'Patagonia': PatagoniaSupplier ,
    'Paperflies': PaperfliesSupplier
}


class ResultsController:

    def __init__(self, search_parameters):
        self._search_parameters = search_parameters
        self._results = {}

    def search(self):
        for supplier_name, supplier_template in suppliers.items():
            supplier = supplier_template(search_parameters=self._search_parameters)
            supplier.fetch_data()
            self._results[supplier_name] = supplier.return_formatted_data()

    def json(self):
        output = {}
        for supplier_name, supplier in self._results.items():
            output[supplier_name] = supplier.json()
        return output

            