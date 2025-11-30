from const import *
import random as rand
class Room():
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

# generate_map
def generate_map():
    map = [[WALL for _ in range(MAP_WIDTH)] for _ in range(MAP_HEIGHT)]
    
    rooms = []
    cell_w = MAP_WIDTH // 3 # 26
    cell_h = MAP_HEIGHT // 3 # 7

    for row in range(3):
        for col in range(3):
            cell_x = col * cell_w # 0, 26, 52
            cell_y = row * cell_h # 0, 7, 14
            room_w = rand.randint(2, cell_w - 2) # 2-24
            room_h = rand.randint(2, cell_h - 2) # 2-5
            room_x = cell_x + rand.randint(1, cell_w - room_w - 1) # 1-23
            room_y = cell_y + rand.randint(1, cell_h - room_h - 1) # 1-4
            room = Room(room_x, room_y, room_x + room_w, room_y + room_h)
            rooms.append(room)

    for room in rooms:
        for y in range(room.y1, room.y2):
            for x in range(room.x1, room.x2):
                map[y][x] = FLOOR

    return map