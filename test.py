import map.map_generator as mg
from consts.const import *
from screen.renderer import draw
from entities.player import Player
import os
ROOMS_ROW = 3
ROOMS_COL = 3
map_data, rooms, parents = mg.MapGenerator(MAP_WIDTH, MAP_HEIGHT, ROOMS_ROW, ROOMS_COL).generate()
player = Player(rooms[0,0].x1+2, rooms[0,0].y1+2, "{player_name}")
os.system('cls')
draw(map_data, player, "")

print("\n")
buffer = ""
for i in range(3):
    for j in range(3):
        room = rooms[(i, j)].grid
        buffer += f"{parents[room]} "
    print(buffer)
    buffer = "" 