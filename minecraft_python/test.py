#minecraft.py 모듈 import
from mcpi.minecraft import Minecraft

import time

import random
import math

# Minecraft에 연결
mc = Minecraft.create()

#
# mc.setBlocks(0,1,0,0,256,0,10)
#
#
# mc.setBlocks(10,1,10,10,256,10,10)
#
# a = 20
# mc.setBlocks(a,1,a,a,256,a,10)
#
# a = 15
# mc.setBlocks(a,1,a,a,256,a,10)
#
#
# a = -5
# mc.setBlocks(a,1,a,a,256,a,10)

# 랜덤 500개 블럭 생성
for i in range(0, 500):
    x = random.randint(-100, 100)
    y = random.randint(-100, 100)
    mc.setBlocks(x, 1, y, x, 50, y, 0)
    print(x, y)

# 1초에 한번씩 플레이어 위에 블럭 생성
for i in range(0, 1000):
    p, q, r = mc.player.getPos()
    mc.setBlocks(round(p)-1, round(q+1), round(r)-1, round(p)+1, round(q+3), round(r)+1, 10)
    time.sleep(1)
