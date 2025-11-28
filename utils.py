# generateMap
def generateMap(height, width):
    map = [['.' for _ in range(width)] for _ in range(height)]
    for i in range(height):
        map[i][0] = "#"
        map[i][width-1] = "#"

    for i in range(width):
        map[0][i] = "#"
        map[height-1][i] = "#"

    map[1][1] = '@'

    return map