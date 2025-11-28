from utils import generateMap, movePlayer
from const import *
import input_handler
import os, keyboard as kb, time

mapData = generateMap(HEIGHT, WIDTH)
playerX = 1
playerY = 1

#입력 스레드 시작
input_handler.start_listener()

a = input("시작하려면 아무 키 입력: ") #추후 조정
os.system('cls')

while True:
    print("\033[H", end="")
    for row in mapData:
        print(''.join(row))
    #decision = input("움직임(qweasdzxc): ")
    decision = input_handler.last_key
    mapData,playerX, playerY = movePlayer(mapData, playerX, playerY, decision)

    time.sleep(0.1) #추후 조정