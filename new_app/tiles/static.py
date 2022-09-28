import pygame

from ..base import BaseTile
from ..supports import texture_dir


class StaticTile(BaseTile):
    def __init__(self, size: int, x: int, y: int, surface: pygame.Surface):
        super(StaticTile, self).__init__(size, x, y)
        self.image = surface


class Crate(StaticTile):
    def __init__(self, size: int, x: int, y: int):
        super().__init__(size, x, y, pygame.image.load(texture_dir("terrain/crate.png")).convert_alpha())
        self.rect = self.image.get_rect(bottomleft=(x, y + size))


__all__ = [
    "StaticTile",
    "Crate"
]
