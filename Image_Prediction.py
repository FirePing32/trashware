""" Clarifai API v2.0 """
import os
from os.path import join, dirname
from dotenv import load_dotenv
from clarifai.rest import ClarifaiApp

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path) #loading env variables

app = ClarifaiApp(api_key=os.getenv('CLARIFAI_API_KEY')) #init Clarifai app

model = app.models.get('Trash')
model.train() #training app with custom model 'Trash'

file = 'capture.jpg' #output image
response = model.predict_by_filename(filename=file) #predicting image by sending requests to api.clarifai.com (v2)

waste = dict(response) #initializing JSON response as a dict
waste_type = waste['outputs'][0]['data']['concepts'] #filtering to get int() values

biodegradable_value = []
non_biodegradable_value = []

def entering_data():
    #when biodegradable value is greater
    if waste_type[0]['id'] == 'Biodegradable':
        biodegradable_value.append(waste_type[0]['value'])
        non_biodegradable_value.append(waste_type[1]['value'])
    #vice versa
    else:
        biodegradable_value.append(waste_type[1]['value'])
        non_biodegradable_value.append(waste_type[0]['value'])

def reading_data():
    #servo code will be added in the future. Watch the repository.
    if biodegradable_value >= non_biodegradable_value:
        print("Servo code here")

    else:
        print("Servo code here")

entering_data()
reading_data()