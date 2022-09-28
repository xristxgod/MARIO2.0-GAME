from typing import NoReturn

import pygame

from ..supports import texture_dir


class UI:
    HEALTH_BAR_TOP_LEFT = (54, 39)
    BAR_WIDTH = 152
    BAR_HEIGHT = 4

    def __init__(self, surface: pygame.Surface):
        self.HEALTH_BAR = pygame.image.load(texture_dir("ui/health_bar.png")).convert_alpha()
        self.COIN = pygame.image.load(texture_dir("ui/coin.png")).convert_alpha()
        self.FONT = pygame.font.Font(texture_dir("ui/ARCADEPI.ttf"), 30)

        self.display_surface = surface

        self.coin_rect = self.COIN.get_rect(topleft=(50, 61))

    def health(self, current: int, full: int) -> NoReturn:
        self.display_surface.blit(self.HEALTH_BAR, (20, 10))
        pygame.draw.rect(
            self.display_surface,
            '#dc4949',
            pygame.Rect(self.HEALTH_BAR_TOP_LEFT, (self.BAR_WIDTH * (current / full), self.BAR_HEIGHT))
        )

    def coins(self, amount: int) -> NoReturn:
        self.display_surface.blit(self.COIN, self.coin_rect)
        coin_amount_surf = self.FONT.render(str(amount), False, '#33323d')
        coin_amount_rect = coin_amount_surf.get_rect(midleft=(self.coin_rect.right + 4, self.coin_rect.centery))
        self.display_surface.blit(coin_amount_surf, coin_amount_rect)


__all__ = [
    "UI"
]
