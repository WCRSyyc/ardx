/** Transistor Test 01
 *
 * Support for experimental setup to test transistor using parts from the
 * standard ARDX kit.  This is intended to be used to verify that transistors are
 * working, and that they are inserted correctly.  It is real easy to get the
 * TO92 case package backwards, reversing (for EBC footprint) the collector and
 * emitter pins.
 *
 * The setup will work to check the functioning of both NPN BJT and N channel FET
 * devices.  Information reported (when transistors are correctly inserted)
 * allows determining the internal (on) resistance, which in turn can be used to
 * calculate the power dissipation for a known load (current).
 *
 * For the circuit, see (exports from) TransistorTest01.fzz
 * That shows switches connecting different compoents to the breadboard.  In
 * reality, the switches do not exist.  The transistor to test is inserted in
 * the appropriate position (based on the footprint).  The switches are just a
 * convenient way to show the logical setup on the schematic.
 *
 * Multiple points in the circuit are connected to analog input pins.
 * Measurements at these points are used to determine information about the
 * transistor being tested, and the load the circuit is putting on the Arduino
 * board.  See http://playground.arduino.cc/Main/ArduinoPinCurrentLimitations
 * for some information about the limits.  NOTE: the information shown on that
 * page are MAXIMUM limits.  It is not a good idea to run at the maximums.  That
 * is why the voltage at the digital output pins is (also) being monitored.  The
 * internal resistance of the atmel chip means that those will (likely) be less
 * than the (nominal) 5V supply voltage.  The voltage drop accross the known
 * value current limiting base drive resistor is used to calculate the actual
 * current sourced from the Arduino pin.
 *
 * The final 2 test cases simultaneously enable multiple control pins.  Comparing
 * those results with the single control pin cases will show how close to `full`
 * on a BJT transistor is.  When a transitor is only partially on, the effective
 * internal resistance is greater, resulting in a higher voltage at the load.
 * Since power is voltage times current, that can mean the transistor is
 * disipating more heat.
 *
 * modified 26 Nov 2018
 * by H Phil Duby
 *
 * This example code is in the public domain
 */

// Constants used to convert measurements into actual voltage values
const uint16_t maxAnalog = 1023; // Maximum 10 bit ADC value
const uint16_t minAnalog = 0; // Minimum 10 bit ADC value
const uint16_t vcc = 5000; // millivolts (VCC, 5 volts)
const uint16_t gnd = 0;

const uint32_t settleTime = 1000; // 1 second to make sure everything stable
const uint32_t sampleInterval = 20; // time between measurement sets (µS)
const uint32_t cycleInterval = 10000; // time between test cycles
const uint32_t stableInterval = 3000; // mS to leave spinning after reporting

// Pin numbers used to make voltage measurements in the circuit
const int sourcePin[] = {A3, A2, A1, A0}; // Tied to source drive digital pins
const int loadPin = A4; // Low end of the load (transistor collector or source)
const int controlPin = A5; // Control pin of the transistor (base or gate)
const uint16_t sourcingCnt = sizeof(sourcePin) / sizeof(int);
const uint16_t measurementCount = 2 + sourcingCnt;

// Pin numbers used to supply drive (voltage or current) for the transistor
const int drivePin[] = {8, 9, 10, 11};
const uint16_t controlCount = sizeof(drivePin) / sizeof(int);

const uint16_t sampleSize = 120;
uint16_t raw[measurementCount][sampleSize]; // recorded raw measurements
uint16_t setNumber = 0;

void setup()
{
  Serial.begin(9600);
  setControlFloat(); // Let all control inputs `float`
  delay(settleTime); // Make sure everything is stable before starting
}

void loop()
{
  takeMeasurements();
  Serial.println(F("All Floating"));
  reportMeasurements();

  sourceFrom(drivePin[3]); // 2.2k == standard ARDX motor spin configuration
  digitalWrite(drivePin[3], LOW); // Override default to force off
  takeMeasurements();
  Serial.println(F("Explicit off"));
  reportMeasurements();

  for(uint16_t cntrl = 0; cntrl < controlCount; cntrl++) {
    sourceFrom(drivePin[cntrl]);
    takeMeasurements();
    Serial.print(F("Only control source "));
    Serial.println(cntrl);
    reportMeasurements();
  }

  sourceFrom(drivePin[0]);
  addSource(drivePin[1]); // Parallel 2 input control sources
  takeMeasurements();
  Serial.println(F("Multiple control sources: 0+1"));
  reportMeasurements();

  addSource(drivePin[2]); // Parallel 3 input control sources
  takeMeasurements();
  Serial.println(F("Multiple control sources: 0+1+2"));
  reportMeasurements();

  sourceFrom(drivePin[3]);
  sourceFrom(drivePin[3]); // 2.2k == standard ARDX motor spin configuration
  digitalWrite(drivePin[3], LOW); // Override default to force off
  delay(cycleInterval);
}

/** Set all input control pins to high impedance inputs
 *
 */
void setControlFloat() {
  for(uint16_t i = 0; i < controlCount; i++) {
    pinMode(i, INPUT); // float the input control signal
  }
}

void sourceFrom(uint16_t controlPin) {
  // Make sure that all (other) control pins are not being used
  setControlFloat();
  addSource(controlPin);
}

void addSource(uint16_t controlPin) {
  pinMode(controlPin, OUTPUT);
  digitalWrite(controlPin, HIGH);
}

void takeMeasurements() {
  for(uint16_t reading = 0; reading < measurementCount; reading++) {
    // Get readings from each of the (possibly) current sourceing pins
    for(uint16_t source = 0; source < sourcingCnt; source++) {
      raw[source][reading] = analogRead(sourcePin[source]);
    }
    raw[sourcingCnt][reading] = analogRead(controlPin);
    raw[sourcingCnt + 1][reading] = analogRead(loadPin);
  }
  delayMicroseconds(sampleInterval);
}

void reportMeasurements() {
  Serial.print(F("Set "));
  Serial.println(setNumber++);
  Serial.print(F("Load "));
  reportSamples(sourcingCnt + 1);
  Serial.print(F("Control "));
  reportSamples(sourcingCnt);
  Serial.println(F("Sources "));
  for(uint16_t src = 0; src < sourcingCnt; src++) {
    Serial.print(F("Source "));
    Serial.print(src);
    Serial.print(F(": "));
    reportSamples(src);
  }
  delay(stableInterval); // Leave long enough for manual verification of motor spin
}

void reportSamples(uint16_t source) {
  reportOneSample(source, 0);
  for(uint16_t smpl = 1; smpl < sampleSize; smpl++) {
    Serial.print(F(", "));
    reportOneSample(source, smpl);
  }
  Serial.println();
}

void reportOneSample(uint16_t source, uint16_t sample) {
  uint16_t reading;
  reading = map(raw[source][sample], minAnalog, maxAnalog, gnd, vcc);
  Serial.print(reading);
}
