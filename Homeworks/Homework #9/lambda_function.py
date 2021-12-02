# import tflite_runtime.interpreter as tflite
import numpy as np
# import tensorflow.lite as tflite
import tflite_runtime.interpreter as tflite
from io import BytesIO
from urllib import request

from PIL import Image

classes = ['dogs', "cats"]

interpreter = tflite.Interpreter(model_path='cats-dogs-v2.tflite')
# interpreter = tflite.Interpreter(model_path='cats-dogs-v1.tflite')
interpreter.allocate_tensors()

input_index = interpreter.get_input_details()[0]['index']
output_index = interpreter.get_output_details()[0]['index']

def download_image(url):
    with request.urlopen(url) as resp:
        buffer = resp.read()
    stream = BytesIO(buffer)
    img = Image.open(stream)
    return img


def prepare_image(img, target_size):
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img = img.resize(target_size, Image.NEAREST)
    return img

def preprocess_input(x):
    x /= 255
    return x


def predict(url):
    img = download_image(url)
    our_img = prepare_image(img, (150, 150))
    x = np.array(our_img, dtype='float32')
    X = np.array([x])

    X= preprocess_input(X)
    interpreter.set_tensor(input_index, X)
    interpreter.invoke()
    preds = interpreter.get_tensor(output_index)

    float_prediction = preds[0].tolist()

    return dict(zip(classes, float_prediction))

def lambda_handler(event, context):
    url = event['url']
    result = predict(url)
    return result