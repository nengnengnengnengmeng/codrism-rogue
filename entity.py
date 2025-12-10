from const import *
from map_const import *

class Entity:
    def __init__(self, x, y, char, name):
        self.x = x
        self.y = y
        self.char = char
        self.name = name

    def coordinate(self):
        return self.x, self.y

    def move(self, dx, dy, map_data):
        ny = self.y + dy
        nx = self.x + dx
        next_cell = map_data[ny][nx]
        if next_cell not in WALLS:
            self.x += dx
            self.y += dy