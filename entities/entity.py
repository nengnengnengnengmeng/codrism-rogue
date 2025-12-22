from consts.const import *
from consts.map_const import *
from consts.entity_const import *
from utils.log import log
import random as rand

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
        self.damage_dice = ENTITIES[type]["damage_dice"]
        self.gold_reward = ENTITIES[type].get("gold_reward", 0)
        self.xp_reward = ENTITIES[type].get("xp_reward", 0)
        self.rank = ENTITIES[type].get("rank", 0)
        self.is_dead = False

    def coordinate(self):
        return self.x, self.y

    def move(self, dx, dy, map_data, entities):
        ny = self.y + dy
        nx = self.x + dx
        next_cell = map_data[ny][nx]
        
        for entity in entities:
            if entity == self: continue
            
            if entity.x == nx and entity.y == ny:
                if self.type != "Player" and entity.type != "Player":
                    return
                self.attack(entity)
                return

        if next_cell not in WALLS:
            self.x += dx
            self.y += dy

    def str_bonus(self):
        return (self.strength - 10) // 2

    def attack(self, target):
        hit_roll = rand.randint(1, 20)
        attack_bonus = self.rank
        total_hit = hit_roll + attack_bonus

        if total_hit >= target.armor:
            min_damage, max_damage = self.damage_dice
            base_damage = rand.randint(min_damage, max_damage)
            damage = base_damage + self.str_bonus()
            target.hp -= damage

            message = f"{self.type}가 {target.type}를 공격했다"
            log(message)
        else:
            message = f"{self.type}의 공격이 빗나갔다"
            log(message)

        if target.hp <= 0:
            target.is_dead = True