from controllers.results_controller import ResultsController
from integrations.suppliers.acme import AcmeSupplier
from integrations.suppliers.paperflies import PaperfliesSupplier
from integrations.suppliers.patagonia import PatagoniaSupplier
from integrations.suppliers.test_supplier import TestSupplier

import datetime
from flask import render_template, request, session, flash, redirect, url_for, jsonify
import json
import requests
import traceback


from settings.settings import settings

class ApiController:
    suppliers = {
        "Acme": AcmeSupplier,
        "Patagonia": PatagoniaSupplier,
        "Paperflies": PaperfliesSupplier
    }

    @classmethod
    def get_client_ip(cls, request):
        if 'X-Forwarded-For' in request.headers:
            return request.headers.get('X-Forwarded-For')
        return request.remote_addr
    
    @classmethod
    def get_my_ip(cls, request):
        return jsonify({'ip': ApiController.get_client_ip(request)}), 200

    @classmethod
    def search_hotels(cls, request):
        headers = dict(request.headers)
        # headers.pop('X-Api-Key', None)
        data = request.get_json()
        print(data)
        print(headers)
        results = ResultsController(search_parameters=data)
        results.search()
        results.merge_result()
        # return jsonify(formatted_data.json()), 200
        return jsonify({'result': results.merged_results, "status": "success"}), 200

    @classmethod
    def test(cls, request):
        headers = dict(request.headers)
        # headers.pop('X-Api-Key', None)
        data = request.get_json()
        print(data)
        # if 'hotels_id' not in data.keys() and 'destination_id' not in data.keys():
        #     return jsonify({"result": "Please ensure that either hotel or destination is provided.", "status": "error"}), 400
        print(headers)
        results = ResultsController(search_parameters=data)
        results.search()
        return jsonify({'result': results.json(), "status": "success"}), 200
        