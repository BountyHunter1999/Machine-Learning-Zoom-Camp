from logging import debug
import pickle
import os

from flask import Flask, request, jsonify

model_file = 'model_t.bin'
# model_file = 'model.bin'

with open(model_file, 'rb') as f:
    dv, model = pickle.load(f)

app = Flask('rain_tommorow')

@app.route('/', methods=['GET'])
def reroute():
    return "<b>Send a post request to <i>/predict</i></b>"

@app.route("/predict", methods=["POST"])
def predict():
    customer = request.get_json()

    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[0,1]
    print("Probability is", y_pred)
    rain = y_pred >= 0.33

    print(rain)

    result = {
        'tommorow_rain_probability': float(round(y_pred, 6)),
        'rain': bool(rain)
    }

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)
