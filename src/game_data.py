import os

from config import LEVEL_0, GRAPHICS_OVER_WORLD_LEVEL_0


level_0 = {
    "terrain": os.path.join(LEVEL_0, "level_0_terrain.csv"),
    "coins": os.path.join(LEVEL_0, "level_0_coins.csv"),
    "fg_palms": os.path.join(LEVEL_0, "level_0_fg_palms.csv"),
    "bg_palms": os.path.join(LEVEL_0, "level_0_bg_palms.csv"),
    "crates": os.path.join(LEVEL_0, "level_0_crates.csv"),
    "enemies": os.path.join(LEVEL_0, "level_0_enemies.csv"),
    "constrains": os.path.join(LEVEL_0, "level_0_constraints.csv"),
    "player": os.path.join(LEVEL_0, "level_0_player.csv"),
    "grass": os.path.join(LEVEL_0, "level_0_grass.csv"),
    "node_pos": (110, 400),
    "node_graphic": GRAPHICS_OVER_WORLD_LEVEL_0,
    "content": "this is level level_zero",
    "unlock": 1
}
level_1 = {
    "node_pos": (300, 220),
    "content": "this is level level_one",
    "unlock": 2
}
level_2 = {"node_pos": (480, 610), "content": "this is level level_two", "unlock": 3}
level_3 = {"node_pos": (610, 350), "content": "this is level level_three", "unlock": 4}
level_4 = {"node_pos": (880, 210), "content": "this is level level_four", "unlock": 5}
level_5 = {"node_pos": (1050, 400), "content": "this is level level_five", "unlock": 5}

levels = {
    0: level_0,
    1: level_1,
    2: level_2,
    3: level_3,
    4: level_4,
    5: level_5,
}
