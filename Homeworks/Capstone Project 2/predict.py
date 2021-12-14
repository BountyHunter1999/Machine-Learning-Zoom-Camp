from logging import debug
import pickle
import os

from flask import Flask, request, jsonify

model_file = 'model.bin'

with open(model_file, 'rb') as f:
    dv, model = pickle.load(f)

app = Flask('heart_disease')

@app.route('/', methods=['GET'])
def reroute():
    return "<b>Send a post request to <i>/predict</i></b>"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    X = dv.transform([data])
    y_pred = model.predict(X)
    print("Probability is", y_pred)
    hd = y_pred >= 0.5

    print(hd)

    result = {
        'Heart Disease': bool(hd)
    }

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)
