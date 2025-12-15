from const import *
from map_const import *
from entity_const import *
from log import log

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
            if entity == self: continue

            if entity.x == nx and entity.y == ny:
                message = self.attack(entity)
                return message

        if next_cell not in WALLS:
            self.x += dx
            self.y += dy

    def attack(self, target):
        target.hp -= self.strength
        log(f"{self.type}가 {target.type}를 공격했다")

    def ___del__(self):
        pass