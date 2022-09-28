import pygame


class Icon(pygame.sprite.Sprite):
    def __init__(self, position: Tuple[int, int]):
        super(Icon, self).__init__()
        self.position = position
        self.image = pygame.Surface((20, 20))
        self.image.fill("blue")
        self.rect = self.image.get_rect(center=position)

    def update(self):
        self.rect.center = self.position


__all__ = [
    "Icon"
]
