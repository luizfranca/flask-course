from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
    {
        'name': 'My Wonderful Store',
        'items': [
            {
                'name': 'My Item',
                'price': 15.99
            }
        ]
    }
]

@app.route('/store', methods=['POST'])
def create_store():
    data = request.get_json()
    
    new_store = {
        'name': data['name'], 
        'items':[]
    }
    stores.append(new_store)

    return jsonify(new_store), 201

@app.route('/store/<string:name>') ## default method is GET
def get_store(name):
    store = next(filter(lambda x: x['name'] == name, stores), None)

    if store:
        return jsonify(store)
    return {'message': 'There isn\'t a store with that name'}, 404

@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})

@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    store = next(filter(lambda x: x['name'] == name, stores), None)

    if store:
        data = request.get_json()
        new_item = {
            'name': data['name'],
            'price': data['price']
        }
        store['items'].append(new_item)
        return jsonify(new_item), 201
    
    return {'message': 'Store not found'}, 404

@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    store = next(filter(lambda x: x['name'] == name, stores), None)

    if store:
        return jsonify({'items': store['items']})
    return {'message': 'Store not found'}, 404
app.run(port=5000)
