from const import *
import random as rand
class Room():
    def __init__(self, x, y, w, h):
        self.x1 = x
        self.y1 = y
        self.x2 = x + w
        self.y2 = y + h

    def center(self):
        cx = (self.x1 + self.x2) // 2
        cy = (self.y1 + self.y2) // 2
        return (cx, cy)

# generate_map
def generate_map():
    map = [[VOID for _ in range(MAP_WIDTH)] for _ in range(MAP_HEIGHT)]
    
    rooms = {}
    cell_w = MAP_WIDTH // 3 # 26
    cell_h = MAP_HEIGHT // 3 # 7

    for row in range(3):
        for col in range(3):
            cell_x = col * cell_w if col < 2 else MAP_WIDTH - cell_w # 0, 26, 52
            cell_y = row * cell_h if row < 2 else MAP_HEIGHT - cell_h # 0, 7, 14

            max_w = cell_w - 1
            max_h = cell_h - 1

            # !!!!이전엔 벽을 크기에서 제외했으나 벽까지 포함하도록 변경!!!
            room_w = rand.randint(4, max_w)
            room_h = rand.randint(4, max_h)

            diff_w = max_w - room_w
            diff_h = max_h - room_h
            
            room_x = cell_x + rand.randint(0, diff_w)
            room_y = cell_y + rand.randint(0, diff_h)

            new_room = Room(room_x, room_y, room_w, room_h)
            rooms[(row, col)] = new_room
            
            for y in range(new_room.y1, new_room.y2):
                for x in range(new_room.x1, new_room.x2):
                    map[y][x] = WALL

            for y in range(new_room.y1 + 1, new_room.y2 - 1):
                for x in range(new_room.x1 + 1, new_room.x2 - 1):
                    map[y][x] = FLOOR

    map[rooms[0,0].y1+2][rooms[0,0].x1+2] = PLAYER

    return map, rooms