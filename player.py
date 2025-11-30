from const import *

class Player:
    def __init__(self, x, y, name="Player"):
        self.x = x
        self.y = y
        self.name = name
        self.hp = PLAYER_INITIAL_HP
        self.max_hp = PLAYER_INITIAL_HP
        self.level = 1