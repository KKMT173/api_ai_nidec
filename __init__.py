
from flask import Flask, request, jsonify
from flask_cors import CORS
from keras.models import load_model

path_route = "/AI/"

#start server
app = Flask(__name__)
CORS(app)

#load model
model = load_model("./model/keras_model.h5", compile=False)

@app.route(f'{path_route}HELLO', methods=['GET'])
def getHello():
    return jsonify({'status': 'success', 'data': 'hello'})

@app.route(f'{path_route}CNN', methods=['POST'])
def process_file_blank():
    response = {}
    if request.files['file']:
        file = request.files['file']
        response = class.run(model,file)
    return jsonify({'status': 'successful', 'data': response})

if __name__ == '__main__':
    app.run(host="0.0.0.0",port='3545',debug=True)