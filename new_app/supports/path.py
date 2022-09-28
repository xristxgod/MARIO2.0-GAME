import os

import config


def _validate_dir(func):
    def wrapper(*args, **kwargs):
        result: str = func(*args, **kwargs)
        if result.find(".") < 0 and not os.path.isdir(result):
            raise NotADirectoryError
        elif result.find(".") >= 0 and not os.path.isfile(result):
            raise FileNotFoundError
        return result
    return wrapper


class _BaseDir:
    DIR: str

    @_validate_dir
    def __call__(self, path: str) -> str:
        if path.find("/") < 0:
            return os.path.join(self.DIR, path)
        absolute_path = self.DIR
        for p in path.split("/"):
            absolute_path = os.path.join(absolute_path, p)
        return absolute_path


class TextureDir(_BaseDir):
    DIR = os.path.join(config.FILES_DIR, "textures")


class LevelDir(_BaseDir):
    DIR = os.path.join(config.FILES_DIR, "levels")


class SoundDir(_BaseDir):
    DIR = os.path.join(config.FILES_DIR, "sounds")


__all__ = [
    "TextureDir", "LevelDir", "SoundDir"
]
