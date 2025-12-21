"""
import threading, keyboard

running = True
pressed_keys = set()

def _input_listener():
    global running, last_key

    while running:
        
        event = keyboard.read_event()
        key = event.name

        if event.event_type == keyboard.KEY_DOWN:
            pressed_keys.add(key)
        
        elif event.event_type == keyboard.KEY_UP:
            if key in pressed_keys:
                pressed_keys.remove(key)

def start_listener():
    listener_thread = threading.Thread(target=_input_listener, daemon=True)
    listener_thread.start()

def stop_listener():
    global running
    running = False
"""

import time
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