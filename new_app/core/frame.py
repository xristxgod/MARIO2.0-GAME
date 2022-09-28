import typing


class FPS:
    def __init__(self, index: int = 0):
        self._index = index

    @property
    def index(self) -> int:
        return self._index

    @index.setter
    def index(self, value: int) -> typing.NoReturn:
        self._index = value


__all__ = [
    "FPS"
]
