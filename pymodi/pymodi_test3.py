import modi
import time
import numpy

# modi.update_module_firmware()

bundle = modi.MODI()

# 모터 6개
motor_arm = bundle.motors[0]
motor_pi_1 = bundle.motors[1]
motor_pi_2 = bundle.motors[2]

motor_arm.first_speed = 100
motor_arm.second_speed = 100

motor_pi_1.first_speed = 100
motor_pi_1.second_speed = 100
motor_pi_2.first_speed = 100
motor_pi_2.second_speed = 100

env = bundle.envs[0]
led = bundle.leds[0]
led.rgb = 100, 100, 100

print(env.red, env.blue, env.green)

reds = []
greens = []
blues = []

time.sleep(3)
while 1:
    reds.append(env.red)
    greens.append(env.green)
    blues.append(env.blue)
    # print(env.red, env.green, env.blue)
    print(f"{max(reds)}, {min(reds)}, {numpy.mean(reds)} / {max(greens)}, {min(greens)}, {numpy.mean(greens)} / {max(blues)}, {min(blues)}, {numpy.mean(blues)}")