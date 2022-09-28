import typing

import pygame


class BaseDraw:
    def draw(self, *args, **kwargs) -> typing.Union[typing.ClassVar, typing.NoReturn]:
        raise NotImplementedError


class Tile(pygame.sprite.Sprite):
    def __init__(self, size: int, x: int, y: int):
        super(Tile, self).__init__()
        self.image = pygame.Surface((size, size))
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self, shift: int) -> typing.NoReturn:
        self.rect.x += shift


__all__ = [
    "BaseDraw",
    "Tile"
]
