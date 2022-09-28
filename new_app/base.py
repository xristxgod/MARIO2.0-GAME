import typing

import pygame


class BaseController:

    def input(self) -> typing.NoReturn:
        raise NotImplementedError

    def run(self) -> typing.NoReturn:
        raise NotImplementedError


class BaseDraw:
    def draw(self, *args, **kwargs) -> typing.Union[typing.ClassVar, typing.NoReturn]:
        raise NotImplementedError


class BaseTile(pygame.sprite.Sprite):
    def __init__(self, size: int, x: int, y: int):
        super(BaseTile, self).__init__()
        self.image = pygame.Surface((size, size))
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self, shift: int) -> typing.NoReturn:
        self.rect.x += shift


__all__ = [
    "BaseDraw",
    "BaseTile",
    "BaseController"
]
