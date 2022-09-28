import random
from typing import NoReturn
from typing import List, Tuple

import pygame

from new_app.supports import ImportSupport, texture_dir
from new_app.settings import VERTICAL_TILE_NUMBER, TILE_SIZE, Condition, screen
from new_app.base import BaseDraw


def _transform(path: str):
    data = pygame.image.load(texture_dir(path)).convert()
    return pygame.transform.scale(data, (screen.width, TILE_SIZE))


class _MenuPalms(BaseDraw):
    def __init__(self):
        self._palms = []

    @property
    def palms(self) -> List[Tuple]:
        return self._palms

    def draw(self, horizont: int) -> '_MenuPalms':
        palms = ImportSupport.import_folder(texture_dir("menu/palms"))
        for surface in [random.choice(palms) for _ in range(10)]:
            rect = surface.get_rect(midbottom=(
                random.randint(0, screen.width),
                (horizont * TILE_SIZE) + random.randint(50, 100)
            ))
            self._palms.append((surface, rect))
        return self


class _MenuCloud(BaseDraw):
    def __init__(self):
        self._clouds = []

    @property
    def clouds(self) -> List[Tuple]:
        return self._clouds

    def draw(self, horizont: int) -> '_MenuCloud':
        cloud_surfaces = ImportSupport.import_folder(texture_dir("menu/clouds"))
        for surface in [random.choice(cloud_surfaces) for image in range(10)]:
            rect = surface.get_rect(midbottom=(
                random.randint(0, screen.width),
                random.randint(0, (horizont * TILE_SIZE) - 100)
            ))
            self.clouds.append((surface, rect))
        return self


class Sky(BaseDraw):
    TOP = _transform("decoration/sky/sky_top.png")
    BOTTOM = _transform("decoration/sky/sky_bottom.png")
    MIDDLE = _transform("decoration/sky/sky_middle.png")

    __slots__ = (
        "horizont", "condition",
        "palms", "clouds"
    )

    def __init__(self, horizont: int, condition: Condition = Condition.level):
        self.horizont = horizont
        self.condition = condition

        if self.condition == Condition.menu:
            self.palms = _MenuPalms().draw(horizont)
            self.clouds = _MenuCloud().draw(horizont)

    def draw(self, surface: pygame.Surface) -> NoReturn:
        for row in range(VERTICAL_TILE_NUMBER):
            y = row * TILE_SIZE
            if row < self.horizont:
                surface.blit(self.TOP, (0, y))
            elif row == self.horizont:
                surface.blit(self.MIDDLE, (0, y))
            else:
                surface.blit(self.BOTTOM, (0, y))
        if self.condition == Condition.menu:
            for palm in self.palms.palms:
                surface.blit(palm[0], palm[1])
            for cloud in self.clouds.clouds:
                surface.blit(cloud[0], cloud[1])


__all__ = [
    "Sky"
]
