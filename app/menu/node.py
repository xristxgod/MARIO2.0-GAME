from typing import Tuple

import pygame

from ..supports import ImportSupport


class Node(pygame.sprite.Sprite):
    def __init__(self, position: Tuple[int, int], status: str, icon_speed: int, path: str):
        super(Node, self).__init__()
        self.frames = ImportSupport.import_folder(path)
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        if status == "available":
            self.status = 'available'
        else:
            self.status = 'locked'
        self.rect = self.image.get_rect(center=position)

        self.detection_zone = pygame.Rect(
            self.rect.centerx - (icon_speed / 2),
            self.rect.centery - (icon_speed / 2),
            icon_speed,
            icon_speed
        )

    def animate(self):
        self.frame_index += 0.15
        if self.frame_index >= len(self.frames):
            self.frame_index = 0
        self.image = self.frames[int(self.frame_index)]

    def update(self):
        if self.status == "available":
            self.animate()
        else:
            tint_surf = self.image.copy()
            tint_surf.fill('black', None, pygame.BLEND_RGBA_MULT)
            self.image.blit(tint_surf, (0, 0))


__all__ = [
    "Node"
]
