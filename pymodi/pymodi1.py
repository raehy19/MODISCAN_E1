import modi
import time

# modi.update_module_firmware()
bundle = modi.MODI()

# 모터 6개
motor_arm = bundle.motors[0]
motor_pi_1 = bundle.motors[1]
motor_pi_2 = bundle.motors[2]

motor_arm.first_speed = 0
motor_arm.second_speed = 0

motor_pi_1.first_speed = 0
motor_pi_1.second_speed = 0
motor_pi_2.first_speed = 0
motor_pi_2.second_speed = 0


# ir센서 3개 사용(하나는 스캔, 두개는 엔코더용)
ir_encoder_1 = bundle.irs[0]
ir_incoder_2 = bundle.irs[1]
ir_head = bundle.irs[2]
time.sleep(1)


# # 센서 무한측정 test
# while 1:
#     print(ir1.proximity, ir2.proximity, ir3.proximity)

# 엔코더로 모터 회전 - 방향별
def motor1_clock1(ir, motor):
    if ir.proximity > 85:
        while ir.proximity > 55:
            motor.first_speed = -40
        while ir.proximity < 85:
            motor.first_speed = -40
        motor.first_speed = 0
    else:
        while ir.proximity < 85:
            motor.first_speed = -40
        while ir.proximity > 55:
            motor.first_speed = -40
        motor.first_speed = 0

def motor1_counterclock1(ir, motor):
    if ir.proximity > 85:
        while ir.proximity > 55:
            motor.first_speed = 40
        while ir.proximity < 85:
            motor.first_speed = 40
        motor.first_speed = 0
    else:
        while ir.proximity < 85:
            motor.first_speed = 40
        while ir.proximity > 55:
            motor.first_speed = 40
        motor.first_speed = 0

def motor2_clock1(ir, motor):
    if ir.proximity > 80:
        while ir.proximity > 45:
            motor.second_speed = -40
        while ir.proximity < 80:
            motor.second_speed = -40
        motor.second_speed = 0
    else:
        while ir.proximity < 80:
            motor.second_speed = -40
        # while ir2.proximity > 45:
        #     motor.second_speed = -40
        motor.second_speed = 0

def motor2_counterclock1(ir, motor):
    if ir.proximity > 80:
        while ir.proximity > 45:
            motor.second_speed = 40
        while ir.proximity < 80:
            motor.second_speed = 40
        motor.second_speed = 0
    else:
        while ir.proximity < 80:
            motor.second_speed = 40
        # while ir2.proximity > 45:
        #     motor.second_speed = 40
        motor.second_speed = 0



from math import pi, sqrt, sin, cos, acos, atan2, isclose, floor, ceil

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
                print(tmpt[0] , end=' ')
                print(tmpt[1], end=' ')
                print(' ', end='')
        print()
# ===================================================================

x_precision = 20
y_precision = 100

def probe() :
    # return True if probe detected
    return False

def move_arm(t1, t2, v1, v2) :
    return

def move_arm_by_position(x, y) :
    theta = [round(v * 180 / pi) for v in pos2theta(x, y)]
    move_arm(theta[0], theta[1], 50, 50)

def measure(x_step = 20, y_step = 100) :
    current_x = - (x_step // 2)
    while current_x <= x_step :
        current_y = 0
        print(f"Measuring at height = {current_x / x_step} : ", end = '')
        while current_y <= y_step :
            move_arm_by_position(l * current_x / x_step, k + l * current_y / y_step)
            if probe() :
                print(current_y / y_step)
                current_y = y_step * 2
            else :
                current_y = current_y + 1
        if current_y != y_step * 2 :
            print("Nothing")
        current_x = current_x + 1
    print("Done")