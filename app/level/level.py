from typing import NoReturn, Callable
from dataclasses import dataclass

import pygame

from ..base import BaseController
from ..settings import screen
from ..data import levels


@dataclass()
class LevelData:
    currentLevel: int
    surface: pygame.Surface
    createMenu: Callable


class Level(BaseController):
    def __init__(self, level: LevelData):
        self.display_surface = level.surface
        self.current_level = level.currentLevel

        level_content = 'Not found'

        self.new_level = levels[self.current_level].unlock
        self.back_to_menu = level.createMenu

        self.font = pygame.font.Font(None, 40)
        self.text_surf = self.font.render(level_content, True, "White")
        self.text_rect = self.text_surf.get_rect(center=(screen.width / 2, screen.height / 2))

    def input(self) -> NoReturn:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            self.back_to_menu(self.current_level, self.new_level)
        if keys[pygame.K_ESCAPE]:
            self.back_to_menu(self.current_level, 0)

    def run(self) -> NoReturn:
        self.input()
        self.display_surface.blit(self.text_surf, self.text_rect)


__all__ = [
    "LevelData",
    "Level"
]
