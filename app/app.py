from typing import NoReturn
from typing import Optional

import pygame

import menu
import level


class GameApp:
    MAX_LEVEL: int = 0
    SCREEN: pygame.Surface
    INSTANCE: Optional['GameApp']

    def __new__(cls, *args, **kwargs):
        if cls.INSTANCE is None:
            cls.SCREEN = kwargs.get("screen")
            cls.instance = super(GameApp, cls).__new__(cls, *args, **kwargs)
        return cls.INSTANCE

    def __init__(self, surface: pygame.Surface):
        self.menu = menu.Menu(menu.MenuData(
            level=0,
            maxLevel=self.MAX_LEVEL,
            surface=surface,
            startLevel=self.create_level
        ))
        self.level = level.Level(level.LevelData(
            currentLevel=0,
            surface=surface,
            createMenu=self.create_menu
        ))
        self.status = "menu"

    def create_level(self, current_level: int) -> NoReturn:
        self.level = level.Level(level.LevelData(
            currentLevel=current_level,
            surface=self.SCREEN,
            createMenu=self.create_menu
        ))
        self.status = f"Level: {current_level}"

    def create_menu(self, current_level: int, new_max_level: int) -> NoReturn:
        if new_max_level > self.MAX_LEVEL:
            self.MAX_LEVEL = new_max_level
        self.menu = menu.Menu(menu.MenuData(
            level=current_level,
            maxLevel=self.MAX_LEVEL,
            surface=self.SCREEN,
            startLevel=self.create_level
        ))

    def run(self):
        if self.status == "menu":
            self.menu.run()
        else:
            self.level.run()

