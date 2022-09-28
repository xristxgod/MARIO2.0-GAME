from random import randint

import pygame

from ..inc import graphics_dir
from .tiles import AnimatedTile


class Enemy(AnimatedTile):
    def __init__(self, size: int, x: int, y: int):
        super().__init__(size, x, y, graphics_dir("enemy/run"))
        self.rect.y += size - self.image.get_size()[1]
        self.speed = randint(3, 5)

    def move(self):
        self.rect.x += self.speed

    def reverse_image(self):
        if self.speed > 0:
            self.image = pygame.transform.flip(self.image, True, False)

    def reverse(self):
        self.speed *= -1

    def update(self, shift: int):
        self.rect.x += shift
        self.animate()
        self.move()
        self.reverse_image()