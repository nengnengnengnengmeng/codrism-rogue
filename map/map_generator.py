from consts.const import *
from consts.map_const import *
import random as rand   

class Room:
    def __init__(self, x, y, w, h, row, col):
        self.x1 = x
        self.y1 = y
        self.x2 = x + w
        self.y2 = y + h
        self.grid = (row, col)
        self.door_locations = []
        self.parent = self.grid
        self.exists = True

    def center(self):
        cx = (self.x1 + self.x2) // 2
        cy = (self.y1 + self.y2) // 2
        return (cx, cy)
    
    def count_doors(self):
        return len(self.door_locations)
    
class MapGenerator:
    def __init__(self, width, height, row, col):
        self.width = width
        self.height = height
        self.row = row
        self.col = col
        self.map_data = []
        self.rooms = {}
        self.parents = {}
        self.stair = None

    def generate(self):
        self.map_data = [[VOID for _ in range(self.width)] for _ in range(self.height)]

        self._place_rooms()

        self._connect_rooms()

        for room in self.rooms.values():
            self._find_parent(room.grid)

        if self._isolated_exist():
            return self.generate()

        self._place_stair()

        return self.map_data, self.rooms, self.parents, self.stair

    def _find_parent(self, room):
        if room != self.parents[room]:
            self.parents[room] = self._find_parent(self.parents[room])
        return self.parents[room]
    
    def _change_parent(self, current_room, target_room):
        current_parent = self._find_parent(current_room)
        target_parent = self._find_parent(target_room)
        if current_parent != target_parent:
            self.parents[current_parent] = target_parent

    def _isolated_exist(self):
        if len(set(self.parents.values())) > 1:
            return True
        return False
    
    def _place_rooms(self):
        cell_w = self.width // self.col
        cell_h = self.height // self.row

        counnter = 0

        for row in range(self.row):
            for col in range(self.col):
                cell_x = col * cell_w if col < self.col - 1 else self.width - cell_w
                cell_y = row * cell_h if row < self.row - 1 else self.height - cell_h

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

                if rand.random() < 0.8:
                    new_room.exists = True
                    counnter += 1
                else:
                    new_room.exists = False

                self.rooms[(row, col)] = new_room
                self.parents[(row, col)] = (row, col)
                self._draw_room(new_room)

        if counnter == 0:
            self._place_rooms()

    def _place_stair(self):
        x = rand.randint(0, MAP_WIDTH-1)
        y = rand.randint(0, MAP_HEIGHT-1)
        if self.map_data[y][x] != '.':
            self._place_stair()
            return
        self.map_data[y][x] = '>'
        self.stair = (x, y)

    def _draw_room(self, new_room):
        if new_room.exists == False:
            cx, cy = new_room.center()
            self.map_data[cy][cx] = CORRIDOR
            return
        for y in range(new_room.y1, new_room.y2):
            for x in range(new_room.x1, new_room.x2):
                self.map_data[y][x] = FLOOR

        self.map_data[new_room.y1][new_room.x1] = LEFT_TOP_WALL
        self.map_data[new_room.y1][new_room.x2 - 1] = RIGHT_TOP_WALL
        self.map_data[new_room.y2 - 1][new_room.x1] = LEFT_BOTTOM_WALL
        self.map_data[new_room.y2 - 1][new_room.x2 - 1] = RIGHT_BOTTOM_WALL

        for x in range(new_room.x1 + 1, new_room.x2 - 1):
            self.map_data[new_room.y1][x] = HORIZONTAL_WALL
            self.map_data[new_room.y2 - 1][x] = HORIZONTAL_WALL

        for y in range(new_room.y1 + 1, new_room.y2 - 1):
            self.map_data[y][new_room.x1] = VERTICAL_WALL
            self.map_data[y][new_room.x2 - 1] = VERTICAL_WALL

    def _connect_rooms(self):
        for row in range(self.row):
            for col in range(self.col):
                current_room = self.rooms[(row, col)]
                row, col = current_room.grid
                if col < self.col - 1 and rand.random() < 0.5:
                    target_room = self.rooms[(row, col + 1)]
                    door_loc_current = self._get_door_location(current_room, 'E')
                    door_loc_target = self._get_door_location(target_room, 'W')
                    current_room.door_locations.append(door_loc_current)
                    target_room.door_locations.append(door_loc_target)
                    self._change_parent(current_room.grid, target_room.grid)
                    self._draw_corridor(door_loc_current, door_loc_target, 'H')
                    if not target_room.exists:
                        self._draw_corridor(door_loc_target, target_room.center(), 'H')
                    if not current_room.exists:
                        self._draw_corridor(current_room.center(), door_loc_target, 'H')
                
                if row < self.row - 1 and rand.random() < 0.5:
                    target_room = self.rooms[(row + 1, col)]
                    door_loc_current = self._get_door_location(current_room, 'S')
                    door_loc_target = self._get_door_location(target_room, 'N')
                    current_room.door_locations.append(door_loc_current)
                    target_room.door_locations.append(door_loc_target)
                    self._change_parent(current_room.grid, target_room.grid)
                    self._draw_corridor(door_loc_current, door_loc_target, 'V')
                    if not current_room.exists:
                        self._draw_corridor(current_room.center(), door_loc_target, 'V')
                    if not target_room.exists:
                        self._draw_corridor(door_loc_target, target_room.center(), 'V')

    def _get_door_location(self, room, direction):
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
        if room.exists:
            self.map_data[y][x] = DOOR
        else:
            self.map_data[y][x] = CORRIDOR
        return (x, y)
    
    def _draw_corridor(self, door1, door2, direction):
        x1, y1 = door1
        x2, y2 = door2
        if direction == 'H':
            mid_x = rand.randint(x1+1, x2-1)
            self._draw_line(x1+1, y1, mid_x, y1)
            self._draw_line(mid_x, y1, mid_x, y2)
            self._draw_line(mid_x, y2, x2-1, y2)

        elif direction == 'V':
            mid_y = rand.randint(y1+1, y2-1)
            self._draw_line(x1, y1+1, x1, mid_y)
            self._draw_line(x1, mid_y, x2, mid_y)
            self._draw_line(x2, mid_y, x2, y2-1)

    def _draw_line(self, x1, y1, x2, y2):
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                self.map_data[y][x1] = CORRIDOR
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                self.map_data[y1][x] = CORRIDOR