import serial
import subprocess
import sys 
import time

port = 'COM3'
rate = 9600

arduino = serial.Serial(port, rate)
    
while True:
    
    def main_prog():
        reading = arduino.readline().decode("ascii").strip()
        print(reading)

        try:
            if int(reading) <= 30:
                time.sleep(2)
                capture = subprocess.Popen([sys.executable, "Webcam_Capture.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                predict = subprocess.Popen([sys.executable, "Image_Prediction.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                time.sleep(2)

        except ValueError:
            pass

    main_prog()