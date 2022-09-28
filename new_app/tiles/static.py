import pygame

from ..base import BaseTile
from ..supports import texture_dir


class StaticTile(BaseTile):
    def __init__(self, size: int, x: int, y: int, surface: pygame.Surface):
        super(StaticTile, self).__init__(size, x, y)
        self.image = surface


__all__ = [
    "StaticTile"
]
