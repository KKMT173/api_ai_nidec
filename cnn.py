from keras.models import load_model  # TensorFlow is required for Keras to work
import cv2  # Install opencv-python
import numpy as np
from PIL import Image, ImageOps
# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

class cnn:
    def __init__(self, model, class_names):
        self.model = model
        self.class_names =class_names

    def detech(self, file):
        print(file)
        with Image.open(file) as image:
            size = (224, 224)
            image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

            # turn the image into a numpy array
            image_array = np.asarray(image)
            data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
            # Normalize the image
            normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
           
            # Load the image into the array
            data[0] = normalized_image_array

            # Predicts the model
            prediction = self.model.predict(data)
            index = np.argmax(prediction)
            class_name = self.class_names[index]
            confidence_score = prediction[0][index]

            # Print prediction and confidence score
            print("Class:", class_name[2:], end="")
            print("Confidence Score:", confidence_score)

        return [class_name[2:],str(np.round(confidence_score * 100))[:-2]]