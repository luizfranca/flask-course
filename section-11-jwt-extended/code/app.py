import os

from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager

from db import db
from resources.item import Item, ItemList
from resources.store import Store, StoreList
from resources.user import UserRegister, User, UserLogin, TokenRefresh, UserLogout
from blocklist import BLOCKLIST

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
## when the user passes a wrong token or doesn't pass one
## it's going to say `unauthorized` instead of a 500 error
app.config['PROPAGATE_EXCEPTIONS'] = True 
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']
app.secret_key = 'luiz' # app.config['JWT_SECRET_KEY']
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWTManager(app) # does not create /auth endpoint

@jwt.user_claims_loader
def add_claims_to_jwt(identity): # identiry = user.id
    if identity == 1: # Instead of hard-coding, you should read from a config file or a database
        return {'is_admin': True}
    return {'is_admin': False}

@jwt.token_in_blacklist_loader
def check_if_token_in_blocklist(decrypted_token):
    return decrypted_token['jti'] in BLOCKLIST

@jwt.expired_token_loader
def expired_token_callback():
    return {
        'description': 'Your token has expired',
        'error': 'token_expired'
    }, 401

@jwt.invalid_token_loader
def invalid_token_callback(error):
    return {
        'description': 'Your token is invalid',
        'error': 'token_invalid'
    }, 401

@jwt.unauthorized_loader
def unauthorized_token_callback(error):
    return {
        'description': 'You need to seend an authorization token',
        'error': 'token_unauthorized'
    }, 401

@jwt.needs_fresh_token_loader
def needs_fresh_token_callback():
    return {
        'description': 'You need a fresh token',
        'error': 'token_unfresh'
    }, 401

@jwt.revoked_token_loader
def revoked_token_callback():
    return {
        'description': 'Your token has been revoked',
        'error': 'token_revoked'
    }, 401

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')
api.add_resource(User, '/user/<int:user_id>')
api.add_resource(UserLogin, '/login')
api.add_resource(UserLogout, '/logout')
api.add_resource(TokenRefresh, '/refresh')

db.init_app(app)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
