from const import *
from entity_const import *
from entity import Entity

class Player(Entity):
    def __init__(self, x, y, name):
        super().__init__(x, y, "Player")
        self.name = name
        self.max_strength = self.strength
        self.gold = ENTITIES["Player"]["gold"]
        self.rank = ENTITIES["Player"]["rank"]