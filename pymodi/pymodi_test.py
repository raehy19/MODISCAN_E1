import modi
import time

# modi.update_module_firmware()
bundle = modi.MODI()

# 모터 한쌍 사용(각 팔 관절)
motor = bundle.motors[0]
motor.first_speed = 0
motor.second_speed = 0

# ir센서 3개 사용(하나는 스캔, 두개는 엔코더용)
ir1 = bundle.irs[0]
ir2 = bundle.irs[1]
ir3 = bundle.irs[2]
time.sleep(1)

# # 센서 무한측정
# while 1:
#     print(ir1.proximity, ir2.proximity, ir3.proximity)

# 엔코더로 모터 회전 - 방향별, 60도씩
def motor1_clock1(ir3, motor):
    if ir3.proximity > 85:
        while ir3.proximity > 55:
            motor.first_speed = -40
        while ir3.proximity < 85:
            motor.first_speed = -40
        motor.first_speed = 0
    else:
        while ir3.proximity < 85:
            motor.first_speed = -40
        # while ir3.proximity > 55:
        #     motor.first_speed = -40
        motor.first_speed = 0

def motor1_counterclock1(ir3, motor):
    if ir3.proximity > 85:
        while ir3.proximity > 55:
            motor.first_speed = 40
        while ir3.proximity < 85:
            motor.first_speed = 40
        motor.first_speed = 0
    else:
        while ir3.proximity < 85:
            motor.first_speed = 40
        # while ir3.proximity > 55:
        #     motor.first_speed = 40
        motor.first_speed = 0

def motor2_clock1(ir2, motor):
    if ir2.proximity > 80:
        while ir2.proximity > 45:
            motor.second_speed = -40
        while ir2.proximity < 80:
            motor.second_speed = -40
        motor.second_speed = 0
    else:
        while ir2.proximity < 80:
            motor.second_speed = -40
        # while ir2.proximity > 45:
        #     motor.second_speed = -40
        motor.second_speed = 0

def motor2_counterclock1(ir2, motor):
    if ir2.proximity > 80:
        while ir2.proximity > 45:
            motor.second_speed = 40
        while ir2.proximity < 80:
            motor.second_speed = 40
        motor.second_speed = 0
    else:
        while ir2.proximity < 80:
            motor.second_speed = 40
        # while ir2.proximity > 45:
        #     motor.second_speed = 40
        motor.second_speed = 0

# 엔코더를 사용하여 일정 각도만큼씩 회전



# main ------------
# 물체를 감지할때까지 index 늘리며 두 모터 60도씩 회전
index = 0
while ir1.proximity < 40:
    print(ir1.proximity, ir2.proximity, ir3.proximity)
    motor1_counterclock1(ir3, motor)
    motor2_counterclock1(ir2, motor)
    index += 1
print("detected")
time.sleep(3)
for i in range(0, index):
    print(ir1.proximity, ir2.proximity, ir3.proximity)
    motor2_clock1(ir2, motor)
    motor1_clock1(ir3, motor)

motor.first_speed = 0
motor.second_speed = 0
