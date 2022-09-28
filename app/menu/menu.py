from typing import NoReturn, Callable
from typing import Optional
from dataclasses import dataclass

import pygame

from ..base import BaseController
from ..data import levels
from ..level import Sky
from .node import Node, Icon


@dataclass()
class MenuData:
    level: int
    maxLevel: int
    surface: pygame.Surface
    startLevel: Callable


class Menu(BaseController):
    def __init__(self, menu: MenuData):
        self.display_surface = menu.surface
        self.max_level = menu.maxLevel
        self.current_level = menu.level

        self.create_level = menu.startLevel

        self.nodes: Optional[pygame.sprite.Sprite] = None
        self.icon: Optional[pygame.sprite.GroupSingle] = None
        self.sky: Optional[Sky] = Sky(8, 'menu')

        self.moving = False
        self.move_direction = pygame.math.Vector2(0, 0)
        self.speed = 8

        self.setup()

        self.start_time = pygame.time.get_ticks()
        self.allow_input = False
        self.timer_length = 300

    # Setups
    def setup(self):
        self.setup_nodes()
        self.setup_icon()
        self.setup_sky()

    def setup_nodes(self) -> NoReturn:
        """Setup nodes"""
        self.nodes = pygame.sprite.Group()
        for i, level in enumerate(levels):
            if i <= self.max_level:
                node = Node(level.nodePosition, "available", self.speed, level.nodeGraphic)
            else:
                node = Node(level.nodePosition, "locked", self.speed, level.nodeGraphic)
            self.nodes.add(node)

    def setup_icon(self) -> NoReturn:
        """Setup icon"""
        self.icon = pygame.sprite.GroupSingle()
        icon = Icon(self.nodes.sprites()[self.current_level].rect.center)
        self.icon.add(icon)

    def setup_sky(self) -> NoReturn:
        # self.sky = Sky(8,'overworld')
        pass

    # Draw
    def draw_paths(self) -> NoReturn:
        if self.max_level > 0:
            points = [node.nodePosition for i, node in enumerate(levels) if i <= self.max_level]
            pygame.draw.lines(self.display_surface, "#a04f45", False, points, 6)

    # Controller & Logic
    def get_move_data(self, target: str) -> pygame.math.Vector2:
        start = pygame.math.Vector2(self.nodes.sprites()[self.current_level].rect.center)
        if target == "next":
            end = pygame.math.Vector2(self.nodes.sprites()[self.current_level + 1].rect.center)
        else:
            end = pygame.math.Vector2(self.nodes.sprites()[self.current_level - 1].rect.center)
        return (end - start).normalize()

    def update_icon_position(self) -> NoReturn:
        if self.moving and self.move_direction:
            self.icon.sprite.position += self.move_direction * self.speed
            target_node = self.nodes.sprites()[self.current_level]
            if target_node.detection_zone.collidepoint(self.icon.sprite.position):
                self.moving = False
                self.move_direction = pygame.math.Vector2(0, 0)

    def input_timer(self) -> NoReturn:
        if not self.allow_input:
            current_time = pygame.time.get_ticks()
            if current_time - self.start_time >= self.timer_length:
                self.allow_input = True

    def input_key(self) -> NoReturn:
        keys = pygame.key.get_pressed()
        if not self.moving:
            if (keys[pygame.K_RIGHT] or keys[pygame.K_UP]) and self.current_level < self.max_level:
                self.move_direction = self.get_move_data("next")
                self.current_level += 1
                self.moving = True
            elif (keys[pygame.K_LEFT] or keys[pygame.K_DOWN]) and self.current_level > 0:
                self.move_direction = self.get_move_data("previous")
                self.current_level -= 1
                self.moving = True
            elif keys[pygame.K_SPACE]:
                self.create_level(self.current_level)

    # Inputs
    def input(self) -> NoReturn:
        self.input_timer()
        self.input_key()

    # Update
    def update(self) -> NoReturn:
        self.update_icon_position()
        self.icon.update()
        self.nodes.update()

    # Draw
    def draw(self):
        self.sky.draw(self.display_surface)
        self.draw_paths()
        self.nodes.draw(self.display_surface)
        self.icon.draw(self.display_surface)

    def run(self) -> NoReturn:
        self.input()
        self.update()
        self.draw()


__all__ = [
    "MenuData",
    "Menu"
]
