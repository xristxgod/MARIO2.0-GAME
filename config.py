import os


BASE_DIR = os.path.abspath(os.path.dirname(__file__))

GRAPHICS_DIR = os.path.join(BASE_DIR, "graphics")
TEXTURES_DIR = os.path.join(BASE_DIR, "textures")

LEVEL_DATA_DIR = os.path.join(TEXTURES_DIR, "level_data")
TILESETS_DIR = os.path.join(TEXTURES_DIR, "tilesets")

LEVEL_0 = os.path.join(TEXTURES_DIR, "level_0")
GRAPHICS_OVER_WORLD = os.path.join(GRAPHICS_DIR, "overworld")
GRAPHICS_OVER_WORLD_LEVEL_0 = os.path.join(GRAPHICS_OVER_WORLD, "level_0")