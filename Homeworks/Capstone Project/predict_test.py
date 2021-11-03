import requests

url = 'http://localhost:9696/predict'

data = {'Location': 'Melbourne',
 'MinTemp': 12.4,
 'MaxTemp': 18.1,
 'Rainfall': 0.0,
 'Evaporation': 5.6,
 'Sunshine': 1.9,
 'WindGustDir': 'SW',
 'WindGustSpeed': 35.0,
 'WindDir9am': 'SE',
 'WindDir3pm': 'SE',
 'WindSpeed9am': 19.0,
 'WindSpeed3pm': 15.0,
 'Humidity9am': 55.0,
 'Humidity3pm': 51.0,
 'Pressure9am': 1013.6,
 'Pressure3pm': 1010.7,
 'Cloud9am': 5.0,
 'Cloud3pm': 5.0,
 'Temp9am': 14.2,
 'Temp3pm': 16.9,
 'RainToday': 0}

response = requests.post(url, json=data).json()
print(response)

if response['rain']:
    print("It will rain tomorrow")
else:
    print("It will not rain tomorrow")