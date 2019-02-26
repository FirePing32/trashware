int triggerPin = 7; //triggering on pin 7
int echoPin = 8;    //echo on pin 8
int info = 0; //variable for the information comming from the sensor module

void setup() { //we will be combinig both setups from the codes
  
  Serial.begin(9600);  //we'll start serial comunication, so we can see the distance on the serial monitor
  pinMode(triggerPin, OUTPUT); //defining pins
  pinMode(echoPin, INPUT);
  
}

void loop(){ //here we combine both codes to work in the loop
  bluetooth();
  sensor();
}

void bluetooth() { //loop from the bluetooth code is renamed to "bluetooth" void
  if(Serial.available() > 0){  //if there is any information comming from the serial lines...
    info = Serial.read();
  }
}

void sensor() { //loop from the sensor code is renamed to the "sensor" void
  
  int duration, distance;    //Adding duration and distance
  
  digitalWrite(triggerPin, HIGH); //triggering the wave(like blinking an LED)
  delay(10);
  digitalWrite(triggerPin, LOW);
  
  duration = pulseIn(echoPin, HIGH); //a special function for listening and waiting for the wave
  distance = (duration/2) / 29.1; //transforming the number to cm(if you want inches, you have to change the 29.1 with a suitable number
  
  Serial.print(distance);    //printing the numbers
  Serial.println(" ");      //just printing to a new line
  delay(500);

  if(distance <= 30){ 
    Serial.println("Object Found !");
    Serial.println("Running Scripts...");
    Serial.println("Processing...");
    delay(10000); //so the stopping is visible
  }
}
