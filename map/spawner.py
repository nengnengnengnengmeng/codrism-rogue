import random as rand
from entities.entity import Entity
from entities.item import Item
from consts.const import *
from consts.entity_const import *

def spawn_entity(rooms, entities, map_data, depth, start_room=None, location=None):
    entity_types = [max(0, depth - 2), depth - 1, depth]
    entity_type = f"{ENTITY_RANK[rand.choice(entity_types)]}"
    if not location:
        x = rand.randint(0, MAP_WIDTH - 1)
        y = rand.randint(0, MAP_HEIGHT - 1)
    else:
        x, y = location
    if map_data[y][x] != "." or any(e.x == x and e.y == y for e in entities):
        spawn_entity(rooms, entities, map_data, depth, start_room)
        return
    if start_room:
        if start_room.x1 <= x < start_room.x2 and start_room.y1 <= y < start_room.y2:
            spawn_entity(rooms, entities, map_data, depth, start_room)
            return
    new_entity = Entity(x, y, entity_type)
    entities.append(new_entity)

def spawn_item(rooms, items, map_data):
    x = rand.randint(0, MAP_WIDTH - 1)
    y = rand.randint(0, MAP_HEIGHT - 1)

    if map_data[y][x] != "." or any(i.x == x and i.y == y for i in items):
        spawn_item(rooms, items, map_data)
        return
    
    if rand.random() < 0.85:
        item_type = "Health Potion"
    else:
        item_type = "Strength Potion"

    new_item = Item(x, y, item_type)
    items.append(new_item)
    return