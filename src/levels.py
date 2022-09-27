import pygame

from .settings import screen
from .game_data import levels


class Level:
    def __init__(self, current_level, surface, create_over_world):
        self.display_surface = surface
        self.current_level = current_level

        level_data = levels[self.current_level]
        level_content = level_data["content"]
        self.new_max_level = level_data["unlock"]
        self.create_over_world = create_over_world

        self.font = pygame.font.Font(None, 40)
        self.text_surf = self.font.render(level_content, True, "White")
        self.text_rect = self.text_surf.get_rect(center=(screen.width / 2, screen.height / 2))

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            self.create_over_world(self.current_level, self.new_max_level)
        if keys[pygame.K_ESCAPE]:
            self.create_over_world(self.current_level, 0)

    def run(self):
        self.input()
        self.display_surface.blit(self.text_surf, self.text_rect)
