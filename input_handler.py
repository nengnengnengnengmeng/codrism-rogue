import threading, keyboard

running = True
last_key = None

def _input_listener():
    global running, last_key

    while running:
        event = keyboard.read_event()
        
        if event.event_type == keyboard.KEY_DOWN:
            last_key = event.name
        
        elif event.event_type == keyboard.KEY_UP:
            last_key = None

def start_listener():
    listener_thread = threading.Thread(target=_input_listener, daemon=True)
    listener_thread.start()

def stop_listener():
    global running
    running = False