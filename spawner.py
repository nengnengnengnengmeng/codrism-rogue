import random as rand
from entity import Entity
from const import *

def spawn_entity(rooms, entities, entity_type, map_data):
    x = rand.randint(0, MAP_WIDTH - 1)
    y = rand.randint(0, MAP_HEIGHT - 1)
    if map_data[y][x] != "." or any(e.x == x and e.y == y for e in entities):
        spawn_entity(rooms, entities, entity_type, map_data)
        return
    new_entity = Entity(x, y, entity_type)
    entities.append(new_entity)