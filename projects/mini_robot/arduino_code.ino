#include <Servo.h>

Servo motor;
int trigPin = 9;
int echoPin = 10;
int motorPin = 3;

void setup() {
  Serial.begin(9600);
  motor.attach(motorPin);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
}

void loop() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  long duration = pulseIn(echoPin, HIGH);
  int distance = duration * 0.034 / 2;

  if (distance < 10) {
    motor.write(0);  // Stop
  } else {
    motor.write(90); // Move Forward
  }
  
  Serial.println(distance);
  delay(500);
}

