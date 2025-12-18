from map_const import *

class Astar:
    def __init__(self, map_data, entity, player, entities):
        self.map_data = map_data
        self.entity = entity
        self.player = player
        self.entities = entities
        
    def huristic(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def if_walkable(self, x, y):
        if x < 0 or y < 0 or x >= len(self.map_data[0]) or y >= len(self.map_data):
            return False
        if self.map_data[y][x] in WALLS:
            return False
        for entity in self.entities:
            if entity == self.entity: continue
            if entity == self.player: continue
            if entity.x == x and entity.y == y and self.map_data[y][x] == FLOOR:
                return False
            
        return True

    def get_neighbors(self, current_node):
        neighbors = []
        current_x, current_y = current_node[2], current_node[3]
        current_g = current_node[1]

        for i in range(-1, 2):
            for j in range(-1, 2):
                if abs(i) == abs(j):
                    continue
                nx = current_x + i
                ny = current_y + j
                h = self.huristic(self.player.coordinate(), (nx, ny))
                g = current_g + 1
                f = g + h
                new_node = (f, g, nx, ny, (current_x, current_y))
                if self.if_walkable(nx, ny):
                    neighbors.append(new_node)

        return neighbors

    def get_path(self):
        open_list = []
        closed_list = set()
        parents = {}

        # f, g, x, y, parent
        start_node = (0, 0, self.entity.x, self.entity.y, None)
        open_list.append(start_node)

        while open_list:
            open_list.sort(key=lambda x: x[0])
            current_node = open_list.pop(0)
            current_x, current_y = current_node[2], current_node[3]
            
            if (current_x, current_y) in closed_list:
                continue

            closed_list.add((current_x, current_y))

            if (current_x, current_y) == self.player.coordinate():
                path = []
                curr = (current_x, current_y)
                while curr is not None:
                    path.append(curr)
                    curr = parents.get(curr, None)
                path.reverse()
                return path[1:]
            
            neighbors = self.get_neighbors(current_node)

            for neighbor in neighbors:
                neighbor_x, neighbor_y = neighbor[2], neighbor[3]
                if (neighbor_x, neighbor_y) in closed_list:
                    continue

                parents[(neighbor_x, neighbor_y)] = neighbor[4]
                open_list.append(neighbor)
        return []