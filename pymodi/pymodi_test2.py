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


# # 센서 무한측정 test
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


# 층별로 탐색하는 함수, 층마다 arm의 각도를 다르게 해야하므로 다르게 구성
# time을 쪼개 시간단위로 얼마나 가서 일정거리 이하인지 = 측정되었는지를 확인
def detect_layer_1(ir1, motor):
    time_checker = 0
    while ir1.proximity < 95:
        motor.speed = 55, 35
        time.sleep(0.05)
        time_checker += 1
    motor.speed = 0, 0
    for i in range(0, time_checker):
        motor.speed = -53, -45
        time.sleep(0.035)
    motor.speed = 0, 0
    return time_checker

def detect_layer_2(ir1, motor):
    time_checker = 0
    while ir1.proximity < 95:
        motor.speed = 55, 40
        time.sleep(0.05)
        time_checker += 1
    motor.speed = 0, 0
    for i in range(0, time_checker):
        motor.speed = -53, -50
        time.sleep(0.03)
    motor.speed = 0, 0
    return time_checker

# 한 층을 측정한 다음 다음층으로 탐침부 헤드를 이동시키는 함수
def layer_up(motor):
    motor.speed = 100, -100
    time.sleep(0.3)
    motor.speed = 30, 0
    time.sleep(0.1)
    motor.speed = 0, 0

# test main -------------------------------------------------------------------------------------------
# 위 함수들로 만든 메인 스캔 함수 시간단위로 스캔해 아래층부더 차례대로 layer 1,2,3,4,5,6이다.
# 측정하는데 걸린 시간 단위를 길이로 변환하는것이 필요
layer_1 = detect_layer_1(ir1, motor)
layer_up(motor)
layer_2 = detect_layer_1(ir1, motor)
layer_up(motor)
layer_3 = detect_layer_1(ir1, motor)
layer_up(motor)
layer_4 = detect_layer_2(ir1, motor)
layer_up(motor)
layer_5 = detect_layer_2(ir1, motor)
layer_up(motor)
layer_6 = detect_layer_2(ir1, motor)
layer_up(motor)

print(f"layers-----")
print(layer_1)
print(layer_2)
print(layer_3)
print(layer_4)
print(layer_5)
print(layer_6)