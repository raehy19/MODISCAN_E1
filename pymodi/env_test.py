import modi


# modi.update_module_firmware()

bundle = modi.MODI()


env = bundle.envs[0]
led = bundle.leds[0]
led.rgb = 100,100,100

while 1:
    print(env.red, env.green, env.blue)

