from screens import start_screen, get_player_name
import map_generator as mg
from const import *
import input_handler
import os, time
from renderer import draw
from player import Player
from entity import Entity
import random as rand

TPS = 8
TICK_TIME = 1 / TPS
ROOMS_ROW = 3
ROOMS_COL = 3

map_data, rooms, parents = mg.MapGenerator(MAP_WIDTH, MAP_HEIGHT, ROOMS_ROW, ROOMS_COL).generate()

player_name = "Player"
#start_screen() # 나중에 활성화
#player_name = get_player_name()
player = Player(rooms[0,0].x1+2, rooms[0,0].y1+2, "player_name")
orc_1 = Entity(rooms[1,1].x1+2, rooms[1,1].y1+2, "Orc")
entities = [player, orc_1]
message = f"Hello {player.name}"

# 입력 스레드 시작
os.system('cls')
draw(map_data, entities, message)
#input_handler.start_listener()

#last_tick = time.time()

while True:
    messages = []
    message = None
    dx, dy = input_handler.get_action()
    message = player.move(dx, dy, map_data, entities)
    messages.append(message)
    message = None

    for entity in entities:
        if entity.type != "Player":
            dx, dy = rand.choice(((0,1),(0,-1),(1,0),(-1,0),(0,0)))
            message = entity.move(dx, dy, map_data, entities)
            messages.append(message)
            message = None

    for entity in entities:
        if entity.hp <= 0 and entity.type != "Player":
            del entities[entities.index(entity)]
            player.gold += 10
            player.rank += 1
            message = f"{entity.type}를 처치했다"
            messages.append(message)
        
        if player.hp <= 0:
            os.system('cls')
            print("당신은 사망했습니다")
            time.sleep(2)
            exit()

    # 화면 출력
    draw(map_data, entities, messages)