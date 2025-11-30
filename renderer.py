from datetime import datetime

def draw(map_data, player, message):
    buffer = ""

    buffer+= "\033[H"
    buffer += f"{message}\033[K\n"

    for row in map_data:
        buffer += ''.join(row) + "\n"

    now = datetime.now()
    clock = now.strftime('%I:%M')

    buffer += (
        f"Level:{player.level}    "
        f"Hits:{player.hp}({player.max_hp})    "
        f"Str:    Gold:    Armor:    \n"
        f"{' ' * 75}{clock}"
    )

    print(buffer, end='')