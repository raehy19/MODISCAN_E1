#minecraft.py 모듈 import
from mcpi.minecraft import Minecraft
import math
import numpy as np
# Minecraft에 연결
mc = Minecraft.create()


def clear():
    mc.setBlocks(-50, 1, -50, 50, 50, 50, 0)



tile_position = mc.player.getTilePos()
print(tile_position)

# # Player 0,0,0으로 이동시킴
# mc.player.setPos(0, 1, 0)
# mc.postToChat("0,0,0 으로 이동")


tile_position = mc.player.getTilePos()
print(tile_position)

mc.setBlock(0,1,0,51)

#
# r = 30
# for theta in np.arange(0, 2 * math.pi, 0.05/r):
#     x = math.cos(theta) * r
#     y = math.sin(theta) * r
#     x = round(x)
#     y = round(y)
#
#     mc.setBlock(x, 5, y, 8)

    # mc.setBlock(x, 1, y, 246)
    # mc.setBlock(x, 2, y, 250)
    # mc.setBlock(x, 3, y, 235)
    # mc.setBlock(x, 4, y, 242)

r = 50
for theta in np.arange(0, 2 * math.pi, 0.1/r):
    x = math.cos(theta) * r
    y = math.sin(theta) * r
    x = round(x)
    y = round(y)

    mc.setBlock(x, 3, y, 10)
    for j in range(1, 100):
        mc.setBlock(x, j, y, 20)

mc.postToChat("map 변경")


# # # 원형으로 clear
# for i in range(2, 50):
#     for theta in np.arange(0, 2 * math.pi, 0.001):
#         x = math.cos(theta) * i
#         y = math.sin(theta) * i
#         x = round(x)
#         y = round(y)
#         mc.setBlock(x, 0, y, 155)
# #         for j in range(1, 50):
#             mc.setBlock(x, j, y, 0)

mc.setBlocks(0,1,0,0,256,0,49)