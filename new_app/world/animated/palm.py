from new_app.tiles import AnimatedTile


class Palm(AnimatedTile):
    def __init__(self, size: int, x: int, y: int, path: str, offset: int):
        super(Palm, self).__init__(size, x, y, path)
        self.rect.topleft = (x, y - offset)


__all__ = [
    "Palm"
]
