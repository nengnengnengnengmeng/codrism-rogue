from consts.const import *
from consts.entity_const import *
from entities.entity import Entity
import utils.log as log
import random as rand

class Player(Entity):
    def __init__(self, x, y, name):
        super().__init__(x, y, "Player")
        self.name = name
        self.max_strength = self.strength
        self.gold = ENTITIES["Player"]["gold"]
        self.xp = ENTITIES["Player"]["xp"]
        self.depth = 1

    def level_up(self):
        if self.xp >= (self.rank + 1) * 10 and self.rank < 7:
            self.rank+= 1
            self.xp -= (self.rank + 1) * 20

            hp = rand.randint(2,5)
            self.max_hp += hp
            self.hp = min(self.max_hp, self.hp + 10)
            
            log.log(f"{RANK_TITLES[self.rank]}로 랭크업")