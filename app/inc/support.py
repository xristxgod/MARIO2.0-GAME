import os
import csv
from typing import List

import pygame

from ..settings import TILE_SIZE


class Importer:
    @staticmethod
    def import_folder(path: str) -> List:
        surface_list = []
        for _, __, image_files in os.walk(path):
            for image in image_files:
                full_path = os.path.join(path, image)
                image_surf = pygame.image.load(full_path).convert_alpha()
                surface_list.append(image_surf)
        return surface_list

    @staticmethod
    def import_csv_layout(path: str) -> List:
        terrain_map = []
        with open(path) as file:
            level = csv.reader(file, delimiter=',')
            for row in level:
                terrain_map.append(list(row))
        return terrain_map

    @staticmethod
    def import_cut_graphics(path: str) -> List:
        surface = pygame.image.load(path).convert_alpha()
        tile_num_x = int(surface.get_size()[0] / TILE_SIZE)
        tile_num_y = int(surface.get_size()[1] / TILE_SIZE)
        cut_tiles = []
        for row in range(tile_num_y):
            for col in range(tile_num_x):
                x = col * TILE_SIZE
                y = row * TILE_SIZE
                new_surf = pygame.Surface((TILE_SIZE, TILE_SIZE), flags=pygame.SRCALPHA)
                new_surf.blit(surface, (0, 0), pygame.Rect(x, y, TILE_SIZE, TILE_SIZE))
                cut_tiles.append(new_surf)
        return cut_tiles


__all__ = [
    "Importer"
]
