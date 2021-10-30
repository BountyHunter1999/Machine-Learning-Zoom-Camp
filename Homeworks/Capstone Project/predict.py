from logging import debug
import pickle
import os

from flask import Flask, request, jsonify

model_file = 'model.bin'
dv_file = 'dv.bin'

with open(model_file, 'rb') as f:
    model = pickle.load(f)
    
with open(dv_file, 'rb') as f:
    dv = pickle.load(f)

app = Flask('rain_tommorow')

@app.route('/', methods=['GET'])
def reroute():
    return "<b>Send a post request to <i>/predict</i></b>"

@app.route("/predict", methods=["POST"])
def predict():
    customer = request.get_json()

    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[0,1]
    rain = y_pred > 0.36

    print(rain)

    result = {
        'tommorow_rain_probability': float(round(y_pred, 3)),
        'rain': bool(rain)
    }

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)
