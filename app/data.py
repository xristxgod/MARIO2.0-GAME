from typing import Tuple
from dataclasses import dataclass

from app.settings import LEVELS_COUNT
from app.supports import texture_dir, level_dir


@dataclass()
class BaseLevel:
    terrain: str
    coins: str
    fgPalms: str
    bgPalms: str
    crates: str
    enemies: str
    constrains: str
    player: str
    grass: str
    nodePosition: Tuple[int, int]
    nodeGraphic: str
    unlock: int


def _generate_level(count: Tuple[int, int] = LEVELS_COUNT) -> Tuple:
    levels_lst = []
    level_positions = {
        0: (110, 400),
        1: (300, 220),
        2: (480, 610),
        3: (610, 350),
        4: (880, 210),
        5: (1050, 400)
    }

    for num in range(count[0], count[1] + 1):
        levels_lst.append(BaseLevel(
            terrain=level_dir(f"{num}/level_{num}_terrain.csv"),
            coins=level_dir(f"{num}/level_{num}_coins.csv"),
            fgPalms=level_dir(f"{num}/level_{num}_fg_palms.csv"),
            bgPalms=level_dir(f"{num}/level_{num}_bg_palms.csv"),
            crates=level_dir(f"{num}/level_{num}_crates.csv"),
            enemies=level_dir(f"{num}/level_{num}_enemies.csv"),
            constrains=level_dir(f"{num}/level_{num}_constraints.csv"),
            player=level_dir(f"{num}/level_{num}_player.csv"),
            grass=level_dir(f"{num}/level_{num}_grass.csv"),
            nodePosition=level_positions[num],
            nodeGraphic=texture_dir(f"menu/{num}"),
            unlock=num if num + 1 > count[1] else num + 1
        ))
    return tuple(levels_lst)


levels: Tuple[BaseLevel] = _generate_level()

__all__ = [
    "levels",
    "BaseLevel"
]
