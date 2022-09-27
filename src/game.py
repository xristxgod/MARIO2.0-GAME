from .overworld import OverWorld
from .levels import Level


class Game:

    def __init__(self, screen):
        self.screen = screen
        self.max_level = 3
        self.over_world = OverWorld(0, self.max_level, self.screen, self.create_level)
        self.level = Level(1, screen, self.create_over_world)
        self.status = "over_world"

    def create_level(self, current_level):
        self.level = Level(current_level, self.screen, self.create_over_world)
        self.status = f"level {current_level}"

    def create_over_world(self, current_level, new_max_level):
        if new_max_level > self.max_level:
            self.max_level = new_max_level
        self.over_world = OverWorld(
            current_level,
            self.max_level,
            self.screen,
            self.create_level
        )
        self.status = "over_world"

    def run(self):
        if self.status == "over_world":
            self.over_world.run()
        else:
            self.level.run()