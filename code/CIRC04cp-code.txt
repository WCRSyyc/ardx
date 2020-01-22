#CIRC04 control a servo Version three
# https://learn.adafruit.com/using-servos-with-circuitpython/high-level-servo-control

import board
import pulseio
import time
import adafruit_motor.servo

print("starting")
pwm = pulseio.PWMOut(board.D6, frequency=50)
my_servo = adafruit_motor.servo.Servo(pwm, min_pulse=500, max_pulse=2500)

while True:
  for angle in range(0, 180, 45):  # 0 - 180 degrees, 5 degrees at a time.
    print(angle-90)
    my_servo.angle = angle
    time.sleep(6.0)

  for angle in range(180, 0, -45): # 180 - 0 degrees, 5 degrees at a time.
    print(angle-90)
    my_servo.angle = angle
    time.sleep(6.0)