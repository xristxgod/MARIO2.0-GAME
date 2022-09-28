from new_app.tiles import AnimatedTile


class Coin(AnimatedTile):
    def __init__(self, size: int, x: int, y: int, path: str, value):
        super(Coin, self).__init__(size, x, y, path)
        self.rect = self.image.get_rect(center=(x + int(size / 2), y + int(size / 2)))
        self.value = value


__all__ = [
    "Coin"
]
