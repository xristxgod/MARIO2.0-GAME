import pygame

from ..inc import ImportSupport, graphics_dir


class ParticleEffect(pygame.sprite.Sprite):

    def __init__(self, position: int, _type: str):
        super(ParticleEffect, self).__init__()
        self.frame_index = 0
        self.animation_speed = 0.5
        if _type == 'jump':
            self.frames = ImportSupport.import_folder(graphics_dir("character/dust_particles/jump"))
        if _type == 'land':
            self.frames = ImportSupport.import_folder(graphics_dir("character/dust_particles/land"))
        if _type == 'explosion':
            self.frames = ImportSupport.import_folder(graphics_dir("enemy/explosion"))
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(center=position)

    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.frames):
            self.kill()
        else:
            self.image = self.frames[int(self.frame_index)]

    def update(self, shift: int):
        self.animate()
        self.rect.x += shift
