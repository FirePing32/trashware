""" Clarifai API v2.0 """
import os
from os.path import join, dirname
from dotenv import load_dotenv
from clarifai.rest import ClarifaiApp

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

app = ClarifaiApp(api_key=os.getenv('CLARIFAI_API_KEY'))

model = app.models.get('Trash')
model.train()

file = 'capture.jpg'
response = model.predict_by_filename(filename=file)

waste = dict(response)
waste_type = waste['outputs'][0]['data']['concepts']

biodegradable_value = []
non_biodegradable_value = []

def entering_data():

    if waste_type[0]['id'] == 'Biodegradable':
        biodegradable_value.append(waste_type[0]['value'])
        non_biodegradable_value.append(waste_type[1]['value'])

    else:
        biodegradable_value.append(waste_type[1]['value'])
        non_biodegradable_value.append(waste_type[0]['value'])

def reading_data():

    if biodegradable_value >= non_biodegradable_value:
        print("Servo code here")

    else:
        print("Servo code here")

entering_data()
reading_data()