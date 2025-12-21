import math

def get_compass_direction(player, map_data):
    for y, row in enumerate(map_data):
        if '>' in row:
            stair_pos = (row.index('>'), y)
            break

    x, y = stair_pos
    px, py = player.x, player.y
    dx = x - px
    dy = py - y

    direction = math.degrees(math.atan2(dy, dx))

    if direction < 0:
        direction += 360

    if 22.5 <= direction < 67.5: return "↗"
    if 67.5 <= direction < 112.5: return "↑"
    if 112.5 <= direction < 157.5: return "↖"
    if 157.5 <= direction < 202.5: return "←"
    if 202.5 <= direction < 247.5: return "↙"
    if 247.5 <= direction < 292.5: return "↓"
    if 292.5 <= direction < 337.5: return "↘"
    return "→"