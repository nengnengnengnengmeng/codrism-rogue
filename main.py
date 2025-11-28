from utils import generateMap, movePlayer
from const import *

mapData = generateMap(HEIGHT, WIDTH)
playerX = 1
playerY = 1

while True:
    for row in mapData:
        print(''.join(row))
    decision = input("움직임(qweasdzxc): ")
    mapData,playerX, playerY = movePlayer(mapData, playerX, playerY, decision)