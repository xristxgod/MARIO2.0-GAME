from typing import Tuple
from enum import Enum


LEVELS_COUNT: Tuple[int, int] = (0, 5)

VERTICAL_TILE_NUMBER: int = 11
TILE_SIZE: int = 64


class Condition(Enum):
    menu = "menu"
    level = "level"


class ScreenConfig:
    _SCREEN_WIDTH = 1200
    _SCREEN_HEIGHT = VERTICAL_TILE_NUMBER * TILE_SIZE

    @property
    def width(self) -> int:
        return self._SCREEN_WIDTH

    @property
    def height(self) -> int:
        return self._SCREEN_HEIGHT

    @property
    def screen(self) -> Tuple[int, int]:
        return self._SCREEN_WIDTH, self._SCREEN_HEIGHT


screen = ScreenConfig()


__all__ = [
    "VERTICAL_TILE_NUMBER", "TILE_SIZE",
    "LEVELS_COUNT",
    "Condition",
    "screen",
]