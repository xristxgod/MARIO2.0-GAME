from typing import Tuple

import pygame


class Node(pygame.sprite.Sprite):
    def __init__(self, position: Tuple[int, int], status: str, icon_speed: int):
        super(Node, self).__init__()
        self.image = pygame.Surface((100, 80))
        if status == "available":
            self.image.fill("red")
        else:
            self.image.fill("grey")
        self.rect = self.image.get_rect(center=position)

        self.detection_zone = pygame.Rect(
            self.rect.centerx - (icon_speed / 2),
            self.rect.centery - (icon_speed / 2),
            icon_speed,
            icon_speed
        )


class Icon(pygame.sprite.Sprite):
    def __init__(self, position: Tuple[int, int]):
        super(Icon, self).__init__()
        self.position = position
        self.image = pygame.Surface((20, 20))
        self.image.fill("blue")
        self.rect = self.image.get_rect(center=position)

    def update(self):
        self.rect.center = self.position


__all__ = [
    "Node",
    "Icon"
]
