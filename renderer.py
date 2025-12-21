from datetime import datetime, timezone, timedelta
from consts.const import *
from consts.entity_const import *
from consts.map_const import *
from compass import get_compass_direction

def draw(map_data, entities, message, remaining_time, visible_tiles, seen_tiles):
    player = entities[0]

    buffer = []
    buffer.append("\033[H\033[?25l")

    mins, secs = divmod(int(max(0, remaining_time)), 60)
    time_str = f"남은 시간: {mins:02d}분 {secs:02d}초\n"
    buffer.append(f"{time_str:}")

    screen_rows = []
    for y in range(len(map_data)):
        row = ""
        for x in range(len(map_data[0])):
            char = map_data[y][x]
            if (x, y) in visible_tiles:
                entity_drawn = False
                for entity in entities:
                    if entity.x == x and entity.y == y:
                        row += entity.char
                        entity_drawn = True
                        break
                if not entity_drawn:
                    row += COLOR_TABLE.get(char, char)

            elif (x, y) in seen_tiles:
                row += f"\033[38;5;240m{char}\033[0m"

            else:
                row += " "

        screen_rows.append(row)

    buffer.append("\n".join(screen_rows))

    buffer.append(
        f"{COLOR_YELLOW}Depth:{player.depth}  "
        f"{COLOR_YELLOW}HP:{player.hp}/{player.max_hp}  "
        f"{COLOR_YELLOW}STR:{player.strength}/{player.max_strength}  "
        f"{COLOR_YELLOW}DEF:{player.armor}  "
        f"{COLOR_YELLOW}$:{player.gold}  "
        f"{COLOR_YELLOW}RANK:{RANK_TITLES[player.rank]}{COLOR_RESET}  "
        f"{COLOR_YELLOW}목표:{get_compass_direction(player, map_data)}{COLOR_RESET}\n"
    )
    buffer.append("\033[J")

    message = message[-(SCREEN_HEIGHT - MAP_HEIGHT - 3):]
    for i in message:
        buffer.append(f"\n➤ {i}")

    buffer.append("\033[J")
    print("".join(buffer), end='')