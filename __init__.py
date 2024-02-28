
from flask import Flask, request, jsonify
from flask_cors import CORS
from keras.models import load_model
from io import BytesIO
from cnn import cnn
from sever_find_blank import sever_find_blank
path_route = "/AI/"

#start server
app = Flask(__name__)
CORS(app)

#load model
model = load_model("./model/keras_model.h5", compile=False)
class_names = open("./label/labels.txt", "r").readlines()

@app.route(f'{path_route}HELLO', methods=['GET'])
def getHello():
    return jsonify({'status': 'success', 'data': 'hello'})

@app.route(f'{path_route}CNN', methods=['POST'])
def process_cnn():
    global class_names
    print(class_names)
    response = {}
    print(request.files)
    if request.files['file']:
        file = request.files['file']
        file_data = file.read()
        model_cnn = cnn(model,class_names)
        response = model_cnn.detech(BytesIO(file_data))
    return jsonify({'status': 'successful', 'data': response})

@app.route(f'{path_route}server_find_blank', methods=['POST'])
def process_find_blank():
    stamp = request.form['stamp']
	file = request.files['file']
	file_data = file.read()
	output_path = sever_find_blank.find_and_replace_blank(BytesIO(file_data), stamp)
	with open(output_path, 'rb') as output_file:
	output_data = output_file.read()
	response = jsonify({'status': 'success', 'base64_img': 'data:image/png;base64,'+base64.b64encode(output_data).decode('utf-8')})
	return response
	
if __name__ == '__main__':
    app.run(host="0.0.0.0",port='3545',debug=True)