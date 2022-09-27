from typing import Tuple


class ScreenConfig:
    _SCREEN_WIDTH = 1280
    _SCREEN_HEIGHT = 720

    @property
    def screen(self) -> Tuple[int, int]:
        return self._SCREEN_WIDTH, self._SCREEN_HEIGHT
