#CIRC04 control a servo Version two

import board
import pulseio

import adafruit_motor.servo

pwm = pulseio.PWMOut(board.D6, frequency=50)
servo = adafruit_motor.servo.Servo(pwm, min_pulse=750, max_pulse=2250)

while True:
  for angle in range(0, 180, 45):  # 0 - 180 degrees, 5 degrees at a time.
    print(angle)
    my_servo.angle = angle
    time.sleep(2)

  for angle in range(180, 0, -45): # 180 - 0 degrees, 5 degrees at a time.
    print(angle)
    my_servo.angle = angle
    time.sleep(2)