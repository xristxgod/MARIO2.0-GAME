from typing import Tuple


LEVELS_COUNT: Tuple[int, int] = (0, 5)


class ScreenConfig:
    _SCREEN_WIDTH = 1280
    _SCREEN_HEIGHT = 720

    @property
    def width(self) -> int:
        return self._SCREEN_WIDTH

    @property
    def height(self) -> int:
        return self._SCREEN_HEIGHT

    @property
    def screen(self) -> Tuple[int, int]:
        return self._SCREEN_WIDTH, self._SCREEN_HEIGHT


screen = ScreenConfig()


__all__ = [
    "screen"
]
