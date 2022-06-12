#minecraft.py 모듈 import
from mcpi.minecraft import Minecraft
import math
import numpy as np

# Minecraft에 연결
mc = Minecraft.create()

# 바닥에 원형으로 BLOCK을 까는 함수
# 반지름이 커질수록 적용되는 각도를 줄여 더 많은 점을 찍도록 구현
def set_round_floor():
    for i in range(1, 100):
        for theta in np.arange(0, 2 * math.pi, 0.05 / i):
            x = math.cos(theta) * i
            y = math.sin(theta) * i
            x = round(x)
            y = round(y)
            # Quartz Block 사용
            mc.setBlock(x, 0, y, 155)

# 바닥에 반지름이 r인 선 긋는 함수
def round_line(r):
    for theta in np.arange(0, 2 * math.pi, 0.05 / r):
        x = math.cos(theta) * r
        y = math.sin(theta) * r
        x = round(x)
        y = round(y)
        # Chiseled Quartz Block 사용
        mc.setBlock(x, 0, y, 155, 1)


# x,y,z 축 그리기
def draw_axis():
    # x 축 (RED)
    mc.setBlocks(1, 0, 0, 100, 0, 0, 251, 14)
    # 우리가 일반적으로 생각하는 Cartesian coordinate로 만들기 위해
    # mincraft상의 y축의 음의방향을 Cartesian coordinate의 y축으로 적용한다.
    # y 축 (GREEN)
    mc.setBlocks(0, 0, -100, 0, 0, -1, 251, 13)
    # z 축 (BLUE)
    mc.setBlocks(0, 1, 0, 0, 256, 0, 251, 11)

# 바닥세팅 종합
def set_floor():
    set_round_floor()
    # 반지름 10 단위로 바닥에 선 긋기
    for r in range(10, 100, 10):
        round_line(r)
    draw_axis()