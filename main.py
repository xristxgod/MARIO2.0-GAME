
def main():
    import sys
    import pygame
    from src.settings import ScreenConfig

    pygame.init()
    screen = pygame.display.set_mode(ScreenConfig().screen)
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill("black")

        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    main()