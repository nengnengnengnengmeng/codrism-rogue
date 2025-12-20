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
from spawner import spawn_entity
import random as rand

map_data, rooms, parents = mg.MapGenerator(MAP_WIDTH, MAP_HEIGHT, ROOMS_ROW, ROOMS_COL).generate()

player_name = "Player"
#start_screen() # 나중에 활성화
#player_name = get_player_name()
valid_rooms = [room for room in rooms.values() if room.exists]
start_room = rand.choice(valid_rooms)
x = rand.randint(start_room.x1 + 1, start_room.x2 - 2)
y = rand.randint(start_room.y1 + 1, start_room.y2 - 2)
player = Player(x, y, player_name)
entities = [player]

for _ in range(1):
    spawn_entity(rooms, entities, "Orc", map_data)
turn = 0

os.system('cls')
draw(map_data, entities, f"Hello {player_name}")
while True:
    log.initialize()
    dx, dy = input_handler.get_action()
    player.move(dx, dy, map_data, entities)

    for entity in entities:
        if entity.type != "Player":
            distance = abs(entity.x - player.x) + abs(entity.y - player.y)
            if distance <= 15:
                astar = Astar(map_data, entity, player, entities)
                path = astar.get_path()
                if path:
                    nx, ny = path[0]
                dx, dy = (nx - entity.x, ny - entity.y)
            else: dx, dy = (0,0)
            entity.move(dx, dy, map_data, entities)

    dead_entities = []
    for entity in entities:
        if entity.is_dead and entity.type != "Player":
            dead_entities.append(entity)
            player.gold += rand.randint(entity.gold_reward[0], entity.gold_reward[1])
            player.xp += entity.xp_reward
            log.log(f"{entity.type}를 처치했다")
            player.level_up()

    entities = [e for e in entities if e not in dead_entities]
        
    if player.hp <= 0:
        os.system('cls')
        print("당신은 사망했습니다")
        time.sleep(2)
        exit()

    logged_messages = log.get()

    if rand.random() < (SPAWN_RATE*0.01):
        spawn_entity(rooms, entities, "Orc", map_data)

    turn += 1
    if turn% 10 == 0:
        player.hp = min(player.max_hp, player.hp + 1)

    # 화면 출력
    draw(map_data, entities, logged_messages)