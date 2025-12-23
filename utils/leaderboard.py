import json
import os
from datetime import datetime

def load():
    if not os.path.exists("leaderboard.json"):
        return []
    
    with open("leaderboard.json", "r", encoding="utf-8") as f:
        return json.load(f)
    
def save(data):
    with open("leaderboard.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def format_time(seconds):
    mins, secs = divmod(int(max(0, seconds)), 60)
    return f"{mins:02d}:{secs:02d}"
    
def update(name, depth, gold, remaining_time):
    data = load()

    new_entry = {
        "name": name,
        "depth": depth,
        "gold": gold,
        "time": remaining_time,
        "date": datetime.now().strftime("%m-%d %H:%M")
    }

    data.append(new_entry)
    data.sort(key=lambda x: (x["depth"], x["gold"], x["time"]), reverse=True)

    data = data[:10]

    save(data)

def show():
    data = load()

    print("\n" + "="*60)
    print(f"{'RANK':<4} {'NAME':<12} {'DEPTH':<6} {'GOLD':<8} {'TIME':<8}")
    print("-" * 60)

    for i, entry in enumerate(data):
        time_str = format_time(entry['time'])
        print(f"{i+1:<4} {entry['name']:<12} {entry['depth']:<6} {entry['gold']:<8} {time_str:<8}")

    print("="*60)