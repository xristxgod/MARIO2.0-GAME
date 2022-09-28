import os
import math
from typing import NoReturn
from typing import Any, Callable, Dict
from dataclasses import dataclass

import pygame

from new_app.core import FPS
from new_app.base import BaseDraw
from new_app.supports import ImportSupport, texture_dir, sound_dir


@dataclass()
class PlayerParticleData:
    jump: Callable


def _wave_value():
    return 255 if math.sin(pygame.time.get_ticks()) >= 0 else 0


class _Sound:
    JUMP_SOUND = pygame.mixer.Sound(sound_dir("effects/jump.wav"))
    HIT_SOUND = pygame.mixer.Sound(sound_dir("effects/hit.wav"))


class _PlayerAsset(BaseDraw):
    TEXTURE_PATH: str = texture_dir("textures/character")

    def __init__(self):
        self._assets = {"idle": [], "run": [], "jump": [], "fall": []}

    def __getitem__(self, item: str) -> Any:
        return self._assets[item]

    @property
    def asset(self) -> Dict:
        return self._assets

    def draw(self) -> '_PlayerAsset':
        for path in self.TEXTURE_PATH:
            self._assets[path] = ImportSupport.import_folder(os.path.join(self.TEXTURE_PATH, path))
        return self


class _PlayerAnimation(_Sound):
    PARTICLES = ImportSupport.import_folder(texture_dir("character/dust_particles/run"))

    def __init__(self, surface: pygame.Surface, particles: PlayerParticleData):
        self.fps = FPS()
        self.animation_speed = 0.15
        self.display_surface = surface
        self.animations_particles = particles


class _PlayerPosition(_Sound):
    SPEED = 8
    GRAVITY = 0.8
    JUMP_SPEED = -16
    FACING_RIGHT = True
    ON_GROUND = False
    ON_CEILING = False
    ON_LEFT = False
    ON_RIGHT = False

    def __init__(self, status: str, rect: pygame.Rect):
        self.status = status
        self.direction = pygame.math.Vector2(0, 0)
        self.collision_rect = pygame.Rect(rect.topleft, (50, rect.height))

    def set_status(self) -> NoReturn:
        if self.direction.y < 0:
            self.status = "jump"
        elif self.direction.y > 1:
            self.status = "fall"
        else:
            if self.direction.x != 0:
                self.status = "run"
            else:
                self.status = "idle"

    def apply_gravity(self) -> NoReturn:
        self.direction.y += self.GRAVITY
        self.collision_rect.y += self.direction.y

    def input(self) -> NoReturn:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.FACING_RIGHT = True
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.FACING_RIGHT = False
        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE] and self.ON_GROUND:
            self.direction.y = self.JUMP_SPEED
            self.JUMP_SOUND.play()


class _PlayerStatus(_Sound):
    HURT_TIME = 0
    INVINCIBLE = False
    INVINCIBILITY_DURATION = 500

    def __init__(self, health: int = 100):
        self.health = health

    def damage(self) -> NoReturn:
        self.HIT_SOUND.play()
        self.health -= 10
        self.INVINCIBLE = True
        self.HURT_TIME = pygame.time.get_ticks()

    def invincibility_timer(self) -> NoReturn:
        if self.INVINCIBLE:
            if pygame.time.get_ticks() - self.HURT_TIME >= self.INVINCIBILITY_DURATION:
                self.INVINCIBLE = False


class Player(pygame.sprite.Sprite):

    __slots__ = (
        "fps", "animation_speed"
        "assets", "image", "rect",
        "animation", "position", "status",
        "sound"
    )

    def __init__(self, position: int, surface: pygame.Surface, health: int, particles: PlayerParticleData):
        super(Player, self).__init__()
        self.fps = FPS()
        self.animation_speed = 0.15

        self.assets = _PlayerAsset().draw()
        self.image = self.assets["idle"][self.fps.index]
        self.rect = self.image.get_rect(topleft=position)

        self.animation = _PlayerAnimation(surface, particles)
        self.position = _PlayerPosition(status="idle", rect=self.rect)
        self.status = _PlayerStatus(health=health)

    def animate(self) -> NoReturn:
        assets = self.assets[self.position.status]

        self.fps.index += self.animation_speed
        if self.fps.index >= len(assets):
            self.fps.index = 0

        image = assets[int(self.fps.index)]
        if self.position.FACING_RIGHT:
            self.image = image
            self.rect.bottomleft = self.position.collision_rect.bottomleft
        else:
            flipped_image = pygame.transform.flip(image, True, False)
            self.image = flipped_image
            self.rect.bottomleft = self.position.collision_rect.bottomleft

        if self.status.INVINCIBLE:
            alpha = _wave_value()
            self.image.set_alpha(alpha)
        else:
            self.image.set_alpha(255)

        self.rect = self.image.get_rect(midbottom=self.rect.midbottom)

    def dust_animation(self) -> NoReturn:
        if self.position.status == 'run' and self.position.ON_GROUND:
            self.animation.fps.index += self.animation.animation_speed
            if self.animation.fps.index >= len(self.animation.PARTICLES):
                self.animation.fps.index = 0

            dust_particle = self.animation.PARTICLES[int(self.animation.fps.index)]
            position = self.rect.bottomleft - pygame.math.Vector2(6, 10)
            if self.position.FACING_RIGHT:
                self.animation.display_surface.blit(dust_particle, position)
            else:
                self.animation.display_surface.blit(pygame.transform.flip(dust_particle, True, False), position)

    def update(self) -> NoReturn:
        self.position.input()
        self.position.set_status()
        self.animate()
        self.dust_animation()
        self.status.invincibility_timer()
        _wave_value()


__all__ = [
    "Player"
]
