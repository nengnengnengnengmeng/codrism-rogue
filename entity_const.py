RANK_TITLES = [
    "",
    "Guild Novice",
    "Apprentice",
    "Journeyman",
    ""
    ]

ENTITY_CHAR = {
    "O",    
}

ENTITIES = {
    "Player": {
        "char": "\033[1;38;5;226m☺\033[0m", 
        "hp": 12,
        "strength": 16,
        "gold": 0,
        "armor": 10,
        "rank": 0,
        "xp": 0,
        "damage_dice": (1, 6),
    },
    "Orc": {
        "char": "O",
        "hp": 20,
        "strength": 12,
        "armor": 12,
        "xp_reward": 5,
        "damage_dice": (1, 2),
        "gold_reward": (2,7),
    }
}