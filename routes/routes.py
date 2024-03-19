from flask import request, Blueprint
from controllers.api_controller import ApiController


routes = Blueprint('routes', __name__)
    
# @routes.route("/debug", methods = ['POST'])
# def debug():
#     return SubmissionController.debug(request)

@routes.route("/get_my_ip", methods=["GET"])
def route_get_my_ip():
    return ApiController.get_client_ip(request)

@routes.route("/search", methods = ['POST'])
def search():
    return ApiController.search_hotels(request)

# @routes.route("/submit", methods = ['POST'])
# def submit():
#     return SubmissionController.store(request)


