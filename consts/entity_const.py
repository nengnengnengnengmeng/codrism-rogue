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
        "hp": 25,
        "strength": 14,
        "armor": 12,
        "damage_dice": (1, 6),
        "rank": 0,
        "xp": 0,
        "gold": 0,
    },
    
    "Kestral": {
        "char": "K",
        "hp": 5,
        "strength": 8, 
        "armor": 8,
        "damage_dice": (1, 4),
        "xp_reward": 5,
        "gold_reward": (1, 3),
        "rank": 0,
    },

    "Bat": {
        "char": "B",
        "hp": 8,
        "strength": 9,
        "armor": 11,
        "damage_dice": (1, 4),
        "xp_reward": 7,
        "gold_reward": (2, 5),
        "rank": 1,
    },

    "Ice monster": {
        "char": "I",
        "hp": 14,
        "strength": 11,
        "armor": 11,
        "damage_dice": (1, 6),
        "xp_reward": 12,
        "gold_reward": (5, 10),
        "rank": 2,
    },

    "Emu": {
        "char": "E",
        "hp": 22,
        "strength": 13,
        "armor": 13,
        "damage_dice": (2, 5),
        "xp_reward": 15,
        "gold_reward": (8, 15),
        "rank": 3,
    },

    "Slime": {
        "char": "S",
        "hp": 24,
        "strength": 10,
        "armor": 5,
        "damage_dice": (1, 3),
        "xp_reward": 15,
        "gold_reward": (6, 12),
        "rank": 4,
    },

    "Mini Slime": {
        "char": "S",
        "hp": 12,
        "strength": 5,
        "armor": 3,
        "damage_dice": (1, 2),
        "xp_reward": 7,
        "gold_reward": (3, 6),
        "rank": 3,
    },

    "Orc": {
        "char": "O",
        "hp": 35,
        "strength": 16,
        "armor": 14,
        "damage_dice": (2, 6),
        "xp_reward": 25,
        "gold_reward": (15, 30),
        "rank": 5,
    },

    "Rattlesnake": {
        "char": "R",
        "hp": 15,
        "strength": 15,
        "armor": 16,
        "damage_dice": (3, 4),
        "xp_reward": 20,
        "gold_reward": (12, 25),
        "rank": 6,
    },

    "Centaur": {
        "char": "C",
        "hp": 45,
        "strength": 18,
        "armor": 15,
        "damage_dice": (3, 6),
        "xp_reward": 40,
        "gold_reward": (30, 60),
        "rank": 7,
    },

}

ITEMS = {
    "Health Potion": {
        "char": "\033[31m!\033[0m",
        "effect_value": 10,
    },
    "Strength Potion": {
        "char": "\033[1;35m!\033[0m",
        "effect_value": 3
    }
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