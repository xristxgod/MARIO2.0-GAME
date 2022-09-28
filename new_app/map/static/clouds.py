import typing
import random

import pygame

from new_app.base import BaseDraw
from new_app.settings import screen
from new_app.supports import ImportSupport, texture_dir
from new_app.tiles import StaticTile


class Clouds(BaseDraw):
    def __init__(self, horizon: int, level_width: int, cloud_number: int):
        self.cloud_sprites = pygame.sprite.Group()
        self._create(horizon, level_width, cloud_number)

    def _create(self, horizon: int, level_width: int, cloud_number: int):
        cloud_surf_list = ImportSupport.import_folder(texture_dir('decoration/clouds'))
        for cloud in range(cloud_number):
            sprite = StaticTile(
                0, random.randint(-screen.width, level_width + screen.width),
                random.randint(0, horizon), random.choice(cloud_surf_list)
            )
            self.cloud_sprites.add(sprite)

    def draw(self, surface: pygame.Surface, shift: int) -> typing.NoReturn:
        self.cloud_sprites.update(shift)
        self.cloud_sprites.draw(surface)


__all__ = [
    "Clouds"
]
