import typing

import pygame

from app.settings import screen
from app.supports import texture_dir
from app.base import BaseDraw
from app.assets.tiles import AnimatedTile


class Water(BaseDraw):
    def __init__(self, top: int, level_width: int):
        self.water = pygame.sprite.Group()
        self._create(top, level_width)

    def _create(self, top: int, level_width: int):
        water_surface = texture_dir("decoration/water")
        for tile in range(int((level_width + screen.width * 2) / 192)):
            sprite = AnimatedTile(192, tile * 192 + (-screen.width), top, water_surface)
            self.water.add(sprite)

    def draw(self, surface: pygame.Surface, shift: int) -> typing.NoReturn:
        self.water.update(shift)
        self.water.draw(surface)


__all__ = [
    "Water"
]
