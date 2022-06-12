
import enum


class Pixel(enum.Enum):
    NONE = ' '
    BORDER = '='
    CHARACTER = 'o'
    ENEMY = 'x'


class Key(enum.Enum):
    ESC = 'Esc'
    UP = 'up'
    DOWN = 'down'
    LEFT = 'left'
    RIGHT = 'right'


class Direction(enum.IntEnum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

