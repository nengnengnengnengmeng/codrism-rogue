from consts.entity_const import *
import utils.log as log

class Item:
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type

        self.char = "\033[31m" + ITEMS[type]["char"] + "\033[0m"
        self.get_collected = False
        
    def use(self, target):
        effect_value = ITEMS[self.type]["effect_value"]

        if self.type == "Health Potion": target.hp += effect_value

        if self.type == "Strength Potion": target.strength += effect_value