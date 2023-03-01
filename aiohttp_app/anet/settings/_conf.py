import pathlib

__all__ = ("BASE_DIR",)

BASE_DIR = pathlib.Path(__file__).parent.parent.absolute()