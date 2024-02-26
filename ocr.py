import os
import json
from keras_ocr import tools
import keras_ocr
import random


class ocr:
	def __init__(self, request):
		self.request = request;

	def scan(self):
		if 'file' not in self.request.files:
        return jsonify({"error": "No file provided"})

	    file = self.request.files['file']

	    if not file.filename.endswith(('.jpg', '.jpeg', '.png')):
	        return jsonify({"error": "Unsupported file format"})

	    image_path = 'temp_image.jpg'

	    token = ''

	    for i in range(10):
	        token += str(int(random.random()*10))
	    image_path = token+'.jpg'

	    file.save(image_path)

	    img = [tools.read(image_path)]
	    prediction_groups = pipeline.recognize(img)

	    os.remove(image_path)

	    return jsonify({'data': prediction_groups})