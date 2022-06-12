import modi
import time
import numpy
import matplotlib.pyplot as plt

# modi.update_module_firmware()
bundle = modi.MODI()


motor_pi_1 = bundle.motors[0]
motor_pi_2 = bundle.motors[1]
motor_pi_1.speed = 0, 0
motor_pi_2.speed = 0, 0

env = bundle.envs[0]
print(env.red, env.green, env.blue)
time.sleep(4)
print(env.red, env.green, env.blue)

led = bundle.leds[0]
led.rgb = 100, 100, 100

speed = 30
motor_pi_1.speed = speed, speed
motor_pi_2.speed = speed, speed













lights = []
nums = []
plt.figure()
for i in range(1000):
    print(env.red, env.green, env.blue)
    # plt.scatter(i, env.red, s = 0.5, c = 'r')
    # plt.scatter(i, env.green, s = 0.5, c = 'g')
    # plt.scatter(i, env.blue, s = 0.5, c = 'b')
    # plt.scatter(i, env.red + env.green + env.blue, s = 0.5, c = 'k')
    # plt.plot(i, env.red + env.green + env.blue, c = 'b', lw = 1, ls = "-", marker = "o", ms = 1, mfc = "k")
    lights.append(env.red + env.green + env.blue)
    nums.append(i)
    time.sleep(0.05)

plt.plot(nums, lights, c = 'b', lw = 1, ls = "-", marker = "o", ms = 1, mec = "k")

plt.show()

print(numpy.mean(lights))

motor_pi_1.speed = 0, 0
motor_pi_2.speed = 0, 0
