from math import pi, sqrt, sin, cos, acos, atan2, isclose, floor, ceil

import modi
import time

# modi
# ==================================================

# 모디 업데이트
# modi.update_module_firmware()

# 모디 연결
bundle = modi.MODI()

# 모터 연결 + 초기화
if str(bundle.motors[0]) == "Motor (2900)":
    motor_arm = bundle.motors[0]
    motor_arm.first_speed = 0
    motor_arm.second_speed = 0
    motor_pi_1 = bundle.motors[1]
    motor_pi_2 = bundle.motors[2]
    motor_pi_1.first_speed = 0
    motor_pi_1.second_speed = 0
    motor_pi_2.first_speed = 0
    motor_pi_2.second_speed = 0
elif str(bundle.motors[1]) == "Motor (2900)":
    motor_arm = bundle.motors[1]
    motor_arm.first_speed = 0
    motor_arm.second_speed = 0
    motor_pi_1 = bundle.motors[0]
    motor_pi_2 = bundle.motors[1]
    motor_pi_1.first_speed = 0
    motor_pi_1.second_speed = 0
    motor_pi_2.first_speed = 0
    motor_pi_2.second_speed = 0
elif str(bundle.motors[2]) == "Motor (2900)":
    motor_arm = bundle.motors[2]
    motor_arm.first_speed = 0
    motor_arm.second_speed = 0
    motor_pi_1 = bundle.motors[0]
    motor_pi_2 = bundle.motors[1]
    motor_pi_1.first_speed = 0
    motor_pi_1.second_speed = 0
    motor_pi_2.first_speed = 0
    motor_pi_2.second_speed = 0
else :
    print("motor error")

print("motor connected")

# 컬러센서 연결
env = bundle.envs[0]
print(f"env sensor init : {env.red, env.green, env.blue}")

# ir센서 3개 연결 + 초기화 (하나는 스캔, 두개는 엔코더용)
if str(bundle.irs[0]) == "Ir (771)":
    ir_head = bundle.irs[0]
elif str(bundle.irs[1]) == "Ir (771)":
    ir_head = bundle.irs[1]
elif str(bundle.irs[2]) == "Ir (771)":
    ir_head = bundle.irs[2]
else:
    print("ir error")

if str(bundle.irs[0]) == "Ir (2500)":
    ir_encoder_left = bundle.irs[0]
elif str(bundle.irs[1]) == "Ir (2500)":
    ir_encoder_left = bundle.irs[1]
elif str(bundle.irs[2]) == "Ir (2500)":
    ir_encoder_left = bundle.irs[2]
else:
    print("ir error")

if str(bundle.irs[0]) == "Ir (3201)":
    ir_encoder_right = bundle.irs[0]
elif str(bundle.irs[1]) == "Ir (3201)":
    ir_encoder_right = bundle.irs[1]
elif str(bundle.irs[2]) == "Ir (3201)":
    ir_encoder_right = bundle.irs[2]
else:
    print("ir error")

print(f"ir sensor init : {ir_encoder_left.proximity, ir_encoder_right.proximity, ir_head.proximity}")

# 버튼 연결
button = bundle.buttons[0]
print("button connected")

# led 연결
led = bundle.leds[0]
led.rgb = 100, 100, 100
print("led connected")

# 스피커
speaker = bundle.speakers[0]
speaker.volume = 100
print("speaker conneted")
time.sleep(0.5)
speaker.volume = 0

# ==================================================

global current_angle_left
global current_angle_right

a = 0.5665
b = 1.6995

def stick(v, *vstick) :
    for vs in vstick[:-1] :
        v = vs if isclose(v, vs, abs_tol = vstick[-1]) else v
    return v

def inRange(v, minV, maxV) :
    return v >= minV and v <= maxV

