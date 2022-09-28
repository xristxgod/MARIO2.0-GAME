import random
import typing

import pygame

from new_app.supports import texture_dir
from new_app.assets.tiles import AnimatedTile


class Enemy(AnimatedTile):
    def __init__(self, size: int, x: int, y: int):
        super().__init__(size, x, y, texture_dir("enemy/run"))
        self.rect.y += size - self.image.get_size()[1]
        self.speed = random.randint(3, 5)

    def move(self) -> typing.NoReturn:
        self.rect.x += self.speed

    def reverse_image(self) -> typing.NoReturn:
        if self.speed > 0:
            self.image = pygame.transform.flip(self.image, True, False)

    def reverse(self) -> typing.NoReturn:
        self.speed *= -1

    def update(self, shift: int) -> typing.NoReturn:
        self.rect.x += shift
        self.animate()
        self.move()
        self.reverse_image()


__all__ = [
    "Enemy"
]
