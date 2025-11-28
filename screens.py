import os, msvcrt, time
def start_screen():
    os.system('cls')
    print("""
        
            Rogue
            press any key to start
        
    """) # 추후 개선
    while msvcrt.kbhit():
        msvcrt.getch()
    msvcrt.getch()

def get_player_name():
    os.system('cls')
    print("""

            Rogue's Name? """, end='')
    name = input()
    return name