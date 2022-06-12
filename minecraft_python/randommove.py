#minecraft.py 모듈 import
from mcpi.minecraft import Minecraft

# Minecraft에 연결
mc = Minecraft.create()
mc.postToChat("Hello Minecraft World!!!")

import random

# Player를 이동시킬 임의의 위치 좌표를 구함
randomX = random.randint(-100, 100)
randomZ = random.randint(-100, 100)
randomY = 5

print("My position: x = %d, y = %d, z = %d" % (randomX, randomY, randomZ))


# Player를 이동시킴
mc.player.setPos(randomX, randomY, randomZ)
mc.postToChat("I'm moved!")