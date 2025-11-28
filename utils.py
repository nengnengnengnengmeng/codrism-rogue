from const import *
# generateMap
def generateMap(height, width):
    map = [['.' for _ in range(width)] for _ in range(height)]
    for i in range(height):
        map[i][0] = WALL
        map[i][width-1] = WALL

    for i in range(width):
        map[0][i] = WALL
        map[height-1][i] = WALL

    map[1][1] = PLAYER

    return map

# movePlayer
def movePlayer(map, x, y, decision):
    if decision not in MOVES:
        return map, x, y
    
    dx, dy = MOVES[decision]

    if map[y+dy][x+dx] == WALL:
        return map, x, y
    
    map[y][x] = FLOOR
    map[y+dy][x+dx] = PLAYER

    return map,x+dx, y+dy