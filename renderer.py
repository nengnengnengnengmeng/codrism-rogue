from datetime import datetime, timezone, timedelta
from const import *

def draw(map_data, entities, message):
    buffer = ""
    buffer+= "\033[H"
    buffer += f"{message}\033[K\n"
    length = len(buffer)

    for row in map_data:
        buffer += "".join(row) + "\n"

    for entity in entities:
        x, y = entity.coordinate()
        buffer = buffer[:length-1 +y*(MAP_WIDTH+1) +x+1] + entity.char + buffer[length-1 +y*(MAP_WIDTH+1) +x+2:]

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

    print(buffer, end='')