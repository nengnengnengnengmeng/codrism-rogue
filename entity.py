from const import *
from map_const import *
from entity_const import *

class Entity:
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.name = type
        self.type = type
        self.char = ENTITIES[type]["char"]
        self.max_hp = ENTITIES[type]["hp"]
        self.hp = self.max_hp
        self.strength = ENTITIES[type]["strength"]
        self.armor = ENTITIES[type]["armor"]

    def coordinate(self):
        return self.x, self.y

    def move(self, dx, dy, map_data, entities):
        ny = self.y + dy
        nx = self.x + dx
        next_cell = map_data[ny][nx]
        
        for entity in entities:
            if entity.type == "Player": continue
            if entity.x == nx and entity.y == ny:
                self.attack(entity)
                return

        if next_cell not in WALLS:
            self.x += dx
            self.y += dy

    def attack(self, target):
        target.hp -= self.strength
        self.hp -= target.strength