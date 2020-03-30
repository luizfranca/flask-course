from flask_restful import Resource
from flask_jwt_extended import jwt_required
from models.store import StoreModel

class Store(Resource):
    @jwt_required
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'message': 'Store not found'}, 404

    @jwt_required
    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'messge': 'This store already exists'}, 400

        store = StoreModel(name)

        try:
            store.upsert()
        except:
            return {'message': 'An error occurred while inserting this store'}, 500
        
        return store.json(), 201

    @jwt_required
    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete()

        return {'message': 'Store deleted'}

class StoreList(Resource):
    @jwt_required
    def get(self):
        return {'Stores': list(map(lambda x: x.json(), StoreModel.query.all()))}
