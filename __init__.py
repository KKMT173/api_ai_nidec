
from flask import Flask, request, jsonify
from flask_cors import CORS
#from keras.models import load_model


#start server
app = Flask(__name__)
CORS(app)

#load model
#smodel = load_model("./model/keras_model.h5", compile=False)

@app.route('/AI/HELLO', methods=['GET'])
def getHello():
    return jsonify({'status': 'success', 'data': 'hello'})

if __name__ == '__main__':
    app.run(host="0.0.0.0",port='3545',debug=True)