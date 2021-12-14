import requests

url = 'http://localhost:9696/predict'

data = {'Location': 'Ballarat',
 'MinTemp': 6.5,
 'MaxTemp': 11.2,
 'Rainfall': 4.8,
 'Evaporation': 4.8,
 'Sunshine': 8.4,
 'WindGustDir': 'W',
 'WindGustSpeed': 52.0,
 'WindDir9am': 'W',
 'WindDir3pm': 'WSW',
 'WindSpeed9am': 31.0,
 'WindSpeed3pm': 28.0,
 'Humidity9am': 99.0,
 'Humidity3pm': 95.0,
 'Pressure9am': 1010.4,
 'Pressure3pm': 1012.6,
 'Cloud9am': 8.0,
 'Cloud3pm': 8.0,
 'Temp9am': 8.5,
 'Temp3pm': 10.8,
 'RainToday': 1}

response = requests.post(url, json=data).json()
print(response)

if response['rain']:
    print("It will rain tomorrow")
else:
    print("It will not rain tomorrow")