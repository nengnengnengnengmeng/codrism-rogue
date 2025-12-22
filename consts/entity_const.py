RANK_TITLES = [
    "",
    "Guild Novice",
    "Apprentice",
    "Journeyman",
    "Adventerer",

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
    
    "Kestral": {
        "char": "K",
        "hp": 5,
        "strength": 8,
        "armor": 6,
        "xp_reward": 4,
        "damage_dice": (1, 4),
        "gold_reward": (1,3),
        "rank": 0,
    },

    "Bat": {
        "char": "B",
        "hp": 8,
        "strength": 9,
        "armor": 12,
        "xp_reward": 5,
        "damage_dice": (1, 4),
        "gold_reward": (2,4),
        "rank": 1,
    },

    "Ice monster": {
        "char": "I",
        "hp": 15,
        "strength": 12,
        "armor": 10,
        "xp_reward": 5,
        "damage_dice": (1, 6),
        "gold_reward": (3,6),
        "rank": 2,
    },

    "Emu": {
        "char": "E",
        "hp": 15,
        "strength": 12,
        "armor": 10,
        "xp_reward": 5,
        "damage_dice": (1, 6),
        "gold_reward": (3,6),
        "rank": 3,
    },

    "Slime": {
        "char": "S",
        "hp": 15,
        "strength": 12,
        "armor": 10,
        "xp_reward": 5,
        "damage_dice": (1, 6),
        "gold_reward": (3,6),
        "rank": 4,
    },

    "Orc": {
        "char": "O",
        "hp": 12,
        "strength": 12,
        "armor": 10,
        "xp_reward": 5,
        "damage_dice": (1, 6),
        "gold_reward": (3,8),
        "rank": 5,
    },

        "Rattlesnake": {
        "char": "R",
        "hp": 12,
        "strength": 12,
        "armor": 10,
        "xp_reward": 5,
        "damage_dice": (1, 6),
        "gold_reward": (3,8),
        "rank": 5,
    },

        "Centaur": {
        "char": "C",
        "hp": 12,
        "strength": 12,
        "armor": 10,
        "xp_reward": 5,
        "damage_dice": (1, 6),
        "gold_reward": (3,8),
        "rank": 5,
    },

}

ENTITY_RANK = [
    "Kestral",
    "Bat",
    "Ice monster",
    "Emu",
    "Slime",
    "Orc",
    "Rattlesnake",
    "Centaur",
]