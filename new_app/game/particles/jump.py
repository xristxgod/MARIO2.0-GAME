import typing

import pygame

from new_app.supports import ImportSupport, texture_dir
from new_app.core import FPS


class JumpParticle(pygame.sprite.Sprite):
    def __init__(self, position: int):
        super(JumpParticle, self).__init__()
        self.fps = FPS()
        self.animation_speed = 0.5
        self.frames = ImportSupport.import_folder(texture_dir("character/dust_particles/jump"))

        self.image = self.frames[self.fps.index]
        self.rect = self.image.get_rect(center=position)

    def animate(self) -> typing.NoReturn:
        self.fps.index += self.animation_speed
        if self.fps.index >= len(self.frames):
            self.kill()
        else:
            self.image = self.frames[int(self.fps.index)]

    def update(self, shift: int) -> typing.NoReturn:
        self.animate()
        self.rect.x += shift


__all__ = [
    "JumpParticle"
]
