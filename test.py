import map_generator as mg
from const import *
from renderer import draw
from player import Player
import os
ROOMS_ROW = 3
ROOMS_COL = 3
map_data, rooms, parents = mg.MapGenerator(MAP_WIDTH, MAP_HEIGHT, ROOMS_ROW, ROOMS_COL).generate()
player = Player(rooms[0,0].x1+2, rooms[0,0].y1+2, "{player_name}")
os.system('cls')
draw(map_data, player, "")

def find_parent(room):
    if room != parents[room]:
        parents[room] = find_parent(parents[room])
    return parents[room]

print("\n")
buffer = ""
for i in range(3):
    for j in range(3):
        room = rooms[(i, j)].grid
        buffer += f"{find_parent(room)} "
    print(buffer)
    buffer = ""