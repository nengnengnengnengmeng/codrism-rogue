from consts.const import *
from consts.entity_const import *
from consts.map_const import *
from utils.compass import get_compass_direction

def draw(map_data, entities, items, message, remaining_time, visible_tiles, seen_tiles, stair):
    player = entities[0]

    buffer = []
    buffer.append("\033[H\033[?25l")

    mins, secs = divmod(int(max(0, remaining_time)), 60)
    time_str = f"남은 시간: {mins:02d}분 {secs:02d}초\n"
    buffer.append(f"{time_str:}")

    entities2 = {(entity.x, entity.y): entity for entity in entities}
    items2 = {(item.x, item.y): item for item in items}

    screen_rows = []
    for y in range(len(map_data)):
        row = ""
        for x in range(len(map_data[0])):
            char = map_data[y][x]
            if (x, y) in visible_tiles:
                if (x, y) in entities2:
                    row += entities2[(x, y)].char
                elif (x, y) in items2:
                    row += items2[(x, y)].char
                else:
                    row += COLOR_TABLE.get(char, char)

            elif (x, y) in seen_tiles:
                row += f"\033[38;5;240m{char}\033[0m"

            else:
                row += " "

        screen_rows.append(row)

    buffer.append("\n".join(screen_rows))

    buffer.append(
        f"\033[K "
        f"{COLOR_YELLOW}Depth:{player.depth}  "
        f"{COLOR_YELLOW}HP:{player.hp}/{player.max_hp}  "
        f"{COLOR_YELLOW}STR:{player.strength}/{player.max_strength}  "
        f"{COLOR_YELLOW}DEF:{player.armor}  "
        f"{COLOR_YELLOW}$:{player.gold}  "
        f"{COLOR_YELLOW}RANK:{RANK_TITLES[player.rank]}{COLOR_RESET}  "
        f"{COLOR_YELLOW}목표:{get_compass_direction(player, stair)}{COLOR_RESET}"
    )
    buffer.append("\033[J")

    message = message[-(SCREEN_HEIGHT - MAP_HEIGHT - 3):]
    for i in message:
        buffer.append(f"\n➤ {i}")

    buffer.append("\033[J")
    print("".join(buffer), end='')