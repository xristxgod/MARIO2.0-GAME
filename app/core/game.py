from typing import NoReturn
from typing import Optional

import pygame

from app.settings import Condition
from app.supports import sound_dir
from app.menu import Menu, MenuData
from app.core.ui import UI
from app.level import Level, LevelData


class GameApp:
    MAX_LEVEL: int = 2
    MAX_HEALTH: int = 100

    def __init__(self, surface: pygame.Surface):
        self.screen = surface

        self.current_health = 100
        self.coins = 0

        self.level_bg_music = pygame.mixer.Sound(sound_dir("level_music.wav"))
        self.menu_bg_music = pygame.mixer.Sound(sound_dir("menu_music.wav"))

        self.level: Optional[Level] = None
        self.menu = Menu(MenuData(
            level=0,
            maxLevel=self.MAX_LEVEL,
            surface=self.screen,
            startLevel=self.create_level
        ))
        self.menu_bg_music.play(loops=-1)

        self.status = Condition.menu
        self.ui = UI(self.screen)

    def create_level(self, current_level: int) -> NoReturn:
        self.level = Level(LevelData(
            currentLevel=current_level,
            surface=self.screen,
            createMenu=self.create_menu,
            changeCoins=self.change_coins,
            health=self.change_health
        ))
        self.status = Condition.level
        self.menu_bg_music.stop()
        self.level_bg_music.play(loops=-1)

    def create_menu(self, current_level: int, new_max_level: int) -> NoReturn:
        if new_max_level > self.MAX_LEVEL:
            self.MAX_LEVEL = new_max_level
        self.menu = Menu(MenuData(
            level=current_level,
            maxLevel=self.MAX_LEVEL,
            surface=self.screen,
            startLevel=self.create_level
        ))
        self.status = Condition.menu
        self.level_bg_music.stop()
        self.menu_bg_music.play(loops=-1)

    def change_coins(self, amount: int):
        self.coins += amount

    def change_health(self, health: int):
        self.current_health += health

    def check_game_over(self):
        if self.current_health <= 0:
            self.current_health = 100
            self.coins = 0
            self.MAX_LEVEL = 0
            self.menu = Menu(MenuData(
                level=0,
                maxLevel=self.MAX_LEVEL,
                surface=self.screen,
                startLevel=self.create_level
            ))
            self.status = Condition.menu
            self.level_bg_music.stop()
            self.menu_bg_music.play(loops=-1)

    def run(self):
        if self.status == Condition.menu:
            self.menu.run()
        else:
            self.level.run()
            self.ui.health(self.current_health, self.MAX_HEALTH)
            self.ui.coins(self.coins)
            self.check_game_over()


__all__ = [
    "GameApp"
]
