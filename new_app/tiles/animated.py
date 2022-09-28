import typing

from ..base import BaseTile

from ..supports import ImportSupport


class AnimatedTile(BaseTile):
    def __init__(self, size: int, x: int, y: int, path: str):
        super(AnimatedTile, self).__init__(size, x, y)
        self.frames = ImportSupport.import_folder(path)
        self.frame_index = 0
        self.image = self.frames[self.frame_index]

    def animate(self) -> typing.NoReturn:
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


__all__ = [
    "AnimatedTile",
    "Coin",
    "Palm"
]
