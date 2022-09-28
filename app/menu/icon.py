from typing import Tuple

import pygame

from app.supports import texture_dir


class Icon(pygame.sprite.Sprite):
    def __init__(self, position: Tuple[int, int]):
        super(Icon, self).__init__()
        self.position = position
        self.image = pygame.image.load(texture_dir("menu/hat.png")).convert_alpha()
        self.rect = self.image.get_rect(center=position)

    def update(self):
        self.rect.center = self.position


__all__ = [
    "Icon"
]
