void setup() {
  Serial.begin(9600); // Initialize serial communication at 9600 baud rate
}

void loop() {
  int sensorValue = analogRead(A5); // Read the analog voltage from the sensor
  float voltage = sensorValue * (5.0 / 1023.0); // Convert the sensor value to voltage (assuming 5V Arduino)
  

  Serial.print("Voltage: ");
  Serial.print(voltage);
  Serial.println(" V");

  delay(100); // Wait for a second before reading again
}
// geel = GND
// Rood = A5
// Zwart = 5/3.3 V