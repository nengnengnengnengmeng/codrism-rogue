import random as rand
from entities.entity import Entity
from consts.const import *
from consts.entity_const import *

def spawn_entity(rooms, entities, map_data, depth, start_room=None):
    entity_types = [max(0, depth - 2), depth - 1, depth]
    entity_type = f"{ENTITY_RANK[rand.choice(entity_types)]}"

    x = rand.randint(0, MAP_WIDTH - 1)
    y = rand.randint(0, MAP_HEIGHT - 1)
    if map_data[y][x] != "." or any(e.x == x and e.y == y for e in entities):
        spawn_entity(rooms, entities, map_data, depth, start_room)
        return
    if start_room:
        if start_room.x1 <= x < start_room.x2 and start_room.y1 <= y < start_room.y2:
            spawn_entity(rooms, entities, map_data, depth, start_room)
            return
    new_entity = Entity(x, y, entity_type)
    entities.append(new_entity)