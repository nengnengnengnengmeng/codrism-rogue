from datetime import datetime, timezone, timedelta
from const import *
from color import *

def draw(map_data, entities, message):
    buffer = ""
    buffer+= "\033[H\033[?25l"
    buffer += f"{message}\033[K\n"
    length = len(buffer)

    for row in map_data:
        buffer += "".join(row) + "\n"

    for entity in entities:
        x, y = entity.coordinate()
        buffer = buffer[:length + y * (MAP_WIDTH + 1) + x] + entity.char + buffer[length + y * (MAP_WIDTH + 1) + x + 1:]

    kst = timezone(timedelta(hours=9))
    now = datetime.now(kst)
    clock = now.strftime('%I:%M')

    player = entities[0]
    buffer += (
        f"Level:{player.level}    "
        f"Hits:{player.hp}({player.max_hp})    "
        f"Str:    Gold:    Armor:    \n"
        f"{' ' * 75}{clock}"
    )

    buffer = buffer.replace(".",COLOR_GREEN + "." + COLOR_RESET)
    for wall in WALLS:
        buffer = buffer.replace(wall, COLOR_BROWN + wall + COLOR_RESET)
    buffer = buffer.replace(DOOR, COLOR_BROWN + DOOR + COLOR_RESET)
    buffer = buffer.replace(PLAYER, COLOR_YELLOW + PLAYER + COLOR_RESET)
    for i in ["Level:", "Hits", "Str", "Gold", "Armor"]:
        buffer = buffer.replace(i, COLOR_YELLOW + i)
    print(buffer, end='')