from const import *
from entity import Entity

class Player(Entity):
    def __init__(self, x, y, name):
        super().__init__(x, y, PLAYER, name)

        self.max_hp = PLAYER_INITIAL_HP
        self.hp = self.max_hp
        self.level = 1