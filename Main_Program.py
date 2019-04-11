import serial
import subprocess
import sys 
import time
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path) #setting env variables

port = os.getenv('PORT')
rate = int(os.getenv('RATE'))

arduino = serial.Serial(port, rate) #establish serial communication
    
while True:
    
    def main_prog():
        reading = arduino.readline().decode("ascii").strip() #removing ascii characters
        print(reading)

        try:
            if int(reading) <= 30: #when object in range of 30 cm
                time.sleep(2)
                #calling CMD processes
                capture = subprocess.Popen([sys.executable, "Webcam_Capture.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                predict = subprocess.Popen([sys.executable, "Image_Prediction.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                time.sleep(2)

        except ValueError:
            pass

    main_prog()