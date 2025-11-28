from utils import generate_map, move_player
from screens import start_screen, get_player_name
from const import *
import input_handler
import os, keyboard as kb, time, sys, msvcrt

map_data = generate_map(HEIGHT, WIDTH)
player_x = 1
player_y = 1
message = "Hello hello"
player_level = 1
player_max_hp = PLAYER_INITIAL_HP
player_hp = player_max_hp

#start_screen() # 나중에 활성화
#playerName = get_player_name()

#입력 스레드 시작
os.system('cls')
input_handler.start_listener()

while True:
    buffer = ""
    buffer+= "\033[H"
    buffer+= f"{message}\n"
    for row in map_data:
        buffer += ''.join(row) + "\n"
    buffer += f"\nLevel:{player_level}    Hits:{player_hp}({player_max_hp})    Str:    Gold:    Armor:    \n"
    print(buffer, end="")

    decision = input_handler.last_key
    map_data,player_x, player_y = move_player(map_data, player_x, player_y, decision)

    time.sleep(0.12) #추후 조정