logs = []

def initialize():
    global logs
    logs = []

def log(text):
    logs.append(text)

def get():
    return logs