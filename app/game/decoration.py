from typing import NoReturn
from random import choice, randint

import pygame

from app.settings import VERTICAL_TILE_NUMBER, TILE_SIZE, screen
from app.inc import ImportSupport, graphics_dir
from app.game.tiles import AnimatedTile, StaticTile


class Sky:
    def __init__(self, horizon: int, style: str = 'level'):
        self.top = pygame.image.load(graphics_dir("decoration/sky/sky_top.png")).convert()
        self.bottom = pygame.image.load(graphics_dir("decoration/sky/sky_bottom.png")).convert()
        self.middle = pygame.image.load(graphics_dir("decoration/sky/sky_middle.png")).convert()
        self.horizon = horizon

        self.top = pygame.transform.scale(self.top, (screen.width, TILE_SIZE))
        self.bottom = pygame.transform.scale(self.bottom, (screen.width, TILE_SIZE))
        self.middle = pygame.transform.scale(self.middle, (screen.width, TILE_SIZE))

        self.style = style
        if self.style == 'menu':
            palm_surfaces = ImportSupport.import_folder(graphics_dir("menu/palms"))
            self.palms = []

            for surface in [choice(palm_surfaces) for _ in range(10)]:
                x = randint(0, screen.width)
                y = (self.horizon * TILE_SIZE) + randint(50, 100)
                rect = surface.get_rect(midbottom=(x, y))
                self.palms.append((surface, rect))

            cloud_surfaces = ImportSupport.import_folder(graphics_dir("menu/clouds"))
            self.clouds = []
            for surface in [choice(cloud_surfaces) for image in range(10)]:
                x = randint(0, screen.width)
                y = randint(0, (self.horizon * TILE_SIZE) - 100)
                rect = surface.get_rect(midbottom=(x, y))
                self.clouds.append((surface, rect))

    def draw(self, surface: pygame.Surface) -> NoReturn:
        for row in range(VERTICAL_TILE_NUMBER):
            y = row * TILE_SIZE
            if row < self.horizon:
                surface.blit(self.top, (0, y))
            elif row == self.horizon:
                surface.blit(self.middle, (0, y))
            else:
                surface.blit(self.bottom, (0, y))
        if self.style == "menu":
            for palm in self.palms:
                surface.blit(palm[0], palm[1])
            for cloud in self.clouds:
                surface.blit(cloud[0], cloud[1])


class Water:
    def __init__(self, top: int, level_width: int):
        self.water_sprites = pygame.sprite.Group()
        water_decoration = graphics_dir('decoration/water')
        for tile in range(int((level_width + screen.width * 2) / 192)):
            sprite = AnimatedTile(192, tile * 192 + (-screen.width), top, water_decoration)
            self.water_sprites.add(sprite)

    def draw(self, surface: pygame.Surface, shift: int) -> NoReturn:
        self.water_sprites.update(shift)
        self.water_sprites.draw(surface)


class Clouds:
    def __init__(self, horizon: int, level_width: int, cloud_number: int):
        cloud_surf_list = ImportSupport.import_folder(graphics_dir('decoration/clouds'))
        self.cloud_sprites = pygame.sprite.Group()

        for cloud in range(cloud_number):
            cloud = choice(cloud_surf_list)
            sprite = StaticTile(
                0, randint(-screen.width, level_width + screen.width),
                randint(0, horizon), choice(cloud_surf_list)
            )
            self.cloud_sprites.add(sprite)

    def draw(self, surface: pygame.Surface, shift: int) -> NoReturn:
        self.cloud_sprites.update(shift)
        self.cloud_sprites.draw(surface)
