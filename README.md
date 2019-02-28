# Trashware 
![Made With Python](https://forthebadge.com/images/badges/made-with-python.svg) ![Built With Love](https://forthebadge.com/images/badges/built-with-love.svg)<br>
![Trashware](https://img.shields.io/badge/Trashware--blue.svg) ![Python 3.7.0](https://img.shields.io/badge/Python-3.7.0-brightgreen.svg)<br><br>
Trashware is a project which aims at environment cleanliness through smart devices. The device hacked in this project uses image recognition to identify recyclable and non-recyclable waste and seperate them in 2 different bins. <br><br>
Here, the PySerial Module(Main_Program.py) is used to get the serial readings from the Arduino UNO. A bluetooth sensor transmits these readings and prints them on the mobile screen as well as in the computer terminal. <br><br>
If the serial readings measure less than 30 cm, then the program runs a python script(Webcam_Capture.py) which uses OpenCV to capture images from the webcam. The captured image is stored in the current directory. Then a second script(Image_Prediction.py) is run which predicts the captured image using the Clarifai API and identifies the object as recyclable or non-recyclable. If the object is recyclable, then the servo motor(Yet to be programmed) is turned 45 degree right which dumps the object into the recyclable bin. And if the object is non-recyclable, then the servo motor is turned 45 degree left which dumps the object into the non-recyclable bin. <br><br>
# Hardware Components 
The Following parts were used to build this project -<br><br>
+   Arduino UNO
+   Ultrasonic Sensor - HCSR04 (Generic)
+   HC-05 Bluetooth Module
+   SG90 Micro-servo Motor<br><br>
<em>Feel free to pull requests and open issues.</em>
