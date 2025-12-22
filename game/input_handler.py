import msvcrt

def get_action():
    if msvcrt.kbhit():
        key = msvcrt.getch().lower()

        if key == b'w':
            return (0, -1)
        elif key == b'a':
            return (-1, 0)
        elif key == b's':
            return (0, 1)
        elif key == b'd':
            return (1, 0)
        
    return (0, 0)