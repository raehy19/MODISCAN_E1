import modi
import time
import numpy
import matplotlib.pyplot as plt

# modi
# ==================================================

# 모디 업데이트
# modi.update_module_firmware()

# 모디 연결
bundle = modi.MODI()

# 모터 연결 + 초기화
motor_arm = bundle.motors[0]
motor_arm.first_speed = 0
motor_arm.second_speed = 0

# ir센서 3개 연결 + 초기화 (하나는 스캔, 두개는 엔코더용)
ir_encoder_1 = bundle.irs[0]
ir_incoder_2 = bundle.irs[1]
print(f"ir sensor init : {ir_encoder_1.proximity, ir_incoder_2.proximity}")


motor_speed = 50
motor_arm.first_speed = motor_speed
motor_arm.second_speed = motor_speed

ir1s = []
ir2s = []
num = []

# while 1:
#     print(ir_encoder_1.proximity, ir_incoder_2.proximity)

time.sleep(2)

for i in range(1000):
    print(ir_encoder_1.proximity, ir_incoder_2.proximity)
    ir1s.append(ir_encoder_1.proximity)
    ir2s.append(ir_incoder_2.proximity)
    num.append(i)
    time.sleep(0.05)


plt.subplot(211)
plt.scatter(num, ir1s, s = 1, c = 'r')

plt.subplot(212)
plt.scatter(num, ir2s, s = 1, c = 'r')


plt.show()

motor_arm.first_speed = 0
motor_arm.second_speed = 0

print(numpy.mean(ir1s), numpy.mean(ir2s))



