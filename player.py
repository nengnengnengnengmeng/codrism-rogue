from const import *

class Player:
    def __init__(self, x, y, name="Player"):
        self.x = x
        self.y = y
        self.name = name
        self.hp = PLAYER_INITIAL_HP
        self.max_hp = PLAYER_INITIAL_HP
        self.level = 1

    def move(self, dx, dy, map_data):
        ny = self.y + dy
        nx = self.x + dx
        if map_data[ny][nx] != HORIZONTAL_WALL and map_data[ny][nx] != VOID and map_data[ny][nx] != VERTICAL_WALL:
            self.x += dx
            self.y += dy
        return map_data