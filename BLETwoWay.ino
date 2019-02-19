#include <AltSoftSerial.h>
AltSoftSerial BTserial;

// IO
const int buttonPin = 2; //NOTE: Change to the pin where your button is connected

// state
boolean asleep = false;
int buttonState = HIGH;
boolean confirmedCentral = false;

// data
char lastChar = 0;
char writeBuffer[32];
int readValue1 = 0;
int readValue2 = 0;
int readValue3 = 0;

int hrValue = 0;
boolean newHR = false;
char hrBuffer[10];

int stepValue = 0;
boolean newStep = false;
char stepBuffer[10];

// --------------------------------------------------------------------------------
// Grab new samples at 20Hz
// --------------------------------------------------------------------------------
unsigned long startTime = 0;
unsigned long endTime = 0;
unsigned long period_us = 50000; // 20Hz
bool grabSamples()
{
  bool newSamples = false;
  endTime = micros();
  if (endTime - startTime >= period_us) {
    readValue1 = analogRead(A0);  // read a sample from A0
    readValue2 = analogRead(A1);  // read a sample from A1
    readValue3 = analogRead(A2);  // read a sample from A2
    startTime = endTime;          // “reset” the timer
    newSamples = true;
  }
  return newSamples;
}

// --------------------------------------------------------------------------------
// Receive Data from Python
// Format:
// AT**** == connection attempt commands from Python 
// H****, == heart rate being sent, delimited by a comma
// S****, == step count being sent, delimited by a comma
// --------------------------------------------------------------------------------
void receiveData( char newChar ) 
{
  // If Python is sending any AT commands, tell it the connection is confirmed
  // If Python is sending data values, read a string until the termination character (',')
  // HUGE NOTE!!!
  // 1) Lines end in commas ","
  // 2) Heart Rate is prefaced with an "H" character
  //    - Example: "H53," is a heart rate value of 53 BPM
  // 3) Step count is prefaced with an "S" character
  //    - Example: "S3245," is a step count of 3245
  switch(newChar) {
    case 'A': // starting AT Command reading
      lastChar = newChar;
      break;
    case 'T': // AT was received
      if (lastChar == 'A') {
        BTserial.write("PeripheralConnected");
        delay(50); BTserial.flushInput(); // purge buffer
        confirmedCentral = true;
        lastChar = 0;
      }
      break;
    case 'H': // starting Heart Rate reading
      lastChar = newChar;
      strcpy(hrBuffer, "");
      break;
    case 'S': // starting Step Count reading
      lastChar = newChar;
      strcpy(stepBuffer, "");
      break;
    case ',': // line ending received
      if (lastChar == 'H') {
        hrValue = atoi(hrBuffer);
        newHR = true;
        lastChar = 0;
      }
      if (lastChar == 'S') {
        stepValue = atoi(stepBuffer);
        newStep = true;
        lastChar = 0;
      }
      break;
    case 0: // no message ("reset")
      lastChar = 0;
    default: // receiving data
      if (lastChar == 'H')
        sprintf(hrBuffer, "%s%c", hrBuffer, newChar);
      if (lastChar == 'S')
        sprintf(stepBuffer, "%s%c", stepBuffer, newChar);
      break;
  }
}

// --------------------------------------------------------------------------------
// Button logic to toggle sleep state
// --------------------------------------------------------------------------------
void checkButton() {
  //Upon button press, disconnect/reconnect BLE (debounce the button for more stable code)
  if(digitalRead(buttonPin) != buttonState) {
    buttonState = !buttonState;

    //Disconnect and put to sleep
    if(buttonState == HIGH && !asleep) {
      //Serial.println("Going to sleep!");
      BTserial.print("OK+LOST"); // just in case it doesn't get written before going to sleep
      delay(50);
      BTserial.print("AT");
      delay(150);
      BTserial.print("AT+ADTY3");
      delay(50);
      BTserial.print("AT+SLEEP");
      delay(50);
      confirmedCentral = false;
      asleep = true;
    }
    //Wake up and re-establish connection 
    else if(buttonState == HIGH && asleep) {
      //Serial.println("Waking up!");
      BTserial.print("AT+hailramsinhailramsinhailramsinhailramsinhailramsinhailramsinhailramsinhailramsin");
      delay(350);
      BTserial.print("AT+ADTY0");
      delay(50);
      BTserial.print("AT+RESET");
      delay(50);
      BTserial.flushInput(); // purge buffer
      asleep = false;
    }
  }
}

// --------------------------------------------------------------------------------
// Basic Arduino Setup
// -------------------------------------------------------------------------------- 
void setup()
{
  pinMode(buttonPin, INPUT_PULLUP);
  BTserial.begin(9600);
  Serial.begin(9600);
}

// --------------------------------------------------------------------------------
// Main Arduino Code
// -------------------------------------------------------------------------------- 
void loop()
{
  // Check if the button was pressed
  checkButton();

  // --------------------------------------------------------------------------------
  // Main code (only when awake!)
  // --------------------------------------------------------------------------------
  if (!asleep) {
    // If Central BLE is sending data, receive it
    if (BTserial.available()) {
      receiveData(BTserial.read());
    }
  
    // Send/receive data to/from the Central BLE if we are connected
    if (confirmedCentral) {
      
      // ----------------------------------------
      // JUST AN EXAMPLE!!!
      // Sending data readings terminated by commas
      // TODO: Change the variables being writen 
      if (grabSamples()) {
        sprintf(writeBuffer, "%d %d %d,", readValue1, readValue2, readValue3);
        BTserial.print(writeBuffer);
      }

      // ----------------------------------------
      // JUST AN EXAMPLE!!!
      // If received new HR/SC values, print them to Serial
      // TODO: WRITE THESE TO OLED
      if (newHR) {
        Serial.print("HR : ");
        Serial.println(hrValue);
        newHR = false;
      }
      if (newStep) {
        Serial.print("Step Count : ");
        Serial.println(stepValue);
        newStep = false;
      }
      // ----------------------------------------

    }
  }
}
