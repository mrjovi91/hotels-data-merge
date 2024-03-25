from flask import request, Blueprint
from controllers.api_controller import ApiController


routes = Blueprint('routes', __name__)

@routes.route("/search", methods = ['POST'])
def search():
    return ApiController.search_hotels(request)

@routes.route("/test", methods = ['POST'])
def test():
    return ApiController.test(request)

