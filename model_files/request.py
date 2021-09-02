import requests
vehicle_config={
    "Cylinders": [4,6,8],
    "Displacement":[155.0,160.0,165.0],
    "HorsePower":[93.0,130.0,98.0],
    "Weight":[2500.0,3150.0,2600.0],
    "Acceleration":[15.0,14.0,16.0],
    "Model Year":[81,80,78],
    "Origin":[3,2,1]
}

url = 'https://prediction-fuel-efficiency1.herokuapp.com/'
r = requests.post(url,json=vehicle_config)
r.text.strip()
print(r.json()) #{'mpg_predictions': [33.17, 19.01, 21.25]}