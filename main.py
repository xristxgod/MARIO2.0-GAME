
def main():
    import sys

    import pygame

    import app
    from app.settings import screen as sr

    pygame.init()
    screen = pygame.display.set_mode(sr.screen)
    clock = pygame.time.Clock()
    game = app.GameApp(screen)

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
