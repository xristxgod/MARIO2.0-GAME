import pygame

from .settings import screen
from .game_data import levels


class Level:
    def __init__(self, current_level, surface):
        self.display_surface = surface
        self.current_level = current_level

        level_data = levels[self.current_level]
        level_content = level_data["content"]
        self.new_max_level = level_data["unlock"]

        self.font = pygame.font.Font(None, 40)
        self.text_surf = self.font.render(level_content, True, "White")
        self.text_rect = self.text_surf.get_rect(center=(screen.width / 2, screen.height / 2))

    def run(self):
        self.display_surface.blit(self.text_surf, self.text_rect)
