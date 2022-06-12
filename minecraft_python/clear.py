#minecraft.py 모듈 import
from mcpi.minecraft import Minecraft

# Minecraft에 연결
mc = Minecraft.create()

import time
time.sleep(10)


def clearwithZ():
    mc.setBlocks(-150, 1, -150, 150, 256, 150, 0)
    # z 축 (BLUE)
    mc.setBlocks(0, 1, 0, 0, 256, 0, 251, 11)

def clearALL():
    mc.setBlocks(-150, 1, -150, 150, 256, 150, 0)
    mc.setBlocks(-150, 0, -150, 150, 0, 150, 1)

clearwithZ()
# clearALL()
