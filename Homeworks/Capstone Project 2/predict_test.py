import requests

url = 'http://localhost:9696/predict'

data = {'Age': 42,
  'Sex': 'M',
  'ChestPainType': 'ATA',
  'RestingBP': 150,
  'Cholesterol': 268,
  'FastingBS': 0,
  'RestingECG': 'Normal',
  'MaxHR': 136,
  'ExerciseAngina': 'N',
  'Oldpeak': 0.0,
  'ST_Slope': 'Up'}

# this data should return normal 

response = requests.post(url, json=data).json()
print(response)

if response['Heart Disease']:
    print("Heart Disease")
else:
    print("Normal")