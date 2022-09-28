import typing

import pygame

from new_app.supports import ImportSupport, texture_dir


class ExplosionParticle(pygame.sprite.Sprite):
    def __init__(self, position: int):
        super(ExplosionParticle, self).__init__()
        self.frame_index = 0
        self.animation_speed = 0.5
        self.frames = ImportSupport.import_folder(texture_dir("character/dust_particles/explosion"))

        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(center=position)

    def animate(self) -> typing.NoReturn:
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.frames):
            self.kill()
        else:
            self.image = self.frames[int(self.frame_index)]

    def update(self, shift: int) -> typing.NoReturn:
        self.animate()
        self.rect.x += shift


__all__ = [
    "ExplosionParticle"
]
