import datetime
from flask import render_template, request, session, flash, redirect, url_for, jsonify
import json
import requests
import traceback


from settings.settings import settings

class ApiController:
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
        if 'hotels_id' not in data.keys() and 'destination_id' not in data.keys():
            return jsonify({"result": "Please ensure that either hotel or destination is provided.", "status": "error"}), 400
        print(headers)
        return jsonify({'result': data, "status": "success"}), 200