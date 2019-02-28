> # Trashware 
![Made With Python](https://forthebadge.com/images/badges/made-with-python.svg) ![Built With Love](https://forthebadge.com/images/badges/built-with-love.svg)<br>
![Trashware](https://img.shields.io/badge/Trashware--blue.svg) ![Python 3.7.0](https://img.shields.io/badge/Python-3.7.0-brightgreen.svg)<br><br>
Trashware is a project which aims at environment cleanliness through smart devices. The device hacked in this project uses image recognition to identify recyclable and non-recyclable waste and seperate them in 2 different bins. <br><br>
> # Hardware 
The following parts were used to build this project -<br><br>
+   Arduino UNO
+   Ultrasonic Sensor - HCSR04 (Generic)
+   HC-05 Bluetooth Module
+   SG90 Micro-servo Motor<br><br>
> # Software 
The following software packages were used to power this project -<br><br>
+   Arduino IDE
+   OpenCV
+   Python
+   Clarifai REST API<br><br>
> # How To Build
1. Connect the ultrasonic sensor and the bluetooth module according to the configurations in the <code>ultrasonic_with_bluetooth/ultrasonic_with_bluetooth.ino</code> file.
2. Upload the <code>.ino</code> file to the Arduino and connect it to your computer.
3. Now configure the software part. Inside the project directory, run the following commands -<br><br>
   +   <pre><code>virtualenv Trashware</code></pre>
   +   For Windows -<br>
        +   <pre><code>cd Trashware/Scripts && activate</code></pre>
       For Linux and Mac -<br>
        +   <pre><code>source Trashware/bin/activate</code></pre>
4. Now run the ``Main_Program.py`` in terminal
5. If everything went well, then the program will display the ultrasonic sensor readings on the screen. You can also view the sensor readings on your Android or IOS device by downloading an arduino emulator.
6. If an object is kept in the range of 30 cm in front of the ultrasonic sensor, then the ``Webcam_Capture.py`` captures the image through a webcam connected to computer, and the ``Image_Prediction.py`` predicts the captured image and classifies it as recyclable or non-recyclable.
7. If the object is recyclable, then the servo motor turns 45 degree right, dumping it in the recyclable bin. And if the object is non-recyclable, then the servo motor turns 45 degree left dumping it in the non-recyclable bin. 
> ##### Note - The code for the servo motor will be added in the future commits. Watch the repository for changes.
<br>
<em>Share and fork the project if you would like to.</em>
<em>Feel free to pull requests and open issues.</em>
