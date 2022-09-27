from dataclasses import dataclass
from typing import Tuple


@dataclass()
class LevelData:
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
    content: str
    unlock: int