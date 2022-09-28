import typing

from new_app.base import BaseTile

from new_app.core import FPS
from new_app.supports import ImportSupport


class AnimatedTile(BaseTile):
    def __init__(self, size: int, x: int, y: int, path: str):
        super(AnimatedTile, self).__init__(size, x, y)
        self.frames = ImportSupport.import_folder(path)
        self.fps = FPS()
        self.image = self.frames[self.fps.index]

    def animate(self) -> typing.NoReturn:
        self.fps.index += 0.15
        if self.fps.index >= len(self.frames):
            self.fps.index = 0
        self.image = self.frames[int(self.fps.index)]

    def update(self, shift: int):
        self.animate()
        self.rect.x += shift


__all__ = [
    "AnimatedTile"
]
