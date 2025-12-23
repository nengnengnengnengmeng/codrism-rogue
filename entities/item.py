from consts.entity_const import *
import utils.log as log

class Item:
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type

        self.char = ITEMS[type]["char"]
        self.get_collected = False
        
    def use(self, target):
        effect_value = ITEMS[self.type]["effect_value"]

        if self.type == "Health Potion": target.hp = min(target.max_hp, target.hp + effect_value)

        if self.type == "Strength Potion": 
            target.max_strength += effect_value
            target.strength += effect_value