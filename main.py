
def main():
    import sys

    import pygame

    from src.settings import screen as sr
    from src.game import Game

    pygame.init()
    screen = pygame.display.set_mode(sr.screen)
    print(type(screen))
    clock = pygame.time.Clock()
    game = Game(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill("black")
        game.run()

        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    main()