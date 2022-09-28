from new_app.assets.tiles import StaticTile

import pygame

from new_app.supports import texture_dir


class Crate(StaticTile):
    def __init__(self, size: int, x: int, y: int):
        super().__init__(size, x, y, pygame.image.load(texture_dir("terrain/crate.png")).convert_alpha())
        self.rect = self.image.get_rect(bottomleft=(x, y + size))


__all__ = [
    "Crate"
]
