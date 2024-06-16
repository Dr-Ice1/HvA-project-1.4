// Define the analog pin for the IR sensor
const int irSensorPin = A5;

// Variable to store the sensor value
int sensorValue = 0;

void setup() {
  // Initialize serial communication at 9600 bits per second
  Serial.begin(9600);
}

void loop() {
  // Read the analog value from the IR sensor
  sensorValue = analogRead(irSensorPin);
  
  // Get the current time in milliseconds
  unsigned long currentTime = millis();
  
  // Print the timestamp, sensor value, and corresponding voltage to the Serial Monitor
  Serial.print(currentTime);
  Serial.print(" ");
  Serial.println(sensorValue);

  // Wait for 10 milliseconds before the next loop
  delay(10);
}
