from utils import generate_map
from renderer import draw
from player import Player

map, rooms = generate_map()
player = Player(rooms[0].x1+1, rooms[0].y1+1, "name")
message = "message"

while True:
    draw(map, player, message)
    