from typing import NoReturn


class BaseController:

    def input(self) -> NoReturn:
        raise NotImplementedError

    def run(self) -> NoReturn:
        raise NotImplementedError
