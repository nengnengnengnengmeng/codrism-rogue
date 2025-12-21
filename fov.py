from consts.const import *

def fov(map_data, player, rooms):
    visible_tiles = set()

    for dy in range(-1, 2):
        for dx in range(-1, 2):
            nx, ny = player.x + dx, player.y + dy
            if 0 <= nx < MAP_WIDTH and 0 <= ny < MAP_HEIGHT:
                visible_tiles.add((nx, ny))

    current_room = None

    for room in rooms.values():
        if not room.exists: continue

        if (room.x1 <= player.x <= room.x2-1 and room.y1 <= player.y <= room.y2-1):
            current_room = room
            break

    if current_room:
        for y in range(current_room.y1, current_room.y2):
            for x in range(current_room.x1, current_room.x2):
                visible_tiles.add((x, y))

    return visible_tiles