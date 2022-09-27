from typing import NoReturn
from typing import Optional

import pygame

from .menu import Menu, MenuData
from .level import Level, LevelData


class GameApp:
    MAX_LEVEL: int = 3

    def __init__(self, surface: pygame.Surface):
        self.screen = surface

        self.menu = Menu(MenuData(
            level=0,
            maxLevel=self.MAX_LEVEL,
            surface=self.screen,
            startLevel=self.create_level
        ))
        self.level = Level(LevelData(
            currentLevel=0,
            surface=self.screen,
            createMenu=self.create_menu
        ))
        self.status = "menu"

    def create_level(self, current_level: int) -> NoReturn:
        self.level = Level(LevelData(
            currentLevel=current_level,
            surface=self.screen,
            createMenu=self.create_menu
        ))
        self.status = f"Level: {current_level}"

    def create_menu(self, current_level: int, new_max_level: int) -> NoReturn:
        if new_max_level > self.MAX_LEVEL:
            self.MAX_LEVEL = new_max_level
        self.menu = Menu(MenuData(
            level=current_level,
            maxLevel=self.MAX_LEVEL,
            surface=self.screen,
            startLevel=self.create_level
        ))

    def run(self):
        if self.status == "menu":
            self.menu.run()
        else:
            self.level.run()

