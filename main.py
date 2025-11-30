from utils import generate_map, move_player
from screens import start_screen, get_player_name
from const import *
import input_handler
import os, keyboard as kb, time, sys, msvcrt
from datetime import datetime
from renderer import draw
from player import Player

TPS = 5
TICK_TIME = 1 / TPS

map_data = generate_map(MAP_HEIGHT, MAP_WIDTH)
player = Player(1, 1, "{player_name}")
message = "Hello {player.name}"

dx = 0
dy = 0

#start_screen() # 나중에 활성화
#player_name = get_player_name()


# 입력 스레드 시작
os.system('cls')
input_handler.start_listener()

last_tick = time.time()

while True:
    now = datetime.now()
    clock = now.strftime('%I:%M')
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

    map_data,player.x, player.y = move_player(map_data, player.x, player.y, (dx, dy))

    # 화면 출력
    draw(map_data, player, message)