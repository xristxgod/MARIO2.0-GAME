from typing import Optional

import pygame


class GameApp:
    MAX_LEVEL: int = 0
    SCREEN: pygame.Surface
    INSTANCE: Optional['GameApp']

    def __new__(cls, *args, **kwargs):
        if cls.INSTANCE is None:
            cls.SCREEN = kwargs.get("screen")
            cls.instance = super(GameApp, cls).__new__(cls, *args, **kwargs)
        return cls.INSTANCE

    def __init__(self, screen: pygame.Surface):
        self.menu = ""
        self.level = ""
        self.status = "menu"

    def create_level(self):
        pass

    def create_menu(self):
        pass

    def run(self):
        if self.status == "menu":
            self.create_menu().run()
        else:
            self.level.run()


m = Game("fsda")
