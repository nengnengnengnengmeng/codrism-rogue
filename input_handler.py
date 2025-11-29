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