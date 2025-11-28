from pprint import pprint
from utils import generateMap
HEIGHT = 5
WIDTH = 10
FLOOR = '.'
PLAYER = '@'
WALL = '#'

mapData = generateMap(HEIGHT, WIDTH)
playerX = 1
playerY = 1

while True:
    for row in mapData:
        print(' '.join(row))
    decision = input("움직임: ")
    if decision == 'd':
        if mapData[playerY][playerX+1] != '#'