import modi
import time

bundle = modi.MODI()

motor = bundle.motors[0]

ir1 = bundle.irs[0]
ir2 = bundle.irs[1]
ir3 = bundle.irs[2]

while ir1.proximity > 80:
    motor.first_speed = 1

motor.first_speed = 0