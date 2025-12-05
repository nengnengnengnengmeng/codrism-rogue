from const import *
import random as rand

ROOMS_ROW = 3
ROOMS_COL = 3

class Room():
    def __init__(self, x, y, w, h, row, col):
        self.x1 = x
        self.y1 = y
        self.x2 = x + w
        self.y2 = y + h
        self.grid = (row, col)
        self.howmanydoorsarethere = 0
        self.wheresarethedoors = []

    def center(self):
        cx = (self.x1 + self.x2) // 2
        cy = (self.y1 + self.y2) // 2
        return (cx, cy)

# generate_rooms
def generate_rooms():
    map_data = [[VOID for _ in range(MAP_WIDTH)] for _ in range(MAP_HEIGHT)]
    rooms = {}
    cell_w = MAP_WIDTH // ROOMS_COL # 26
    cell_h = MAP_HEIGHT // ROOMS_ROW # 7

    for row in range(ROOMS_ROW):
        for col in range(ROOMS_COL):
            cell_x = col * cell_w if col < ROOMS_COL - 1 else MAP_WIDTH - cell_w # 0, 26, 52
            cell_y = row * cell_h if row < ROOMS_ROW - 1 else MAP_HEIGHT - cell_h # 0, 7, 14

            max_w = cell_w - 1
            max_h = cell_h - 1

            # !!!!이전엔 벽을 크기에서 제외했으나 벽까지 포함하도록 변경!!!
            room_w = rand.randint(4, max_w)
            room_h = rand.randint(4, max_h)

            diff_w = max_w - room_w
            diff_h = max_h - room_h
            
            room_x = cell_x + rand.randint(0, diff_w)
            room_y = cell_y + rand.randint(0, diff_h)

            new_room = Room(room_x, room_y, room_w, room_h, row, col)
            rooms[(row, col)] = new_room
            
            for y in range(new_room.y1, new_room.y2):
                for x in range(new_room.x1, new_room.x2):
                    map_data[y][x] = FLOOR

            map_data[new_room.y1][new_room.x1] = LEFT_TOP_WALL
            map_data[new_room.y1][new_room.x2 - 1] = RIGHT_TOP_WALL
            map_data[new_room.y2 - 1][new_room.x1] = LEFT_BOTTOM_WALL
            map_data[new_room.y2 - 1][new_room.x2 - 1] = RIGHT_BOTTOM_WALL
            for x in range(new_room.x1 + 1, new_room.x2 - 1):
                map_data[new_room.y1][x] = HORIZONTAL_WALL
                map_data[new_room.y2 - 1][x] = HORIZONTAL_WALL
            for y in range(new_room.y1 + 1, new_room.y2 - 1):
                map_data[y][new_room.x1] = VERTICAL_WALL
                map_data[y][new_room.x2 - 1] = VERTICAL_WALL

    for col in range(ROOMS_COL):
        for row in range(ROOMS_ROW):
            current_room = rooms[(row, col)]
            connect_rooms(map_data, rooms, current_room)

    return map_data, rooms

# get_door_location
def get_door_location(room, direction):
    if direction == 'N':
        x = rand.randint(room.x1 + 1, room.x2 - 2)
        y = room.y1
    elif direction == 'S':
        x = rand.randint(room.x1 + 1, room.x2 - 2)
        y = room.y2 - 1
    elif direction == 'W':
        x = room.x1
        y = rand.randint(room.y1 + 1, room.y2 - 2)
    elif direction == 'E':
        x = room.x2 - 1
        y = rand.randint(room.y1 + 1, room.y2 - 2)
    return (x, y)
    
#connect_rooms
def connect_rooms(map_data, rooms, current_room):
    current_room = current_room
    row, col = current_room.grid
    if col < ROOMS_COL - 1:
        if rand.random() < 0.7:
            target_room = rooms[row, col+1]

            current_room.howmanydoorsarethere += 1
            target_room.howmanydoorsarethere += 1

            x1, y1 = get_door_location(current_room, 'E')
            x2, y2 = get_door_location(target_room, 'W')
            
            map_data[y1][x1] = DOOR
            map_data[y2][x2] = DOOR

            current_room.wheresarethedoors.append('E')
            target_room.wheresarethedoors.append('W')

            make_corridor(map_data, x1, y1, x2, y2, 'H')

    if row < ROOMS_ROW - 1:
        if rand.random() < 0.7:
            target_room = rooms[row+1, col]

            current_room.howmanydoorsarethere += 1
            target_room.howmanydoorsarethere += 1

            x1, y1 = get_door_location(current_room, 'S')
            x2, y2 = get_door_location(target_room, 'N')

            map_data[y1][x1] = DOOR
            map_data[y2][x2] = DOOR

            current_room.wheresarethedoors.append('S')
            target_room.wheresarethedoors.append('N')

            make_corridor(map_data, x1, y1, x2, y2, 'V')

    if current_room.howmanydoorsarethere <= 1:
        if col < ROOMS_COL - 1 and 'E' not in current_room.wheresarethedoors:
            target_room = rooms[row, col+1]

            current_room.howmanydoorsarethere += 1
            target_room.howmanydoorsarethere += 1

            x1, y1 = get_door_location(current_room, 'E')
            x2, y2 = get_door_location(target_room, 'W')
            
            map_data[y1][x1] = DOOR
            map_data[y2][x2] = DOOR

            make_corridor(map_data, x1, y1, x2, y2, 'H')

        elif row < ROOMS_ROW - 1 and 'S' not in current_room.wheresarethedoors:
            target_room = rooms[row+1, col]

            current_room.howmanydoorsarethere += 1
            target_room.howmanydoorsarethere += 1

            x1, y1 = get_door_location(current_room, 'S')
            x2, y2 = get_door_location(target_room, 'N')

            map_data[y1][x1] = DOOR
            map_data[y2][x2] = DOOR

            make_corridor(map_data, x1, y1, x2, y2, 'V')

def make_corridor(map_data, x1, y1, x2, y2, direction):
    if direction == 'H':
        mid_x = rand.randint(x1+1, x2-1)

        for x in range(x1+1, mid_x + 1):
            map_data[y1][x] = CORRIDOR

        if y1 < y2:
            for y in range(y1, y2 + 1):
                map_data[y][mid_x] = CORRIDOR
        else:  
            for y in range(y2, y1 + 1):
                map_data[y][mid_x] = CORRIDOR

        for x in range(mid_x, x2):
            map_data[y2][x] = CORRIDOR

    elif direction == 'V':
        mid_y = rand.randint(y1+1, y2-1)

        for y in range(y1+1, mid_y + 1):
            map_data[y][x1] = CORRIDOR

        if x1 < x2:
            for x in range(x1, x2 + 1):
                map_data[mid_y][x] = CORRIDOR
        else:  
            for x in range(x2, x1 + 1):
                map_data[mid_y][x] = CORRIDOR

        for y in range(mid_y, y2):
            map_data[y][x2] = CORRIDOR