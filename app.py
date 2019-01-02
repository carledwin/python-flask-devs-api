from flask import Flask, jsonify, request

app = Flask(__name__)

devs = [
    {
    'id': 3,
    'name': 'Fulano de Tal',
    'lang': 'Python'
    },
    {
    'id': 1,
    'name': 'Beltrano de Lano',
    'lang': 'Java'
    },
    {
    'id': 2,
    'name': 'Zelano de Meby',
    'lang': 'Python'
    }
]

@app.route('/', methods=['GET'])
def home():
    return 'Bem vindo a API REST Python com Flask! :) :)', 200

@app.route('/devs', methods=['GET'])
def all():
    return jsonify(devs), 200

@app.route('/devs/<string:lang>', methods=['GET'])
def devs_by_lang(lang): 
    devs_by_lang = [dev for dev in devs if dev['lang'] == lang]
    return jsonify(devs_by_lang), 200

@app.route('/devs/<int:id>', methods=['GET'])
def dev_by_id(id):
    for dev in devs:
        if dev['id'] == id:
            return jsonify(dev), 200
        
    return jsonify({'error':'Not found'}), 404

@app.route('/devs', methods=['POST'])
def save():
    data = request.get_json()
    devs.append(data) 
    return jsonify(data), 201

@app.route('/devs/<int:id>', methods=['PUT'])
def update(id):
    data = request.get_json()
    for dev in devs:
        if dev['id'] == id:
            dev['name'] = data.get('name')
            dev['lang'] = data.get('lang')
            return jsonify(data), 200
    
    return jsonify({'error':'Not found'}), 404

@app.route('/devs/<int:id>', methods=['DELETE'])
def remove(id):
    for dev in devs:
        index = devs.index(dev)
        if dev['id'] == id:
            devs.pop(index)
            return jsonify({}), 204

    return jsonify({'error':'Not found'}), 404        

if __name__ == '__main__':
    app.run(debug=True)