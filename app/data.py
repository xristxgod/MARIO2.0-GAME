from dataclasses import dataclass
from typing import Tuple

from app.inc import graphics_dir, levels_dir


@dataclass()
class LevelOne:
    terrain: str = levels_dir.get("level_zero/level_0_terrain.csv")
    coins: str = levels_dir.get("level_zero/level_0_coins.csv")
    fgPalms: str = levels_dir.get("level_zero/level_0_fg_palms.csv")
    bgPalms: str = levels_dir.get("level_zero/level_0_bg_palms.csv")
    crates: str = levels_dir.get("level_zero/level_0_crates.csv")
    enemies: str = levels_dir.get("level_zero/level_0_enemies.csv")
    constrains: str = levels_dir.get("level_zero/level_0_constraints.csv")
    player: str = levels_dir.get("level_zero/level_0_player.csv")
    grass: str = levels_dir.get("level_zero/level_0_grass.csv")
    nodePosition: Tuple[int, int] = (110, 400)
    nodeGraphic: str = graphics_dir.get("menu/level_zero")
    unlock: int = 1
