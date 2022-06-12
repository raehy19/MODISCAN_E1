import modi


# modi.update_module_firmware()

bundle = modi.MODI()
#
# print(str(bundle.motors[0], bundle.motors[1], bundle.motors[2]))

print(bundle.motors[0], bundle.motors[1], bundle.motors[2])

if str(bundle.motors[0]) == "Motor (2900)":
    print("2900")

if str(bundle.motors[0]) == "Motor (1013)":
    print("1013")

if str(bundle.motors[0]) == "Motor (2950)":
    print("2950")

bundle.motors[0].speed = 100, 100