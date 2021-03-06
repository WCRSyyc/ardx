# CIRC09 read Analog temperature
import time
import board
import digitalio
import analogio
import pulseio
import adafruit_motor.servo

led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

pwm = pulseio.PWMOut(board.D6, frequency=50)
                    # may have to tweak the min and max to match individual servos
my_servo = adafruit_motor.servo.Servo(pwm, min_pulse=600, max_pulse=2500)

analog_in = analogio.AnalogIn(board.A1)

def get_temp(pin):
#    print(pin.reference_voltage)   # debugging: max value for ADC: will be 3.3 unless using AREF
#    print((pin.value,))     # debugging: pin.value is an integer from 0 to 65535
                       # 3.3 volt ADC ref voltage so 65535 - 3.3 volts
    return (((pin.value * 3.3 / 65536) - 0.500 ) * 100.0 ) # 10 mV per degree with a 500 mV offset

def map( x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def constrain(y, in_min, in_max):
    if (y < in_min):
        y = in_min
    if (y > in_max):
        y = in_max
    return(y)

while True:
    temperature = get_temp(analog_in)
    temperature = round(temperature, 1)     # don't print extra secimal places
    print((temperature, ))    #if you are using MU : try the plotter !
#    print((temperature, temperature * 9/5 +32 ))    # also print it in Farenheight


    if(temperature > 25):         # light the LED if the temp above threshold
        led.value = True
    else:
        led.value = False
    # constrain the temperature so we don't break the display
    temperature= constrain(temperature, -20, +40)   # centigrade limits of servo's display area
    temperatureServo = map(temperature, -20, 40, 0, 179)    # range to be painted on servo's scale

#    print(temperatureServo)            # map temp range to 180 degrees of servo rotation
    my_servo.angle = temperatureServo  # 3.3 is A to D reference voltage
                                            # 3.3 Volts is also max voltage on analog pin.
                                            # because there is no seperate reference here
                                            # the Arduino uses the supply voltage
    """
    note that the jitter in the servo is due to
    the ADC being only 10 bit even if the library returns a 16 bit value.
    We are only using the lower 1/3 of this renge with this sensor.
    This results in a huge jump in temperature from a small change in the ADC reading.
    this could be remedied by using a higher resolution ADC
    or a different type of sensor.
    """

    time.sleep(0.1)