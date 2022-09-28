import sys
import pygame

from app.core import GameApp
from app.settings import screen as sr


def run_app():
    pygame.init()
    screen = pygame.display.set_mode(sr.screen)
    clock = pygame.time.Clock()
    game = GameApp(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill("black")
        game.run()

        pygame.display.update()
        clock.tick(60)


__all__ = [
    "run_app"
]
