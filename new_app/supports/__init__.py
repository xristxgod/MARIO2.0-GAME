from .path import TextureDir, LevelDir, SoundDir
from .imports import ImportSupport


texture_dir = TextureDir()
level_dir = LevelDir()
sound_dir = SoundDir()

support = ImportSupport


__all__ = [
    "texture_dir", "level_dir", "sound_dir",
    "ImportSupport",
    "support"
]