def theta2pos(ti, tj) :
    sti = sin(ti)
    stj = sin(tj)
    cti = cos(ti)
    ctj = cos(tj)
    L = [a + sti + stj, ctj - cti]
    M = [(sti - stj) / 2, 1 - (cti + ctj) / 2]
    L2 = L[0] * L[0] + L[1] * L[1]
    L1 = sqrt(L2)
    k = sqrt(b * b - L2 / 4)
    return [M[0] - L[1] / L1 * k, M[1] + L[0] / L1 * k]

def pos2theta(x, y) :
    Ri = [x - a / 2, y - 1]
    Rj = [- x - a / 2, y -1]
    Ri2 = Ri[0] * Ri[0] + Ri[1] * Ri[1]
    Rj2 = Rj[0] * Rj[0] + Rj[1] * Rj[1]
    Ri1 = sqrt(Ri2)
    Rj1 = sqrt(Rj2)
    ti = atan2(Ri[1], Ri[0]) + pi / 2
    tj = atan2(Rj[1], Rj[0]) + pi / 2
    dti = acos((Ri2 + 1 - b * b) / 2 / Ri1)
    dtj = acos((Rj2 + 1 - b * b) / 2 / Rj1)
    tiA = stick(ti + dti, 0, pi, 0.001)
    tiB = stick(ti - dti, 0, pi, 0.001)
    tjA = stick(tj + dtj, 0, pi, 0.001)
    tjB = stick(tj - dtj, 0, pi, 0.001)
    if tiA >= 0 and tiA <= pi :
        ti = -1 if tiB >= 0 and tiB <= pi else tiA
    else :
        ti = tiB if tiB >= 0 and tiB <= pi else -1
    if tjA >= 0 and tjA <= pi :
        tj = -1 if tjB >= 0 and tjB <= pi else tjA
    else :
        tj = tjB if tjB >= 0 and tjB <= pi else -1
    return [ti, tj]

# x축(높이 방향) -l ~ l, y축 (가로 방향) k ~ k + l
k = 0.5 + b
l = (sqrt(2 * b ** 2 - (k - 2 - a / 2) ** 2) - (k - 2 + a / 2)) / 2
k = ceil(k * 1000) / 1000
l =  floor(l * 1000) / 1000

# ===================================================================
# k, l debug
if False :
    print(k, l)
    for i in range(-100, 101) :
        print(i, end = ' : ')
        for j in range(0, 101) :
            tmpt = [round(v * 180 / pi) for v in pos2theta(l * i / 100, k + l * j / 100)]
            if tmpt[0] < 63 or tmpt[1] < 63 :
                print(tmpt[0], end=' ')
                print(tmpt[1], end=' ')
                print(' ', end='')
        print()
# ===================================================================

x_precision = 20
y_precision = 100


def beep():
    speaker.volume = 100
    time.sleep(0.5)
    speaker.volume = 0
    return


def probe() :
    # return True if probe detected
    if ir_head.proximity > 80 :
        return True
    return False


# 엔코더로 왼쪽 모터 회전 - 30도
def motor_arm_left_move(ir, speed):
    # 엔코더 값 클때
    if ir.proximity > 60:
        while ir.proximity > 45:
            # print(ir.proximity)
            motor_arm.first_speed = speed
            time.sleep(0.00001)
            motor_arm.first_speed = 0
            time.sleep(0.1)
        motor_arm.first_speed = 0
        # print(ir.proximity)
        # print("ir high -> low")
    # 엔코더 센서 값 작을때
    else:
        while ir.proximity < 75:
            # print(ir.proximity)
            motor_arm.first_speed = speed
            time.sleep(0.00001)
            motor_arm.first_speed = 0
            time.sleep(0.1)
        time.sleep(0.001)
        motor_arm.first_speed = 0
        # print(ir.proximity)
        # print("ir low -> high")

