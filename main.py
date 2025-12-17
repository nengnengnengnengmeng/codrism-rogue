from screens import start_screen, get_player_name
import map_generator as mg
from const import *
import input_handler
import os, time
from renderer import draw
from player import Player
from entity import Entity
import random as rand
import log
from astar import Astar

ROOMS_ROW = 3
ROOMS_COL = 3

map_data, rooms, parents = mg.MapGenerator(MAP_WIDTH, MAP_HEIGHT, ROOMS_ROW, ROOMS_COL).generate()

player_name = "Player"
#start_screen() # 나중에 활성화
#player_name = get_player_name()
player = Player(rooms[0,0].x1+2, rooms[0,0].y1+2, "player_name")
orc_1 = Entity(rooms[1,1].x1+2, rooms[1,1].y1+2, "Orc")
entities = [player, orc_1]

os.system('cls')
draw(map_data, entities, f"Hello {player_name}")
while True:
    log.initialize()
    dx, dy = input_handler.get_action()
    player.move(dx, dy, map_data, entities)

    for entity in entities:
        if entity.type != "Player":
            distance = abs(entity.x - player.x) + abs(entity.y - player.y)
            if distance <= 10:
                astar = Astar(map_data, entity, player)
                path = astar.get_path()
                if path:
                    nx, ny = path[0]
                entity.move(nx - entity.x, ny - entity.y, map_data, entities)

    for entity in entities:
        if entity.hp <= 0 and entity.type != "Player":
            del entities[entities.index(entity)]
            player.gold += 10
            player.rank += 1
            log.log(f"{entity.type}를 처치했다")
        
        if player.hp <= 0:
            os.system('cls')
            print("당신은 사망했습니다")
            time.sleep(2)
            exit()

    logged_messages = log.get()

    # 화면 출력
    draw(map_data, entities, logged_messages)