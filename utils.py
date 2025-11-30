from const import *
# generate_map
def generate_map(height, width):
    map = [['.' for _ in range(width)] for _ in range(height)]
    for i in range(height):
        map[i][0] = WALL
        map[i][width-1] = WALL

    for i in range(width):
        map[0][i] = WALL
        map[height-1][i] = WALL

    map[1][1] = PLAYER

    return map