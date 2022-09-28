from typing import NoReturn

import pygame

from app.inc import ImportSupport, graphics_dir


class Tile(pygame.sprite.Sprite):
    def __init__(self, size: int, x: int, y: int):
        super(Tile, self).__init__()
        self.image = pygame.Surface((size, size))
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self, shift: int) -> NoReturn:
        self.rect.x += shift


class StaticTile(Tile):
    def __init__(self, size: int, x: int, y: int, surface: pygame.Surface):
        super(StaticTile, self).__init__(size, x, y)
        self.image = surface


class Crate(StaticTile):
    def __init__(self, size: int, x: int, y: int):
        super().__init__(size, x, y, pygame.image.load(graphics_dir("terrain/crate.png")).convert_alpha())
        self.rect = self.image.get_rect(bottomleft=(x, y + size))


class AnimatedTile(Tile):
    def __init__(self, size: int, x: int, y: int, path: str):
        super(AnimatedTile, self).__init__(size, x, y)
        self.frames = ImportSupport.import_folder(path)
        self.frame_index = 0
        self.image = self.frames[self.frame_index]

    def animate(self) -> NoReturn:
        self.frame_index += 0.15
        if self.frame_index >= len(self.frames):
            self.frame_index = 0
        self.image = self.frames[int(self.frame_index)]

    def update(self, shift: int):
        self.animate()
        self.rect.x += shift


class Coin(AnimatedTile):
    def __init__(self, size: int, x: int, y: int, path: str, value):
        super(Coin, self).__init__(size, x, y, path)
        self.rect = self.image.get_rect(center=(x + int(size / 2), y + int(size / 2)))
        self.value = value


class Palm(AnimatedTile):
    def __init__(self, size: int, x: int, y: int, path: str, offset: int):
        super(Palm, self).__init__(size, x, y, path)
        self.rect.topleft = (x, y - offset)
