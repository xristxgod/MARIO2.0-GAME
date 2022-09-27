from .overworld import OverWorld
from .levels import Level


class Game:

    def __init__(self, screen):
        self.max_level = 3
        self.over_world = OverWorld(0, self.max_level, screen, self.create_level())
        self.level = Level(1, screen)

    def create_level(self):
        pass

    def run(self):
        self.over_world.run()
