# -*- coding: utf-8 -*-

from flask_restful import Api, Resource

class Index(Resource):

    def get(self):
        return {'hello': 'world by api python method get'}

    def post(self):
        return {'hello': 'world by api python method post'}

    def put(self):
        return {'hello': 'world by api python method put'}

    def delete(self):
        return {'hello': 'world by api python method delete'}

api = Api()

def configure_api(app):
    api.add_resource(Index, '/')

    api.init_app(app)