#minecraft.py 모듈 import
from mcpi.minecraft import Minecraft
import math

# Minecraft에 연결
mc = Minecraft.create()


# pi
pi = math.pi

# Cylindrical coordinate의 좌표를 입력받아 마인크래프트에 그리는 함수 (theta의 단위는 라디안)
# 우리가 일반적으로 생각하는 Cartesian coordinate로 만들기 위해 theta 는 음수로 적용한다.
def DRAW(r, theta, z):
    # Cylindrical to Cartesian
    x = r*(math.cos(-theta))
    y = r*(math.sin(-theta))
    z = z
    # 블럭의 Cartesian coordinate 좌표를 정수로 반올림
    x = round(x)
    y = round(y)
    z = round(z)
    # 마인크래프트 공간상에 블럭 생성 (YELLOW)
    mc.setBlock(x, z, y, 251, 4)


# test 1 for pi increase
t1_z = 10
DRAW(10, 0, t1_z)
DRAW(10, pi / 2, t1_z + 2)
DRAW(10, pi, t1_z + 4)
DRAW(10, pi * 3 / 2, t1_z + 6)

# test 2 for random points
import random
import time
for i in range(0, 1000):
    t2_r = random.random()*50
    t2_z = random.random()*49+1
    t2_theta = random.random()*2*pi
    DRAW(t2_r, t2_theta, t2_z)
    time.sleep(0.1)



