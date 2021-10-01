"""API views """
from flask import Blueprint
from flask_restful import Api

from .resources.index import IndexResource
from .resources.wish_list import WishListResource

main_blueprint = Blueprint('api', __name__, url_prefix='/api/v1/book')

api = Api(main_blueprint)


api.add_resource(IndexResource, '/')

api.add_resource(WishListResource, '/wish_list')


