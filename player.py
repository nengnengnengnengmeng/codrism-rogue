from const import *
from entity_const import *
from entity import Entity

class Player(Entity):
    def __init__(self, x, y, name):
        super().__init__(x, y, PLAYER["char"], name)
        self.max_hp = PLAYER["hp"]
        self.hp = self.max_hp
        self.max_strength = PLAYER["strength"]
        self.strength = PLAYER["strength"]
        self.gold = PLAYER["gold"]
        self.armor = PLAYER["armor"]
        self.rank = PLAYER["rank"]