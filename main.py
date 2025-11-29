from utils import generate_map, move_player
from screens import start_screen, get_player_name
from const import *
import input_handler
import os, keyboard as kb, time, sys, msvcrt

TPS = 10
TICK_TIME = 1 / TPS

map_data = generate_map(HEIGHT, WIDTH)
player_x = 1
player_y = 1
message = "Hello hello"
player_level = 1
player_max_hp = PLAYER_INITIAL_HP
player_hp = player_max_hp

dx = 0
dy = 0

#start_screen() # 나중에 활성화
#playerName = get_player_name()


# 입력 스레드 시작
os.system('cls')
input_handler.start_listener()

last_tick = time.time()

while True:
    
    # 틱 계산
    now = time.time()
    delta = now - last_tick

    if delta < TICK_TIME:
        time.sleep(TICK_TIME - delta)
        continue

    last_tick = now

    # 입력 처리
    dx = 0
    dy = 0

    for key in input_handler.pressed_keys:
        if key in MOVES:
            mx, my = MOVES[key]
            dx += mx
            dy += my

            decision = key

    map_data,player_x, player_y = move_player(map_data, player_x, player_y, (dx, dy))

    # 화면 표시
    buffer = ""
    buffer+= "\033[H"
    buffer+= f"{message}\n"
    for row in map_data:
        buffer += ''.join(row) + "\n"
    buffer += f"\nLevel:{player_level}    Hits:{player_hp}({player_max_hp})    Str:    Gold:    Armor:    \n"
    print(buffer, end="")