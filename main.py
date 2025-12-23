import os
import time
import msvcrt
import random as rand

from consts.const import *
from consts.map_const import *
from entities.player import Player
from entities.item import Item
from entities.entity import Entity
import game.input_handler as input_handler
import map.map_generator as mg
from map.spawner import spawn_entity, spawn_item
import screen.renderer as renderer
import screen.screens as screens
from utils.astar import Astar
from utils.fov import fov
import utils.log as log

def initialize_level(depth, player=None):
    map_data, rooms, parents, stair = mg.MapGenerator(MAP_WIDTH, MAP_HEIGHT, ROOMS_ROW, ROOMS_COL).generate()

    valid_rooms = [room for room in rooms.values() if room.exists]
    start_room = rand.choice(valid_rooms)

    x = rand.randint(start_room.x1 + 1, start_room.x2 - 2)
    y = rand.randint(start_room.y1 + 1, start_room.y2 - 2)
    
    if player is None:
        player = Player(x, y, "Player")
    else:
        player.x = x
        player.y = y

    entities = [player]
    items = []

    goalkeeper_loc = (rand.randint(stair[0] - 1, stair[0] + 1), rand.randint(stair[1] - 1, stair[1] + 1))
    spawn_entity(rooms, entities, map_data, depth, start_room=start_room, location=goalkeeper_loc)

    monster = 1 + depth
    for _ in range(monster):
        spawn_entity(rooms, entities, map_data, depth, start_room=start_room)

    item_count = 1 + depth
    for _ in range(item_count):
        spawn_item(rooms, items, map_data)

    astar = Astar(map_data, player, entities)

    return map_data, rooms, entities, items, player, stair, astar

def main():
    player_name = "Player"
    
    map_data, rooms, entities, items, player, stair, astar = initialize_level(1)

    visible_tiles = set()
    seen_tiles = set()

    visible_tiles = fov(map_data, player, rooms)
    seen_tiles.update(visible_tiles)

    start_time = time.time()
    turn = 0

    os.system('cls')
    renderer.draw(map_data, entities, items,[f"Hello {player_name}"], TIME_LIMIT, visible_tiles, seen_tiles, stair)

    while True:
        elapsed_time = time.time() - start_time
        remaining_time = TIME_LIMIT - elapsed_time

        action = input_handler.get_action()
        dx, dy = action

        if dx != 0 or dy != 0:
            log.initialize()
            player.move(dx, dy, map_data, entities)

            visible_tiles = fov(map_data, player, rooms)
            seen_tiles.update(visible_tiles)

            if map_data[player.y][player.x] == '>':
                pause_time = time.time()
                os.system('cls')

                mins, secs = divmod(int(max(0, remaining_time)), 60)
                time_str = f"남은 시간: {mins:02d}분 {secs:02d}초\n"
                
                print(f"지하 {player.depth}층을 클리어했습니다")
                print(f"현재 배율: {MULTIPLIERS.get(player.depth, 1)}")
                print(f"다음 배율: {MULTIPLIERS.get(player.depth + 1, 1)}")
                print(f"{time_str}")
                if player.depth == 1: print("\n[1] 원금만 찾고 나가기")
                else: print("[1] 익절하고 나가기")
                print(f"[2] 지하 {player.depth+1}층 도전하기")

                while True:
                    key = msvcrt.getch()

                    if key == b'1':
                        os.system('cls')
                        print(f"{MULTIPLIERS.get(player.depth, 1)}")
                        time.sleep(3)
                        exit()

                    elif key == b'2':
                        pause_time2 = time.time() - pause_time
                        start_time += pause_time2

                        log.log(f"지하 {player.depth+1}층으로 내려갑니다")
                        player.depth += 1
                        player.hp = min(player.max_hp, player.hp + 5)
                        map_data, rooms, entities, items, player, stair, astar = initialize_level(player.depth, player)

                        seen_tiles = set()
                        visible_tiles = fov(map_data, player, rooms)
                        seen_tiles.update(visible_tiles)

                        renderer.draw(map_data, entities, items, log.get(), remaining_time, visible_tiles, seen_tiles, stair)
                        break

                continue

            for entity in entities:
                if entity.type != "Player":
                    distance = abs(entity.x - player.x) + abs(entity.y - player.y)
                    if distance <= 15:
                        path = astar.get_path(entity)
                        if path:
                            nx, ny = path[0]
                            dx, dy = (nx - entity.x, ny - entity.y)
                        else: dx, dy = (0,0)
                    entity.move(dx, dy, map_data, entities)

            for item in items:
                if item.x == player.x and item.y == player.y:
                    item.use(player)
                    item.get_collected = True

            if rand.random() < (SPAWN_RATE*0.01):
                spawn_entity(rooms, entities, map_data, player.depth)

            turn+=1
            if turn % 15 == 0:
                player.hp = min(player.max_hp, player.hp + 1)

            dead_entities = []
            baby = []
            for entity in entities:
                if entity.is_dead and entity.type != "Player":
                    dead_entities.append(entity)

                    if entity.type == "Slime":
                        log.log(f"슬라임이 둘로 쪼개졌다")
                        baby.append(Entity(entity.x, entity.y, "Mini Slime"))

                        spawn_second = False
                        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
                            nx, ny = entity.x + dx, entity.y + dy

                            if (0 <= nx < MAP_WIDTH and 0 <= ny < MAP_HEIGHT and map_data[ny][nx] == '.' and not any(e.x == nx and e.y == ny for e in entities)):
                                baby.append(Entity(nx, ny, "Mini Slime"))
                                spawn_second = True

                        if not spawn_second:
                            baby.append(Entity(entity.x, entity.y, "Mini Slime"))

                    player.gold += rand.randint(entity.gold_reward[0], entity.gold_reward[1])
                    player.xp += entity.xp_reward
                    log.log(f"{entity.type}를 처치했다")
                    player.level_up()

            entities = [e for e in entities if e not in dead_entities]
            entities.extend(baby)

            collected_items = []
            for item in items:
                if item.get_collected:
                    collected_items.append(item)
            items = [i for i in items if i not in collected_items]

            if player.hp <= 0 or remaining_time <= 0:
                os.system('cls')
                if remaining_time <= 0:
                    print("시간 초과")
                    multip = MULTIPLIERS.get(player.depth, 1)
                else:
                    print("당신은 사망했습니다")
                    multip = 0
                print(f"보상: {multip}배")
                time.sleep(2)
                exit()

        renderer.draw(map_data, entities, items, log.get(), remaining_time, visible_tiles, seen_tiles, stair)

if __name__ == "__main__":
    main()