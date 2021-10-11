import pickle
import os

from flask import Flask
from flask import request
from flask import jsonify

if os.path.isfile('model2.bin'):
    model_file = 'model2.bin'
else:
    model_file = 'model1.bin'
    
dv_file = 'dv.bin'

with open(model_file, 'rb') as f:
    model = pickle.load(f)

with open(dv_file, 'rb') as f:
    dv = pickle.load(f)

app = Flask('churn')

@app.route("/", methods=['GET'])
def reroute():
    return "<b>Send a post request to <a>/predict</a></b>"


@app.route('/predict', methods=['POST'])
def predict():
    customer = request.get_json()

    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[0,1]
    churn = y_pred > 0.5

    print(churn)

    result = {
        'churn_probability': float(round(y_pred, 3)),
        'churn': bool(churn)
    }

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)