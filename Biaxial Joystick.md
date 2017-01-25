# Instructable for Biaxial Joystick

## What We are Doing
This project prints out the X and Y coordinates from a joystick on the serial monitor.

## Hardware
![Joystick](./Joystick.png)

* Joystick module
* Arduino<sup> * </sup>
* USB cable for Arduino
* Male-to-Male connector wires

<sup> * </sup>This example is for an Arduino Uno.

## Libraries
No libraries are required.

## Wiring Diagram

![Joystick](./Biaxial Joystick_bb.png)

## Example Code
```c++
/*
 Pin 1 of the joystick to A0 of the Arduino.
 Pin 2 of the joystick to A1 of the Arduino.
 Pin 3 of the joystick to the 5V power source of the Arduino.
 Pin 4 of the joystick to one of the ground connections on the Arduino.
 */

void setup() {
  Serial.begin(9600);
}

void loop() {
  int joystickXValue = analogRead(A0);
  int joystickYValue = analogRead(A1);
  Serial.print("The X and Y coordinates are:");
  Serial.print(joystickXValue, DEC);
  Serial.print(",");
  Serial.println(joystickYValue, DEC);
  delay(500);
}

```

## Making It Better
* Use the joystick to control a tethered vehicle.

* Use the joystick to remotely control a vehicle.  There are a number of ways to add remote control.  See the WCRS instructables on IR remote, IR transmitter, nRF2401L transceivers, 8266 transceivers, and RFM69HW transceivers.

![Joystick](./WCRS.png)
