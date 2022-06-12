import open3d as o3d
import numpy as np
import random
from math import pi, sqrt, sin, cos, acos, atan2, isclose, floor, ceil
from mcpi.minecraft import Minecraft
import math
import modi
import time

# ========== 마인크래프트 ==========

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


def clearwithZ():
    mc.setBlocks(-150, 1, -150, 150, 256, 150, 0)
    # z 축 (BLUE)
    mc.setBlocks(0, 1, 0, 0, 256, 0, 251, 11)

def clearALL():
    mc.setBlocks(-150, 1, -150, 150, 256, 150, 0)
    mc.setBlocks(-150, 0, -150, 150, 0, 150, 1)

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


# ========== main ==========

# while 1:
#     # 3d draw test
#     # test for random points
#     # clearALL()
#     # time.sleep(1)
#     # set_floor()
#     # time.sleep(1)
#     for i in range(0, 400):
#         t2_r = random.random()*50
#         t2_z = random.random()*49+1
#         t2_theta = random.random()*2*pi
#         DRAW(t2_r, t2_theta, t2_z)
#         time.sleep(0.1)
#
#     time.sleep(2)
#     clearwithZ()
#     time.sleep(1)
while 1:
    clearwithZ()

    temp_np_array = np.array([[0, 0, 0]], dtype=np.float32)
    # test1
    for theta in np.arange(0, 6.3, 0.1):
        for z in range(1, 40):
            r = random.randint(21, 23)
            DRAW(r, theta, z)
            time.sleep(0.02)
            x = r * (math.cos(-theta))
            y = r * (math.sin(-theta))
            z = z
            temp_np_array = np.append(temp_np_array, np.array([[x, y, z]]), axis=0)

    # 포인트클라우드를 만들기 위해
    # 1. 각 점들의 x, y, z 좌표를 numpy 2D array로 저장
    # 2. open3d의 pointcloud type 변수 생성
    # 3. open3d의 Vector3dVector 함수로 1번에서 만든 2D numpy array를 변환해 2번의 pointcloud형 변수로 저장
    PointCloud_array = temp_np_array

    # PointCloud 생성(초기화)
    PointCloud_data = o3d.geometry.PointCloud()

    # Numpy Array로 입력받아 PointCloud로 변환
    PointCloud_data.points = o3d.utility.Vector3dVector(PointCloud_array)
    print(PointCloud_data)

    # PointCloud data를 담을 수 있는 .xyz 파일로 저장
    o3d.io.write_point_cloud("pcd_test1.xyz", PointCloud_data)

    # visualization : open3d의 함수를 이용해 pointcloud 시각화
    print(np.asarray(PointCloud_data.points))
    o3d.visualization.draw_geometries([PointCloud_data])





