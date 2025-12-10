from datetime import datetime, timezone, timedelta
from const import *
from entity_const import *
from map_const import *

def draw(map_data, entities, message):
    screen_data = [j[:] for j in map_data]

    for entity in entities:
        x, y = entity.coordinate()
        screen_data[y][x] = entity.char

    buffer = []
    buffer.append("\033[H\033[?25l")
    buffer.append(f"{message}\033[K\n")

    for row in screen_data:
        temp = ""
        for char in row:
            temp += COLOR_TABLE.get(char, char)
        buffer.append(temp + "\n")
            
    kst = timezone(timedelta(hours=9))
    now = datetime.now(kst)
    clock = now.strftime('%I:%M')
    player = entities[0]

    buffer.append(
        f"{COLOR_YELLOW}Depth:12    "
        f"{COLOR_YELLOW}HP:{player.hp}/{player.max_hp}    "
        f"{COLOR_YELLOW}Strength:{player.strength}/{player.max_strength}    "
        f"{COLOR_YELLOW}Gold:{player.gold}    "
        f"{COLOR_YELLOW}Armor:{player.armor}    "
        f"{COLOR_YELLOW}Rank:{RANK_TITLES[player.rank]}{COLOR_RESET}\n"
        f"{' '*75}{clock}"
    )

    print("".join(buffer), end='')