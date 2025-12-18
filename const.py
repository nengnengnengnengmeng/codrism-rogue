SCREEN_WIDTH = 80
SCREEN_HEIGHT = 25
MAP_HEIGHT = 22
MAP_WIDTH = 80
ROOMS_ROW = 3
ROOMS_COL = 3

ORC = "O"
MOVES = {
    'w': (0, -1),
    'a': (-1, 0),
    's': (0, 1),
    'd': (1, 0)
}

TOMBSTONE = """
             .---.
            /     \\
           /       \\
          |  R.I.P  |
          |         |
          |         |
          |         |
          |         |
          |         |
          |         |
          |         |
          |         |
         /|_________|\\
        /_/_/_/_/_/_/_\\
"""