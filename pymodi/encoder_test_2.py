import modi
import time

# 모디 업데이트
# modi.update_module_firmware()


# 모디 연결
bundle = modi.MODI()

# 모터 연결 + 초기화
motor_arm = bundle.motors[0]
motor_arm.first_speed = 0
motor_arm.second_speed = 0

# 버튼 연결
button = bundle.buttons[0]

# ir센서
ir_encoder_1 = bundle.irs[0]
ir_encoder_2 = bundle.irs[1]
print(f"ir sensor init : {ir_encoder_1.proximity, ir_encoder_2.proximity}")

# 엔코더로 왼쪽 모터 회전 - 30도
def motor_arm_left_move(ir, speed):
    # 엔코더 값 클때
    if ir.proximity > 60:
        while ir.proximity > 45:
            print(ir.proximity)
            motor_arm.first_speed = speed
            time.sleep(0.00001)
            motor_arm.first_speed = 0
            time.sleep(0.1)
        motor_arm.first_speed = 0
        print(ir.proximity)
        print("ir high -> low")
    # 엔코더 센서 값 작을때
    else:
        while ir.proximity < 75:
            print(ir.proximity)
            motor_arm.first_speed = speed
            time.sleep(0.00001)
            motor_arm.first_speed = 0
            time.sleep(0.1)
        time.sleep(0.001)
        motor_arm.first_speed = 0
        print(ir.proximity)
        print("ir low -> high")

# 엔코더로 오른쪽 모터 회전 - 30도
def motor_arm_right_move(ir, motor, speed):
    # 엔코더 값 클때
    if ir.proximity > 60:
        while ir.proximity > 45:
            print(ir.proximity)
            motor.second_speed = speed
            time.sleep(0.00001)
            motor.second_speed = 0
            time.sleep(0.1)
        motor.second_speed = 0
        print(ir.proximity)
        print("ir high -> low")
    # 엔코더 센서 값 작을때
    else:
        while ir.proximity < 75:
            print(ir.proximity)
            motor.second_speed = speed
            time.sleep(0.00001)
            motor.second_speed = 0
            time.sleep(0.1)
        time.sleep(0.001)
        motor.second_speed = 0
        print(ir.proximity)
        print("ir low -> high")

global current_angle_left
global current_angle_right

def move_arm(t1, t2, v1, v2):
    global current_angle_left
    global current_angle_right

    left_count = (t1 - current_angle_left)//2
    if left_count > 0:
        for i in range(0, left_count):
            motor_arm_left_move(ir_encoder_1, v1)
    if left_count < 0:
        left_count = -left_count
        for i in range(0, left_count):
            motor_arm_left_move(ir_encoder_1, -v1)
    current_angle_left = t1

    right_count = (t2 - current_angle_left)//2
    if right_count > 0:
        for i in range(0, right_count):
            motor_arm_right_move(ir_encoder_2, v2)
            right_count = -right_count
    if right_count > 0:
        for i in range(0, right_count):
            motor_arm_right_move(ir_encoder_2, -v2)
    current_angle_right = t2


