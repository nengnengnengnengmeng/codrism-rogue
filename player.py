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
        if map_data[self.y + dy][self.x + dx] != WALL:
            map_data[self.y][self.x] = FLOOR
            self.x += dx
            self.y += dy
            map_data[self.y][self.x] = PLAYER
            
        return map_data