# 엔코더로 오른쪽 모터 회전 - 30도
def motor_arm_right_move(ir, speed):
    # 엔코더 값 클때
    if ir.proximity > 60:
        while ir.proximity > 45:
            # print(ir.proximity)
            motor_arm.second_speed = speed
            time.sleep(0.00001)
            motor_arm.second_speed = 0
            time.sleep(0.1)
        motor_arm.second_speed = 0
        # print(ir.proximity)
        # print("ir high -> low")
    # 엔코더 센서 값 작을때
    else:
        while ir.proximity < 75:
            # print(ir.proximity)
            motor_arm.second_speed = speed
            time.sleep(0.00001)
            motor_arm.second_speed = 0
            time.sleep(0.1)
        time.sleep(0.001)
        motor_arm.second_speed = 0
        # print(ir.proximity)
        # print("ir low -> high")

# t1, t2각도로 팔 이동
def move_arm(t1, t2, v1, v2):
    global current_angle_left
    global current_angle_right

    left_count = (t1 - current_angle_left)//2
    if left_count > 0:
        for i in range(0, left_count):
            motor_arm_left_move(ir_encoder_left, v1)
    if left_count < 0:
        left_count = -left_count
        for i in range(0, left_count):
            motor_arm_left_move(ir_encoder_left, -v1)
    current_angle_left = t1

    right_count = (t2 - current_angle_right)//2
    if right_count > 0:
        for i in range(0, right_count):
            motor_arm_right_move(ir_encoder_right, v2)
    if right_count < 0:
        right_count = -right_count
        for i in range(0, right_count):
            motor_arm_right_move(ir_encoder_right, -v2)
    current_angle_right = t2

def move_arm_by_position(x, y) :
    theta = [round(v * 180 / pi) for v in pos2theta(x, y)]
    print(' -> ', end = '')
    print(theta[0], theta[1], end = '')
    move_arm(theta[0], theta[1], 50, 50)

def measure(x_step = 4, y_step = 100) :
    current_x = - x_step // 2
    while current_x <= x_step // 2 :
        current_y = 0
        print(f"Measuring at height = {current_x / x_step} : ", end = '')
        while current_y <= y_step :
            # print(l * current_x / x_step, end = ' ')
            # print(k + l * current_y / y_step, end = ' / ')
            print(current_x / x_step, end = ', ')
            print(current_y / y_step, end = '')
            move_arm_by_position(l * current_x / x_step, k + l * current_y / y_step)
            print(' / ', end = '')
            if probe() :
                print(current_y / y_step)
                current_y = y_step * 2
            else :
                current_y = current_y + 1
        if current_y != y_step * 2 :
            print("Nothing")
        current_x = current_x + 1
    print("Done")

# 파이축 회전
def pi_rotate(speed):
    if (env.red + env.green + env.blue) > 12 :
        while (env.red + env.green + env.blue) > 12:
            motor_pi_1.speed = speed, speed
            motor_pi_2.speed = speed, speed
            time.sleep(0.00001)
            motor_pi_1.speed = 0, 0
            motor_pi_2.speed = 0, 0
    else :
        while (env.red + env.green + env.blue) < 12:
            motor_pi_1.speed = speed
            motor_pi_2.speed = speed
            time.sleep(0.00001)
            motor_pi_1.speed = 0, 0
            motor_pi_2.speed = 0, 0

# ===================================================================
# main
#
# init arm angle
# 팔 각도 180도 되도록 버튼 조작
while button.pressed == False:
    motor_arm_left_move(ir_encoder_left, 100)
    time.sleep(0.1)
beep()
while button.pressed == False:
    motor_arm_left_move(ir_encoder_left, -100)
    time.sleep(0.1)
beep()
while button.pressed == False:
    motor_arm_right_move(ir_encoder_right, 100)
    time.sleep(0.1)
beep()
while button.pressed == False:
    motor_arm_right_move(ir_encoder_right, -100)
    time.sleep(0.1)
beep()

current_angle_left = 90
current_angle_right = 90


# 초기화 60 60
move_arm(60, 60, 80, 80)
beep()

# # 바닥판 test
# pi_rotate(50)
#

measure()

beep()