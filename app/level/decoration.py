from random import choice, randint

import pygame

from ..settings import VERTICAL_TILE_NUMBER, TILE_SIZE
from ..inc import graphics_dir
from .tiles import AnimatedTile, StaticTile


class Sky:
    def __init__(self, horizon: str, style: str = 'level'):
        self.top = pygame.image.load(graphics_dir("decoration/sky/sky_top.png")).convert()
        self.bottom = pygame.image.load(graphics_dir("decoration/sky/sky_bottom.png")).convert()
        self.middle = pygame.image.load(graphics_dir("decoration/sky/sky_middle.png'")).convert()
