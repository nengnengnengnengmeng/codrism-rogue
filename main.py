from pprint import pprint

HEIGHT = 5
WIDTH = 10

map = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]
for i in range(WIDTH):
    map[0][i] = "*"
    map[HEIGHT-1][i] = "*"

for i in range(HEIGHT):
    map[i][0] = "*"
    map[i][WIDTH-1] = "*"

pprint(map)