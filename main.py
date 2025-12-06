from utils import generate_rooms, connect_rooms
from screens import start_screen, get_player_name
import map_generator as mg
from const import *
import input_handler
import os, time
from renderer import draw
from player import Player

TPS = 8
TICK_TIME = 1 / TPS
ROOMS_ROW = 3
ROOMS_COL = 3

map_data, rooms, parents = mg.MapGenerator(MAP_WIDTH, MAP_HEIGHT, ROOMS_ROW, ROOMS_COL).generate()

#start_screen() # 나중에 활성화
#player_name = get_player_name()
player = Player(rooms[0,0].x1+2, rooms[0,0].y1+2, "{player_name}")
message = "Hello {player.name}"

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
            dx, dy = MOVES[key]
            break
        
    player.move(dx, dy, map_data)

    # 화면 출력
    draw(map_data, player, message)