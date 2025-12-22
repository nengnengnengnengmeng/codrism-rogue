from screens import start_screen, get_player_name
import map_generator as mg
from consts.const import *
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
from fov import fov

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

    monster = 1 + depth
    for _ in range(monster):
        spawn_entity(rooms, entities, "Orc", map_data, start_room=start_room)

    return map_data, rooms, entities, player, stair

def main():
    player_name = "Player"
    
    map_data, rooms, entities, player, stair = initialize_level(1)

    visible_tiles = set()
    seen_tiles = set()

    visible_tiles = fov(map_data, player, rooms)
    seen_tiles.update(visible_tiles)

    start_time = time.time()
    turn = 0

    os.system('cls')
    draw(map_data, entities, [f"Hello {player_name}"], TIME_LIMIT, visible_tiles, seen_tiles, stair)

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
                log.log(f"지하 {player.depth+1}층으로 내려갑니다")
                draw(map_data, entities, log.get(), remaining_time, visible_tiles, seen_tiles, stair)
                time.sleep(0.5)

                player.depth += 1
                player.hp = min(player.max_hp, player.hp + 5)
                map_data, rooms, entities, player, stair = initialize_level(player.depth, player)

                seen_tiles = set()
                visible_tiles = fov(map_data, player, rooms)
                seen_tiles.update(visible_tiles)

                draw(map_data, entities, log.get(), remaining_time, visible_tiles, seen_tiles, stair)
                continue

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

            if rand.random() < (SPAWN_RATE*0.01):
                spawn_entity(rooms, entities, "Orc", map_data)

            turn+=1
            if turn % 15 == 0:
                player.hp = min(player.max_hp, player.hp + 1)

            dead_entities = []
            for entity in entities:
                if entity.is_dead and entity.type != "Player":
                    dead_entities.append(entity)
                    player.gold += rand.randint(entity.gold_reward[0], entity.gold_reward[1])
                    player.xp += entity.xp_reward
                    log.log(f"{entity.type}를 처치했다")
                    player.level_up()
            entities = [e for e in entities if e not in dead_entities]

            if player.hp <= 0 or remaining_time <= 0:
                os.system('cls')
                print("당신은 사망했습니다")
                time.sleep(2)
                exit()

        draw(map_data, entities, log.get(), remaining_time, visible_tiles, seen_tiles, stair)

if __name__ == "__main__":
    main()