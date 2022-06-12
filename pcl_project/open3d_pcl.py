import open3d as o3d
import numpy as np
import random


# test1
temp_np_array = np.array([[0, 0, 0]], dtype=np.float32)
# x축
for i in range(1, 100):
    x, y, z = i, 0, 0
    temp_np_array = np.append(temp_np_array, np.array([[x, y, z]]), axis=0)
# y축
for i in range(1, 100):
    x, y, z = 0, i, 0
    temp_np_array = np.append(temp_np_array, np.array([[x, y, z]]), axis=0)
# z축
for i in range(1, 100):
    x, y, z = 0, 0, i
    temp_np_array = np.append(temp_np_array, np.array([[x, y, z]]), axis=0)
# 랜덤 점 1000개 생성
for i in range(0, 1000):
    x = random.random() * 50
    y = random.random() * 50
    z = random.random() * 50
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

